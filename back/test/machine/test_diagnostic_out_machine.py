import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_diagnostic_out_one_machine():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    event_diagnostic = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="diagnostic_in",
        payload={},
    )

    event_repository.save_event(event_diagnostic)

    event = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-05-08 10:07",
        "event": "diagnostic_out",
        "payload": [
            {"next_event": "repair"},
        ],
    }

    response = client.post("/api/process/diagnostic/exit", json=event)
    assert response.status_code == 200


def test_should_not_save_event_if_diagnostic_out_is_already_registered():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    event_diagnostic = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="diagnostic_out",
        payload={},
    )

    event_repository.save_event(event_diagnostic)

    event = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-05-08 10:07",
        "event": "diagnostic_out",
        "payload": [
            {"next_event": "repair"},
        ],
    }

    response = client.post("/api/process/diagnostic/exit", json=event)
    assert response.status_code == 400
