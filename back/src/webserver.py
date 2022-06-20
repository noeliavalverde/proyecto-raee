from flask import Flask, request, jsonify
from flask_cors import CORS
from src.domain.events import Event
from src.validations_endpoints.validations_general import *
from src.domain.projections.supplyline import *

from flasgger import Swagger

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)
    swagger = Swagger(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():

        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/process/register", methods=["POST"])
    def register_machine_event():

        """Endpoint to save the registration details of a machine

        ---
        parameters:
            -   in: body
                name: Register event
                description: Event to register a machine
                schema:
                    type: object
                    required:
                        - id_machine
                        - employee
                        - timestamp
                        - payload
                    properties:
                        id_machine:
                            type: uuid
                            description: An unique id for the machine
                            example: flgr0087
                        employee:
                            type: string
                            description: An employee id
                            example: operario-005
                        timestamp:
                            type: string
                            description: Register date in isoformat
                            example: "2022-05-25 00:00:00"
                            pattern: YY-MM-DD hh:mm:ss
                        payload:
                            type: object
                            description: An object containing brand and model of the machine
                            example: {brand: Balay, model: BAL5667}
                            items:
                                brand:
                                    type:string
                                model:
                                    type:string


        responses:
          200:
            description: Returns a 200 response. Registered.


        """
        data = request.json

        if not validate_datetime(data["timestamp"]):
            return ("Not isoformat date", 400)
        register_machine = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event="register",
            payload=data["payload"],
        )

        if validate_id_already_exists(register_machine, repositories):
            return ("ID already existing", 400)
        if not validate_register_contains_brand_and_model(register_machine):
            return ("Empty brand or model fields", 400)

        repositories["event"].save_event(register_machine)
        return "", 200

    @app.route("/api/process/diagnostic/enter", methods=["POST"])
    def diagnostic_machine_enter():
        """Endpoint to register the timestamp when a machine gets into diagnostic process

        ---
        parameters:
            -   in: body
                name: event
                description: Enter timestamp of a machine at diagnostic process.
                schema:
                    type: object
                    required:
                        - id_machine
                        - employee
                        - timestamp
                    properties:
                        id_machine:
                            type: uuid
                            description: A unique id for the machine
                            example: flgr0087
                        employee:
                            type: string
                            description: An employee id
                            example: operario-005
                        timestamp:
                            type: string
                            description: Date in isoformat
                            example: "2022-05-25 00:00:00"
                            pattern: YY-MM-DD hh:mm:ss
                        payload:
                            type: object
                            description:
                            example: {docs: }
                            items:
                                docs:
                                    type:string



        responses:
          200:
            description: Returns a 200 response. Diagnostic in event registered.
          400:
            description: Returns 400. The id_machine introduced is not already registered, or invalid isoformat date.



        """

        data = request.json

        if not validate_datetime(data["timestamp"]):
            return ("Not isoformat date", 400)
        event = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event="diagnostic_in",
            payload=data["payload"],
        )

        if not validate_previous_event_is_already_registered(
            event, "register", repositories
        ):
            return ("ID not already registered at REGISTER event", 400)

        if validate_previous_event_is_already_registered(
            event, "diagnostic_in", repositories
        ):
            return ("this ID is already registered at diagnostic in", 400)

        if not validate_datetime_is_later_than_previous_event(
            event, "register", repositories
        ):
            return ("Introduced date is previous than register date", 400)

        repositories["event"].save_event(event)
        return "", 200

    @app.route("/api/process/diagnostic/exit", methods=["POST"])
    def diagnostic_machine_exit():
        """Endpoint to register the timestamp when a machine gets out of diagnostic process. It also registers the next process that the machine needs, repair, test, valid, detachable
        ---
        parameters:
            -   in: body
                name: event
                description: Exit timestamp of a machine at diagnostic process.
                schema:
                    type: object
                    required:
                        - id_machine
                        - employee
                        - timestamp
                        - payload
                    properties:
                        id_machine:
                            type: uuid
                            description: A unique id for the machine
                            example: flgr0087
                        employee:
                            type: string
                            description: An employee id
                            example: operario-005
                        timestamp:
                            type: string
                            description: Date in isoformat
                            example: "2022-05-25 00:00:00"
                            pattern: YY-MM-DD hh:mm:ss
                        payload:
                            type: object
                            description: An object containing next step of the process. Must be "repair", "test", "valid" or "detachable"
                            example: {"next_event": "repair"}


        responses:
          200:
            description: Returns a 200 response. Registered.


        """

        data = request.json

        if not validate_datetime(data["timestamp"]):
            return ("Not isoformat date", 400)
        diagnostic_event = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event="diagnostic_out",
            payload=data["payload"],
        )
        if not validate_previous_event_is_already_registered(
            diagnostic_event, "diagnostic_in", repositories
        ):
            return ("ID not already registered at DIAGNOSTIC_IN event", 400)
        if validate_previous_event_is_already_registered(
            diagnostic_event, "diagnostic_out", repositories
        ):
            return ("ID already registered at DIAGNOSTIC_OUT event", 400)

        if not validate_datetime_is_later_than_previous_event(
            diagnostic_event, "diagnostic_in", repositories
        ):
            return ("Introduced date is previous than DIAGNOSTIC_IN date", 400)

        repositories["event"].save_event(diagnostic_event)
        return "", 200

    @app.route("/api/process/repair/enter", methods=["POST"])
    def repair_machine_enter():
        """Endpoint to register the timestamp when a machine gets into repair process
        ---
        parameters:
            -   in: body
                name: event
                description: Enter timestamp of a machine at repair process.
                schema:
                    type: object
                    required:
                        - id_machine
                        - employee
                        - timestamp
                        - event
                        - payload
                    properties:
                        id_machine:
                            type: uuid
                            description: A unique id for the machine
                            example: flgr0087
                        employee:
                            type: string
                            description: An employee id
                            example: operario-005
                        timestamp:
                            type: string
                            description: Date in isoformat
                            example: "2022-05-25 00:00:00"
                            pattern: YY-MM-DD hh:mm:ss
                        event:
                            type: string
                            description: Specific event
                            example: repair_in
                            default: repair_in
                        payload:
                            type: object
                            example: {}


        responses:
          200:
            description: Returns a 200 response. Registered.


        """

        data = request.json
        if data["event"] == "repair_in":
            if validate_datetime(data["timestamp"]):
                repair_event = Event(
                    id_machine=data["id_machine"],
                    employee=data["employee"],
                    timestamp=data["timestamp"],
                    event=data["event"],
                    payload=data["payload"],
                )
                if validate_datetime_is_later_than_previous_event(
                    repair_event, "diagnostic_out", repositories
                ):
                    if validate_previous_event_is_already_registered(
                        repair_event, "diagnostic_out", repositories
                    ):
                        repositories["event"].save_event(repair_event)
                        return "", 200
                    else:
                        return (
                            "ID not already registered at DIAGNOSTIC_OUT event",
                            400,
                        )
                else:
                    return ("Introduced date is previous than diagnostic_out date", 400)

            else:
                return ("Not isoformat date", 400)
        else:
            return ("Event name must be 'repair_in'", 400)

    @app.route("/api/process/repair/exit", methods=["POST"])
    def repair_machine_exit():

        """Endpoint to register the timestamp when a machine gets out of repair process
        ---
        parameters:
            -   in: body
                name: event
                description: Exit timestamp of a machine at repair process.
                schema:
                    type: object
                    required:
                        - id_machine
                        - employee
                        - timestamp
                        - event
                        - payload
                    properties:
                        id_machine:
                            type: uuid
                            description: A unique id for the machine
                            example: flgr0087
                        employee:
                            type: string
                            description: An employee id
                            example: operario-005
                        timestamp:
                            type: string
                            description: Date in isoformat
                            example: "2022-05-25 00:00:00"
                            pattern: YY-MM-DD hh:mm:ss
                        event:
                            type: string
                            description: Specific event
                            example: diagnostic_out
                            default: diagnostic_out
                        payload:
                            type: object
                            description: An object containing next step of process
                            example: {"next_event": "test"}
                            items:
                                next_event:
                                    type:string

        responses:
          200:
            description: Returns a 200 response. Registered.


        """

        data = request.json
        if data["event"] == "repair_out":
            if validate_datetime(data["timestamp"]):
                repair_event = Event(
                    id_machine=data["id_machine"],
                    employee=data["employee"],
                    timestamp=data["timestamp"],
                    event=data["event"],
                    payload=data["payload"],
                )
                if validate_datetime_is_later_than_previous_event(
                    repair_event, "repair_in", repositories
                ):
                    if validate_previous_event_is_already_registered(
                        repair_event, "repair_in", repositories
                    ):

                        repositories["event"].save_event(repair_event)
                        return "", 200
                    else:
                        return ("ID not already registered at REPAIR_IN event", 400)
                else:
                    return ("Introduced date is previous than REPAIR_IN date", 400)

            else:
                return ("Not isoformat date", 400)
        else:
            return ("Event name must be 'repair_out'", 400)

    @app.route("/api/process/test/enter", methods=["POST"])
    def test_machine_enter():

        """Endpoint to register the timestamp when a machine gets into test process
        ---
        parameters:
            -   in: body
                name: event
                description: Enter timestamp of a machine at test process.
                schema:
                    type: object
                    required:
                        - id_machine
                        - employee
                        - timestamp
                        - event
                        - payload
                    properties:
                        id_machine:
                            type: uuid
                            description: A unique id for the machine
                            example: flgr0025
                        employee:
                            type: string
                            description: An employee id
                            example: operario-005
                        timestamp:
                            type: string
                            description: Date in isoformat
                            example: "2022-05-25 00:00:00"
                            pattern: YY-MM-DD hh:mm:ss
                        event:
                            type: string
                            description: Specific event
                            example: test_in
                            default: test_in
                        payload:
                            type: object
                            example: {}


        responses:
          200:
            description: Returns a 200 response. Registered.


        """
        data = request.json
        if data["event"] == "test_in":
            if validate_datetime(data["timestamp"]):
                test_event = Event(
                    id_machine=data["id_machine"],
                    employee=data["employee"],
                    timestamp=data["timestamp"],
                    event=data["event"],
                    payload=data["payload"],
                )
                if validate_datetime_is_later_than_previous_event(
                    test_event, "diagnostic_out", repositories
                ):
                    if validate_previous_event_is_already_registered(
                        test_event, "diagnostic_out", repositories
                    ):
                        repositories["event"].save_event(test_event)
                        return "", 200
                    else:
                        return (
                            "ID not already registered at DIAGNOSTIC_OUT event",
                            400,
                        )
                else:
                    return ("Introduced date is previous than DIAGNOSTIC_OUT date", 400)

            else:
                return ("Not isoformat date", 400)
        else:
            return ("Event name must be 'test_in'", 400)

    @app.route("/api/process/test/exit", methods=["POST"])
    def test_machine_exit():

        """Endpoint to register the timestamp when a machine gets out of test process
        ---
        parameters:
            -   in: body
                name: event
                description: Exit timestamp of a machine at test process.
                schema:
                    type: object
                    required:
                        - id_machine
                        - employee
                        - timestamp
                        - event
                        - payload
                    properties:
                        id_machine:
                            type: uuid
                            description: A unique id for the machine
                            example: flgr0025
                        employee:
                            type: string
                            description: An employee id
                            example: operario-005
                        timestamp:
                            type: string
                            description: Date in isoformat
                            example: "2022-05-25 00:00:00"
                            pattern: YY-MM-DD hh:mm:ss
                        event:
                            type: string
                            description: Specific event
                            example: test_out
                            default: test_out
                        payload:
                            type: object
                            example: { "procedures": [
                                            {"title": "test 1", "is_completed": 0},
                                            {"title": "test 2", "is_completed": 0},
                                            ],
                                        }
        responses:
          200:
            description: Returns a 200 response. Registered.

        """
        data = request.json
        if data["event"] == "test_out":
            if validate_datetime(data["timestamp"]):
                test_event = Event(
                    id_machine=data["id_machine"],
                    employee=data["employee"],
                    timestamp=data["timestamp"],
                    event=data["event"],
                    payload=data["payload"],
                )
                if validate_datetime_is_later_than_previous_event(
                    test_event, "test_in", repositories
                ):
                    if validate_previous_event_is_already_registered(
                        test_event, "test_in", repositories
                    ):

                        repositories["event"].save_event(test_event)
                        return "", 200

                    else:
                        return ("ID not already registered at TEST_IN event", 400)
                else:
                    return ("Introduced date is previous than DIAGNOSTIC_OUT date", 400)

            else:
                return ("Not isoformat date", 400)
        else:
            return ("Event name must be 'test_out'", 400)

    @app.route("/api/process/scrap_inform", methods=["GET"])
    def get_info_for_scrap():

        all_events = repositories["event"].get_events()
        return object_to_json(all_events), 200

    @app.route("/api/process/<id_machine>", methods=["GET"])
    def get_by_id(id_machine):

        event = repositories["event"].get_events_by_machine_id(id_machine)
        return object_to_json(event)

    # Supply line routes

    @app.route("/api/analysis/collector", methods=["GET"])
    def get_collector():

        all_events_collected = supply_line_state_collector(repositories["event"])

        return all_events_collected, 200

    @app.route("/api/analysis/number_of_machines_in_each_event", methods=["GET"])
    def getnumber_of_machines_in_each_event():

        all_events = repositories["event"].get_events()
        # devuelve diccionario con key id_machine
        all_events_classified_by_id_machine = get_all_events_classified_by_id_machine(
            all_events
        )

        current_event_classified_by_id_machine = supply_line_current_state(
            all_events_classified_by_id_machine
        )
        number_of_machines_in_each_event = get_number_of_machines_in_each_event(
            current_event_classified_by_id_machine
        )

        return number_of_machines_in_each_event, 200

    @app.route("/api/analysis/supply_line_current_state", methods=["GET"])
    def get_id_machine_in_current_event():

        all_events = repositories["event"].get_events()
        # devuelve diccionario con key id_machine
        all_events_classified_by_id_machine = get_all_events_classified_by_id_machine(
            all_events
        )

        current_event_classified_by_id_machine = supply_line_current_state(
            all_events_classified_by_id_machine
        )

        return jsonify(current_event_classified_by_id_machine), 200

    return app
