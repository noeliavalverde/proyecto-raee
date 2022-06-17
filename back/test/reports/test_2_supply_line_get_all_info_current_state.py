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
]


def test_should_get_machines_in_their_current_event_and_its_info():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    # Set up
    expected_list = [
        {
            "id_machine": "machine-1",
            "brand": "balay",
            "model": "bal2525",
            "employee": "operario-007",
            "event": "diagnostic_in",
            "payload": {"brand": "balay", "model": "bal2525"},
            "timestamp": "2035-05-10 10:06:00",
        },
        {
            "id_machine": "machine-2",
            "brand": "balay",
            "model": "bal6666",
            "employee": "operario-007",
            "event": "diagnostic_out",
            "payload": {"brand": "balay", "model": "bal6666"},
            "timestamp": "2035-05-12 10:06:00",
        },
    ]

    id_machine_with_its_events_dict = get_all_events_classified_by_id_machine(
        events_list
    )
    # Function to test, it should return all the info of the current events of each washing machine
    # and also, its brand and model data.
    all_current_info_list = supply_line_current_state(id_machine_with_its_events_dict)

    # assert all_current_info_list == expected_list

    assert all_current_info_list[0]["id_machine"] == "machine-1"
    assert all_current_info_list[0]["brand"] == "balay"
    assert all_current_info_list[0]["model"] == "bal2525"
    assert all_current_info_list[0]["employee"] == "operario-007"
    assert all_current_info_list[0]["event"] == "diagnostic_in"

    assert all_current_info_list[1]["id_machine"] == "machine-2"
    assert all_current_info_list[1]["brand"] == "balay"
    assert all_current_info_list[1]["model"] == "bal6666"
    assert all_current_info_list[1]["employee"] == "operario-007"
    assert all_current_info_list[1]["event"] == "diagnostic_out"
