import datetime
from src.domain.events import EventRepository
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_test_one_machine():
    registered_machine = EventRepository(temp_file())
    app = create_app(repositories={"event": registered_machine})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": datetime.datetime.now().isoformat(),
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
