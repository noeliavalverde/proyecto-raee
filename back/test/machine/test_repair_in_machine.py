import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_repair_one_machine():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    diagnostic_in_event = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-05-08 10:06",
        event="diagnostic_out",
        payload={"brand": "balay", "model": "bal2525"},
    )

    event_repository.save_event(diagnostic_in_event)

    event = {
        "id_machine": "machine-1",
        "employee": "operario-007",
        "timestamp": "2022-05-17 10:00:00",
        "event": "repair_in",
        "payload": [],
    }

    response = client.post("/api/process/repair/enter", json=event)
    assert response.status_code == 200
