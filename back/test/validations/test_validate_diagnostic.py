from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_already_exist_id_machine_at_diagnostic_event():

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    existing_event = Event(
        id_machine="machine_1",
        employee="Jeff",
        timestamp="2022-06-15 09:33",
        event="register",
        payload={
            "brand": "Balay",
            "model": "Balay2365",
        },
    )

    event_repository.save_event(existing_event)

    event = {
        "id_machine": "machine_2",
        "employee": "Jeff",
        "timestamp": "2022-06-15 09:33",
        "event": "diagnostic",
        "payload": {
            "brand": "BAL5264",
            "model": "Balay",
        },
    }
    response = client.post("/api/process/diagnostic/enter", json=event)
    assert response.status_code == 400
