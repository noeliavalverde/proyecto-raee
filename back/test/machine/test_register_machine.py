from datetime import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_register_one_machine():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": "2022-08-05 22:36:00",
        "event": "register",
        "payload": {
            "brand": "samsung",
            "model": "samsung_3",
        },
    }

    response = client.post("/api/process/register", json=event)
    assert response.status_code == 200


def test_should_not_register_one_machine_if_is_already_registered():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    register1_event = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-06-15 09:33:00",
        event="register",
        payload=[],
    )

    event_repository.save_event(register1_event)

    event = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-08-05 22:36:00",
        "payload": {
            "brand": "samsung",
            "model": "samsung_3",
        },
    }

    response = client.post("/api/process/register", json=event)
    assert response.status_code == 400
