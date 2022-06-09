import datetime
from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.projections.supplyline import supply_line_current_state


def test_should_get_all_machines_in_diagnostic():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    events_list = [
        Event(
            id_machine="machine-1",
            employee="operario-007",
            timestamp="2035-05-08 10:06",
            event="register",
            payload={"brand": "balay", "model": "bal2525"},
        ),
        Event(
            id_machine="machine-2",
            employee="operario-007",
            timestamp="2035-05-08 10:06",
            event="register",
            payload={"brand": "balay", "model": "bal2525"},
        ),
        Event(
            id_machine="machine-1",
            employee="operario-007",
            timestamp="2035-05-08 10:06",
            event="diagnostic_in",
            payload={"brand": "balay", "model": "bal2525"},
        ),
        Event(
            id_machine="machine-2",
            employee="operario-007",
            timestamp="2035-05-08 10:06",
            event="diagnostic_in",
            payload={"brand": "balay", "model": "bal2525"},
        ),
        Event(
            id_machine="machine-1",
            employee="operario-007",
            timestamp="2035-05-08 10:06",
            event="diagnostic_out",
            payload={"brand": "balay", "model": "bal2525"},
        ),
        Event(
            id_machine="machine-2",
            employee="operario-007",
            timestamp="2035-05-08 10:06",
            event="diagnostic_out",
            payload={"brand": "balay", "model": "bal2525"},
        ),
        Event(
            id_machine="machine-1",
            employee="operario-007",
            timestamp="2035-05-08 10:06",
            event="repair_in",
            payload={"brand": "balay", "model": "bal2525"},
        ),
        Event(
            id_machine="machine-2",
            employee="operario-007",
            timestamp="2035-05-08 10:06",
            event="repair_in",
            payload={"brand": "balay", "model": "bal2525"},
        ),
    ]
    for event in events_list:
        event_repository.save_event(event)

    expected = supply_line_current_state(event_repository)

    assert expected["registered"] == 0
    assert expected["repair_in"] == 2
