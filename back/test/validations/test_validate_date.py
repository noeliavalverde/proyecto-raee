from datetime import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_return_date_isoformat():
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
