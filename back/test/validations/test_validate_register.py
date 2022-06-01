from datetime import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app
from src.lib.utils import object_to_json


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

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
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

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
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


def test_should_validate_register_with_new_id():

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    existing_event = Event(
        id_machine="machine_1",
        employee="Jeff",
        timestamp=datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        event="register",
        payload={
            "brand": "Balay",
            "model": "Balay2365",
        },
    )

    event_repository.save_event(existing_event)

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        "event": "register",
        "payload": {
            "brand": "BAL5264",
            "model": "Balay",
        },
    }
    response = client.post("/api/process/register", json=event)
    assert response.status_code == 400


def test_should_get_none_id():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    existing_event = Event(
        id_machine="machine_1",
        employee="Jeff",
        timestamp=datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        event="register",
        payload={
            "brand": "Balay",
            "model": "Balay2365",
        },
    )
    event_repository.save_event(existing_event)
    response = client.get("/api/process/machine_2")

    assert response.status_code == 400
