import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_diagnostic_one_machine():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    register_event = Event(
        id_machine="machine_1",
        employee="Jeff",
        timestamp="2022-06-15 09:33",
        event="register",
        payload={
            "brand": "Balay",
            "model": "Balay2365",
        },
    )

    event_repository.save_event(register_event)

    diagnostic_event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": "2022-06-15 09:34",
        "event": "diagnostic_in",
        "payload": [
            {"docs": "Aqui va el enlace de un vide de como chekear una lavadora"}
        ],
    }

    response = client.post("/api/process/diagnostic/enter", json=diagnostic_event)
    assert response.status_code == 200
