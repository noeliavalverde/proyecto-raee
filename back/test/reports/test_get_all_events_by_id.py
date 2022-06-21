from src.domain.events import EventRepository, Event
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.projections.supplyline import *
from src.lib import utils

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
]


def test_should_get_all_events_by_id():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    # Set up

    # Storaging some events in repository
    for event in events_list:
        event_repository.save_event(event)

    # Function to test, it should return all the events of one machine
    all_events_of_a_machine = get_all_events_by_id("machine-1", event_repository)

    assert len(all_events_of_a_machine) == 2

    assert all_events_of_a_machine[0].id_machine == "machine-1"
    assert all_events_of_a_machine[0].employee == "operario-007"
    assert all_events_of_a_machine[0].event == "register"
    assert all_events_of_a_machine[0].timestamp == "2035-05-08 10:06:00"
    assert all_events_of_a_machine[0].payload["brand"] == "balay"
    assert all_events_of_a_machine[0].payload["model"] == "bal2525"

    assert all_events_of_a_machine[1].id_machine == "machine-1"
    assert all_events_of_a_machine[1].employee == "operario-007"
    assert all_events_of_a_machine[1].timestamp == "2035-05-10 10:06:00"
    assert all_events_of_a_machine[1].event == "diagnostic_in"
    assert all_events_of_a_machine[1].payload == {}
