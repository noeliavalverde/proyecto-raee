import datetime

from src.domain.events import EventRepository
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_get_last_event_of_a_machine():
    # 1 - SET UP
    event_repo = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repo})
    client = app.test_client()

    register_event = {
        "id_machine": "m1",
        "employee": "empleado-1",
        "timestamp": "2022-05-01 09:02:55",
        "event": "register",
        "payload": [],
    }

    diagnostic_in_event = {
        "id_machine": "m1",
        "employee": "empleado-1",
        "timestamp": "2022-05-01 12:02:55",
        "event": "diagnostic_in",
        "payload": [],
    }

    diagnostic_out_event = {
        "id_machine": "m1",
        "employee": "empleado-1",
        "timestamp": "2022-06-01 09:32:55",
        "event": "diagnostic_out",
        "payload": [],
    }

    sending_post = client.post("/api/process/repair/exit", json=register_event)
    sending_post2 = client.post("/api/process/repair/exit", json=diagnostic_in_event)
    sending_post3 = client.post("/api/process/repair/exit", json=diagnostic_out_event)

    # 2 - CALLING THE METHOD TO TEST
    last_event = event_repo.get_last_event_by_id("m1")

    # 3 - COMPARING ACTUAL VALUES WITH PREDICTED <<<<<<<<<<<<<<<<<<<<RESULTS
    # Parsing the object Event 'last_event' to a diccionary
    last_event = last_event.to_dict()

    # Cheking if the posts have been received correctly
    assert sending_post.status_code == 200
    assert sending_post2.status_code == 200
    assert sending_post3.status_code == 200

    # Checking the last event
    assert last_event["id_machine"] == "m1"
    assert last_event["employee"] == "empleado-1"
    assert last_event["timestamp"] == "2022-06-01 09:32:55"
    assert last_event["event"] == "diagnostic_out"
