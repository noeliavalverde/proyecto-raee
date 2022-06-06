from datetime import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app
import json


def test_should_get_one_machine_by_id():

    events_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": events_repository})
    client = app.test_client()

    event = Event(
        id_machine="machine-0005",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="register",
        payload={"brand": "balay", "model": "bal2525"},
    )

    event_dict = event.to_dict()

    client.post("/api/process/register", json=event_dict)
    r = client.get("/api/process/machine-0005")

    response = events_repository.get_event_by_machine_id("machine-0005")
    dict_event = response.to_dict()

    assert dict_event["id_machine"] == "machine-0005"


def test_should_get_machine_by_id():
    events_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": events_repository})
    client = app.test_client()

    event = Event(
        id_machine="machine-0005",
        employee="operario-007",
        timestamp="2022-05-08T10:06:00",
        event="register",
        payload={"brand": "balay", "model": "bal2525"},
    )

    events_repository.save_event(event)
    response = client.get("/api/process/machine-0005")
    assert response.json == {
        "id_machine": "machine-0005",
        "employee": "operario-007",
        "timestamp": "2022-05-08 10:06:00",
        "event": "register",
        "payload": {"brand": "balay", "model": "bal2525"},
    }
