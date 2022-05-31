import json
from src.domain.events import Event


def validate_register(registration_machine):

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
