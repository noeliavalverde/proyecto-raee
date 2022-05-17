import datetime
from src.domain.events import EventRepository
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_diagnostic_out_one_machine():
    registered_machine = EventRepository(temp_file())
    app = create_app(repositories={"event": registered_machine})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": datetime.datetime.now().isoformat(),
        "event": "diagnostic_in",
        "payload": {"next_event": "repair"},
    }

    response = client.post("/api/process/diagnostic/exit", json=event)
    assert response.status_code == 200