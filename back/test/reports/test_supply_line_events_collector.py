from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.projections.supplyline import *


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
        timestamp="2035-05-09 10:06",
        event="register",
        payload={"brand": "balay", "model": "bal6666"},
    ),
    Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2035-05-10 10:06",
        event="diagnostic_in",
        payload={},
    ),
    Event(
        id_machine="machine-2",
        employee="operario-007",
        timestamp="2035-05-11 10:06",
        event="diagnostic_in",
        payload={},
    ),
    Event(
        id_machine="machine-2",
        employee="operario-007",
        timestamp="2035-05-12 10:06",
        event="diagnostic_out",
        payload={},
    ),
    Event(
        id_machine="machine-1",
        employee="operario-007",
        timestamp="2035-05-13 10:06",
        event="diagnostic_out",
        payload={},
    ),
    Event(
        id_machine="machine-2",
        employee="operario-007",
        timestamp="2035-05-14 10:06",
        event="repair_in",
        payload={},
    ),
]


def test_should_get_all_events_of_machines_collector():

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    for event in events_list:
        event_repository.save_event(event)

    expected = supply_line_state_collector(event_repository)

    assert expected["registered"] == 2
    assert expected["diagnostic_in"] == 2
    assert expected["diagnostic_out"] == 2
    assert expected["repair_in"] == 1
    assert expected["repair_out"] == 0
    assert expected["test_in"] == 0
    assert expected["test_out"] == 0
