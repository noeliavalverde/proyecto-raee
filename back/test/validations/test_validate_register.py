from datetime import datetime
from src.domain.events import EventRepository
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_validate_json_contains_brand_machine():

    registered_machine = EventRepository(temp_file())
    app = create_app(repositories={"event": registered_machine})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        "event": "register",
        "payload": {
            "brand": "",
            "model": "jhvjh",
        },
    }

    response = client.post("/api/process/register", json=event)
    assert response.status_code == 400


def test_should_validate_json_contains_model_machine():

    registered_machine = EventRepository(temp_file())
    app = create_app(repositories={"event": registered_machine})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        "event": "register",
        "payload": {
            "brand": "Balay",
            "model": "",
        },
    }

    response = client.post("/api/process/register", json=event)
    assert response.status_code == 400


def test_should_validate_json_not_contains_space_at_model_or_brand():

    registered_machine = EventRepository(temp_file())
    app = create_app(repositories={"event": registered_machine})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        "event": "register",
        "payload": {
            "brand": " ",
            "model": "Balay",
        },
    }

    response = client.post("/api/process/register", json=event)
    assert response.status_code == 400
