from datetime import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app
from src.lib.utils import object_to_json


def test_should_validate_one_event_must_be_registered_in_to_be_in_out():

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    event_register = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2035-05-08 10:06",
        event="register",
        payload={"brand": "balay", "model": "bal2525"},
    )
    event_diagnostic = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2035-05-08 10:06",
        event="diagnostic_in",
        payload={},
    )

    event_repository.save_event(event_register)
    event_repository.save_event(event_diagnostic)

    event_diagnostic_out = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-06-15 09:33",
        "event": "diagnostic_out",
        "payload": {},
    }

    response = client.post("/api/process/diagnostic/exit", json=event_diagnostic_out)
    assert response.status_code == 200


def test_should_validate_repair_out_not_allowed_if_not_repair_in_registered():

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    event_diagnostic = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2035-05-08 10:06",
        event="diagnostic_in",
        payload={},
    )

    event_repository.save_event(event_diagnostic)

    event_repair_out = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-06-15 09:33",
        "event": "repair_out",
        "payload": {},
    }

    response = client.post("/api/process/repair/exit", json=event_repair_out)
    assert response.status_code == 400
