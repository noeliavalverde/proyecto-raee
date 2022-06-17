from atexit import register
from datetime import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_not_allow_not_isoformat_date():
    registered_machine = EventRepository(temp_file())
    app = create_app(repositories={"event": registered_machine})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": "202l-05-05",
        "event": "register",
        "payload": {
            "brand": "balay",
            "model": "bal2525",
        },
    }
    response = client.post("/api/process/register", json=event)
    assert response.status_code == 400


def test_should_not_allow_a_previous_date():

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    register_event = Event(
        id_machine="machine_1",
        employee="Jeff",
        timestamp="2022-05-05 19:25:00",
        event="diagnostic_in",
        payload={
            "brand": "balay",
            "model": "bal2525",
        },
    )

    event_repository.save_event(register_event)

    diagnostic_event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": "2022-05-05 17:25:00",
        "event": "diagnostic_out",
        "payload": {
            "brand": "balay",
            "model": "bal2525",
        },
    }
    response = client.post("/api/process/diagnostic/exit", json=diagnostic_event)
    assert response.status_code == 400
