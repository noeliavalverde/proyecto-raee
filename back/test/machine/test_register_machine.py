from datetime import datetime
from src.domain.events import EventRepository
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_register_one_machine():
    registered_machine = EventRepository(temp_file())
    app = create_app(repositories={"event": registered_machine})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": "2022-08-05 22:36:00",
        "event": "register",
        "payload": {
            "brand": "samsung",
            "model": "samsung_3",
        },
    }

    response = client.post("/api/process/register", json=event)
    assert response.status_code == 200
