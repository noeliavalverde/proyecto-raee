import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_test_one_machine():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    register_event = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="diagnostic_out",
        payload={"brand": "balay", "model": "bal2525"},
    )

    event_repository.save_event(register_event)

    event = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-07-08 10:06",
        "event": "test_in",
        "payload": {
            "procedures": [
                {"title": "test 1", "is_completed": 0},
                {"title": "test 2", "is_completed": 0},
            ],
        },
    }

    response = client.post("/api/process/test/enter", json=event)
    assert response.status_code == 200


def test_should_not_save_one_machine_at_test_in_if_is_already_registered():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    test_in_event = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="test_in",
        payload={"brand": "balay", "model": "bal2525"},
    )

    event_repository.save_event(test_in_event)

    event = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-07-08 10:06",
        "payload": {
            "procedures": [
                {"title": "test 1", "is_completed": 0},
                {"title": "test 2", "is_completed": 0},
            ],
        },
    }

    response = client.post("/api/process/test/enter", json=event)
    assert response.status_code == 400
