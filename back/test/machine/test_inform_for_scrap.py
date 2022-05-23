from datetime import datetime
from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.events import EventRepository, Event


def test_should_get_info_for_scrap_inform():

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    print(date)
    washing_machine = Event(
        id_machine="machine_1",
        employee="Jeff",
        timestamp="2022-05-19 10:14:33",
        event="register",
        payload={"brand": "samsung", "model": "samsung_3"},
    )
    event_repository.save_event(washing_machine)

    response_washing_machine = client.get("/api/process/scrap_inform")

    assert response_washing_machine.json == [
        {
            "id_machine": "machine_1",
            "employee": "Jeff",
            "timestamp": "2022-05-19 10:14:33",
            "event": "register",
            "payload": {"brand": "samsung", "model": "samsung_3"},
        }
    ]
