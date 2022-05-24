from flask import Flask, request
from flask_cors import CORS
from src.domain.events import Event
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

        """Endpoint to save a register data of machine
        This is using docstrings for specifications.
        ---
        parameters:
            -   in: body
                name: event
                description: The event to send
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
                            example: 125489621
                        employee:
                            type: string
                            description: An employee id
                            example: operario-005
                        timestamp:
                            type: date
                            description: Register date in isoformat
                            example: 2022-05-25
                        event:
                            type: string
                            description: Specific event
                            example: register
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
        register_machine = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event=data["event"],
            payload=data["payload"],
        )

        repositories["event"].save_event(register_machine)
        return "", 200

    @app.route("/api/process/diagnostic/enter", methods=["POST"])
    def diagnostic_machine_enter():
        data = request.json
        event = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event=data["event"],
            payload=data["payload"],
        )

        washer_event = repositories["event"].save_event(event)
        return "", 200



    @app.route("/api/process/diagnostic/exit", methods=["POST"])
    def diagnostic_machine_exit():
        data = request.json
        event = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event=data["event"],
            payload=data["payload"],
        )

        repositories["event"].save_event(event)
        return "", 200

    @app.route("/api/process/repair/enter", methods=["POST"])
    def repair_machine_enter():
        data = request.json
        event = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event=data["event"],
            payload=data["payload"],
        )

        repositories["event"].save_event(event)
        return "", 200

    @app.route("/api/process/repair/exit", methods=["POST"])
    def repair_machine_exit():
        data = request.json
        event = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event=data["event"],
            payload=data["payload"],
        )

        repositories["event"].save_event(event)
        return "", 200

    @app.route("/api/process/test/enter", methods=["POST"])
    def test_machine_enter():
        data = request.json
        event = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event=data["event"],
            payload=data["payload"],
        )

        repositories["event"].save_event(event)
        return "", 200

    @app.route("/api/process/test/exit", methods=["POST"])
    def test_machine_exit():
        data = request.json
        event = Event(
            id_machine=data["id_machine"],
            employee=data["employee"],
            timestamp=data["timestamp"],
            event=data["event"],
            payload=data["payload"],
        )

        repositories["event"].save_event(event)
        return "", 200

    @app.route("/api/process/scrap_inform", methods=["GET"])
    def get_info_for_scrap():

        all_events = repositories["event"].get_events()
        return object_to_json(all_events), 200

    return app
