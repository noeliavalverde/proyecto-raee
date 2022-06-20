import json

from src.domain.events import Event, EventRepository
import sqlite3
from datetime import datetime


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


def validate_id_already_exists(event, repositories):

    event_dict = event.to_dict()
    id_machine = event_dict["id_machine"]
    event_by_id = repositories["event"].get_events_by_machine_id(id_machine)

    if event_by_id == []:
        return False
    else:
        return True


def validate_previous_event_is_already_registered(event, event_to_check, repositories):
    event_dict = event.to_dict()
    id_machine = event_dict["id_machine"]
    events_list = repositories["event"].get_events_by_machine_id(id_machine)

    for item in events_list:
        item_dict = item.to_dict()

        if item_dict["event"] == event_to_check:
            return True

    return False


def validate_datetime(date_str):

    try:
        datetime.fromisoformat(date_str)
    except ValueError:
        return False
    return True


def validate_datetime_is_later_than_previous_event(event, previous_event, repositories):
    event_dict = event.to_dict()
    id_machine = event_dict["id_machine"]
    events_list = repositories["event"].get_events_by_machine_id(id_machine)

    for item in events_list:
        item_dict = item.to_dict()

        if item_dict["event"] == previous_event:
            if item_dict["timestamp"] < event_dict["timestamp"]:
                return True
            else:
                return False
