from flask import Flask, request
from flask_cors import CORS
from src.domain.events import Event

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/process/register", methods=["POST"])
    def register_machine_event():
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

    return app
