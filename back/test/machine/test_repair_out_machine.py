import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_repair_out_one_machine():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    repair_in_event = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-06-15 09:33:00",
        event="repair_in",
        payload=[],
    )

    event_repository.save_event(repair_in_event)

    repair_out_event = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-06-20 09:33:00",
        "event": "repair_out",
        "payload": [],
    }

    response = client.post("/api/process/repair/exit", json=repair_out_event)
    assert response.status_code == 200


def test_should_not_save_one_machine_with_incorrect_event_repair_out_name():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    repair_in_event = Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2022-06-15 09:33:00",
        event="repair_in",
        payload=[],
    )

    event_repository.save_event(repair_in_event)

    repair_out_event = {
        "id_machine": "machine-1",
        "employee": "Jeff",
        "timestamp": "2022-06-20 09:33:00",
        "event": "REPAIR_OUT",
        "payload": [],
    }

    response = client.post("/api/process/repair/exit", json=repair_out_event)
    assert response.status_code == 400
