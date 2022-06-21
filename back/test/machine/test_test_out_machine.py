import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_test_out_one_machine():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    test_event = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-05-30 17:26:00",
        event="test_in",
        payload={},
    )

    event_repository.save_event(test_event)

    event = {
        "id_machine": "machine-1",
        "employee": "operario-007",
        "timestamp": "2022-05-30 17:27:00",
        "event": "test_out",
        "payload": {},
    }

    response = client.post("/api/process/test/exit", json=event)
    assert response.status_code == 200


def test_should_not_save_one_machine_at_test_out_if_is_already_registered():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    test_event = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-05-30 17:26:00",
        event="test_out",
        payload={},
    )

    event_repository.save_event(test_event)

    event = {
        "id_machine": "machine-1",
        "employee": "operario-007",
        "timestamp": "2022-05-30 17:27:00",
        "payload": {},
    }

    response = client.post("/api/process/test/exit", json=event)
    assert response.status_code == 400
