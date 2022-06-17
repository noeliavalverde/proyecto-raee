import datetime
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
        event="diagnostic_in",  # current event - machine-1
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
        event="diagnostic_out",  # current event machine-2
        payload={},
    ),
]


def test_should_get_how_many_machines_are_in_each_event():

    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    for event in events_list:
        event_repository.save_event(event)

    all_events_classified_by_id_machine = get_all_events_classified_by_id_machine(
        events_list
    )
    current_event_classified_by_id_machine = supply_line_current_state(
        all_events_classified_by_id_machine
    )
    # Method to test:
    # It checks every machine's current event and and adds 1 in the event's counter
    number_of_machines_in_each_event = get_number_of_machines_in_each_event(
        current_event_classified_by_id_machine
    )

    assert number_of_machines_in_each_event["registered"] == 0
    assert number_of_machines_in_each_event["diagnostic_in"] == 1
    assert number_of_machines_in_each_event["diagnostic_out"] == 1
    assert number_of_machines_in_each_event["repair_in"] == 0
    assert number_of_machines_in_each_event["repair_out"] == 0
    assert number_of_machines_in_each_event["test_in"] == 0
    assert number_of_machines_in_each_event["test_out"] == 0
