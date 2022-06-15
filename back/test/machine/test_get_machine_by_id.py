from datetime import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app
import json


def test_should_get_all_events_of_machine_by_id():
    events_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": events_repository})
    client = app.test_client()

    event_register = Event(
        id_machine="machine-0005",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="register",
        payload={"brand": "balay", "model": "bal2525"},
    )
    event_diagnostic = Event(
        id_machine="machine-0005",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="diagnostic_in",
        payload={},
    )
    event_diagnostic89 = Event(
        id_machine="machine-00089",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="diagnostic_in",
        payload={},
    )

    events_repository.save_event(event_register)
    events_repository.save_event(event_diagnostic)
    events_repository.save_event(event_diagnostic89)

    response = client.get("/api/process/machine-0005")
    assert response.json == [
        {
            "id_machine": "machine-0005",
            "employee": "operario-007",
            "timestamp": "2022-05-08 10:06:00",
            "event": "register",
            "payload": {"brand": "balay", "model": "bal2525"},
        },
        {
            "id_machine": "machine-0005",
            "employee": "operario-007",
            "timestamp": "2022-05-08 10:06:00",
            "event": "diagnostic_in",
            "payload": {},
        },
    ]
