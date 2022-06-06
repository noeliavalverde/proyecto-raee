import json
from src.domain.events import Event, EventRepository
import sqlite3


def validate_register_contains_brand_and_model(registration_machine):

    event_dict = registration_machine.to_dict()
    payload = event_dict["payload"]

    brand = payload["brand"]
    model = payload["model"]

    if brand == "":
        return False

    elif model == "":
        return False

    elif brand == " ":
        return False

    elif model == " ":
        return False

    else:
        return True


def validate_register_contains_not_empty_id(registration_machine):

    event_dict = registration_machine.to_dict()
    id_machine = event_dict["id_machine"]

    if id_machine == "":
        return False
    elif id_machine == " ":
        return False


def validate_id_not_existing(event, repositories):

    event_dict = event.to_dict()
    id_machine = event_dict["id_machine"]
    event_by_id = repositories["event"].get_event_by_machine_id(id_machine)

    if event_by_id == None:
        return True
    else:
        return False
