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


def test_should_get_all_machines_in_its_last_event():
    event_repository = EventRepository(temp_file())
    app = create_app(repositories={"event": event_repository})
    client = app.test_client()

    # Set up
    expected_list = {
        "machine-1": [
            {
                "id_machine": "machine-1",
                "employee": "operario-007",
                "timestamp": "2035-05-08 10:06:00",
                "event": "register",
                "payload": {"brand": "balay", "model": "bal2525"},
            },
            {
                "id_machine": "machine-1",
                "employee": "operario-007",
                "timestamp": "2035-05-10 10:06:00",
                "event": "diagnostic_in",
                "payload": {},
            },
        ],
        "machine-2": [
            {
                "id_machine": "machine-2",
                "employee": "operario-007",
                "timestamp": "2035-05-09 10:06:00",
                "event": "register",
                "payload": {"brand": "balay", "model": "bal6666"},
            },
            {
                "id_machine": "machine-2",
                "employee": "operario-007",
                "timestamp": "2035-05-11 10:06:00",
                "event": "diagnostic_in",
                "payload": {},
            },
            {
                "id_machine": "machine-2",
                "employee": "operario-007",
                "timestamp": "2035-05-12 10:06:00",
                "event": "diagnostic_out",
                "payload": {},
            },
        ],
    }
    # Function to test: get_all_events_classified_by_id_machine
    # It returns a dictionary with each ID Machine as key and the List of its Events as value
    classified_list = get_all_events_classified_by_id_machine(events_list)

    assert expected_list["machine-1"][0]["event"] == "register"

    assert expected_list["machine-1"][0] == {
        "id_machine": "machine-1",
        "employee": "operario-007",
        "timestamp": "2035-05-08 10:06:00",
        "event": "register",
        "payload": {"brand": "balay", "model": "bal2525"},
    }

    # if the key 'machine-1' is accessed, it returns the list of its events as a value
    assert expected_list["machine-1"] == [
        {
            "id_machine": "machine-1",
            "employee": "operario-007",
            "timestamp": "2035-05-08 10:06:00",
            "event": "register",
            "payload": {"brand": "balay", "model": "bal2525"},
        },
        {
            "id_machine": "machine-1",
            "employee": "operario-007",
            "timestamp": "2035-05-10 10:06:00",
            "event": "diagnostic_in",
            "payload": {},
        },
    ]
