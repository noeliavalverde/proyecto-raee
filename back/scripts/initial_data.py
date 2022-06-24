def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.events import EventRepository, Event
    from datetime import datetime, timedelta, date

    database_path = "data/database.db"

    event_repository = EventRepository(database_path)

    list_all_events = [
        Event(
            id_machine="washing_machine_1",
            employee="operario-008",
            timestamp="2022-06-10",
            event="register",
            payload={"brand": "SAMSUNG", "model": "SAMSUNG_3"},
        ),
        Event(
            id_machine="washing_machine_2",
            employee="operario-007",
            timestamp="2022-06-10",
            event="register",
            payload={"brand": "BALAY", "model": "BALAY_2"},
        ),
        Event(
            id_machine="washing_machine_3",
            employee="operario-011",
            timestamp="2022-06-10",
            event="register",
            payload={"brand": "LG", "model": "LG_3"},
        ),
        Event(
            id_machine="washing_machine_4",
            timestamp="2022-06-10",
            employee="operario-011",
            event="register",
            payload={"brand": "BEKO", "model": "BEKO_4"},
        ),
        Event(
            id_machine="washing_machine_5",
            timestamp="2022-06-10",
            employee="operario-008",
            event="register",
            payload={"brand": "SAMSUNG", "model": "SS48"},
        ),
        Event(
            id_machine="washing_machine_6",
            timestamp="2022-06-10",
            employee="operario-007",
            event="register",
            payload={"brand": "LG", "model": "LG_7"},
        ),
        Event(
            id_machine="washing_machine_7",
            timestamp="2022-06-10",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKO", "model": "BEKO_20"},
        ),
        Event(
            id_machine="washing_machine_8",
            timestamp="2022-06-10",
            employee="operario-011",
            event="register",
            payload={"brand": "BALAY", "model": "BALAY_B4"},
        ),
        Event(
            id_machine="washing_machine_9",
            timestamp="2022-06-10",
            employee="operario-007",
            event="register",
            payload={"brand": "BOSCH", "model": "BOSCH_B31"},
        ),
        Event(
            id_machine="washing_machine_10",
            timestamp="2022-06-10",
            employee="operario-008",
            event="register",
            payload={"brand": "BOSCH", "model": "BOSCH_B23"},
        ),
        Event(
            id_machine="washing_machine_11",
            timestamp="2022-06-11",
            employee="operario-008",
            event="register",
            payload={"brand": "BALAY", "model": "BALAY_2"},
        ),
        Event(
            id_machine="washing_machine_12",
            timestamp="2022-06-11",
            employee="operario-007",
            event="register",
            payload={"brand": "SAMSUNG", "model": "SAMSUNG_3"},
        ),
        Event(
            id_machine="washing_machine_13",
            timestamp="2022-06-11",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKO", "model": "BEKO_15"},
        ),
        Event(
            id_machine="washing_machine_14",
            timestamp="2022-06-11",
            employee="operario-007",
            event="register",
            payload={"brand": "BALAY", "model": "BALAY_33"},
        ),
        Event(
            id_machine="washing_machine_15",
            timestamp="2022-06-11",
            employee="operario-011",
            event="register",
            payload={"brand": "BOSCH", "model": "BOSCH_11"},
        ),
        Event(
            id_machine="washing_machine_16",
            timestamp="2022-06-11",
            employee="operario-007",
            event="register",
            payload={"brand": "BALAY", "model": "BALAY_B9"},
        ),
        Event(
            id_machine="washing_machine_17",
            timestamp="2022-06-11",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKO", "model": "BEKO_21"},
        ),
        Event(
            id_machine="washing_machine_18",
            timestamp="2022-06-11",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKO", "model": "BEKO_B12"},
        ),
        Event(
            id_machine="washing_machine_19",
            timestamp="2022-06-11",
            employee="operario-007",
            event="register",
            payload={"brand": "BEKO", "model": "BEKO_21"},
        ),
        Event(
            id_machine="washing_machine_20",
            timestamp="2022-06-11",
            employee="operario-011",
            event="register",
            payload={"brand": "LG", "model": "LG_7"},
        ),
        Event(
            id_machine="washing_machine_21",
            timestamp="2022-01-05",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKKO", "model": "B-JK"},
        ),
        Event(
            id_machine="washing_machine_22",
            timestamp="2022-01-05",
            employee="operario-007",
            event="register",
            payload={"brand": "LG", "model": "LG-58"},
        ),
        Event(
            id_machine="washing_machine_23",
            timestamp="2022-01-05",
            employee="operario-011",
            event="register",
            payload={"brand": "SAMSUNG", "model": "S23J"},
        ),
        Event(
            id_machine="washing_machine_24",
            timestamp="2022-02-05",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKKO", "model": "B-JK"},
        ),
        Event(
            id_machine="washing_machine_25",
            timestamp="2022-02-05",
            employee="operario-007",
            event="register",
            payload={"brand": "LG", "model": "LG-58"},
        ),
        Event(
            id_machine="washing_machine_26",
            timestamp="2022-02-05",
            employee="operario-011",
            event="register",
            payload={"brand": "SAMSUNG", "model": "S23J"},
        ),
        Event(
            id_machine="washing_machine_27",
            timestamp="2022-03-05",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKKO", "model": "B-JK"},
        ),
        Event(
            id_machine="washing_machine_28",
            timestamp="2022-03-05",
            employee="operario-007",
            event="register",
            payload={"brand": "LG", "model": "LG-58"},
        ),
        Event(
            id_machine="washing_machine_29",
            timestamp="2022-03-05",
            employee="operario-011",
            event="register",
            payload={"brand": "SAMSUNG", "model": "S23J"},
        ),
        Event(
            id_machine="washing_machine_30",
            timestamp="2022-04-05",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKKO", "model": "B-JK"},
        ),
        Event(
            id_machine="washing_machine_31",
            timestamp="2022-04-05",
            employee="operario-007",
            event="register",
            payload={"brand": "LG", "model": "LG-58"},
        ),
        Event(
            id_machine="washing_machine_32",
            timestamp="2022-04-05",
            employee="operario-011",
            event="register",
            payload={"brand": "SAMSUNG", "model": "S23J"},
        ),
        Event(
            id_machine="washing_machine_33",
            timestamp="2022-05-05",
            employee="operario-008",
            event="register",
            payload={"brand": "BEKKO", "model": "B-JK"},
        ),
        Event(
            id_machine="washing_machine_34",
            timestamp="2022-05-05",
            employee="operario-007",
            event="register",
            payload={"brand": "LG", "model": "LG-58"},
        ),
        Event(
            id_machine="washing_machine_35",
            timestamp="2022-05-05",
            employee="operario-011",
            event="register",
            payload={"brand": "SAMSUNG", "model": "S23J"},
        ),
    ]

    #################################################### SAVE REGISTERS:

    for event in list_all_events:
        event_repository.save_event(event)

    #################################################### SAVE DIAGNOSTIC:

    # diagnostic_in:
    diagnostic_in_list = list_all_events[:-3]

    for event in diagnostic_in_list:
        # we updated the key "timestamp" one more day, compared with event "register". And save it like a string
        event.timestamp = str(
            datetime.fromisoformat(event.timestamp) + timedelta(days=1)
        )
        event.event = "diagnostic_in"
        event.payload = {}
        event_repository.save_event(event)

    # diagnostic_out:
    diagnostic_out_list = diagnostic_in_list[:-3]

    for event in diagnostic_out_list:
        # we updated the key "timestamp" one more day, compared with event "diagnostic_in". And save it like a string
        event.timestamp = str(
            datetime.fromisoformat(event.timestamp) + timedelta(days=1)
        )
        event.event = "diagnostic_out"
        event.payload = {"next_event": "repair"}
        event_repository.save_event(event)

    #################################################### SAVE REPAIR:

    # repair_in:
    repair_in_list = diagnostic_out_list[:-3]

    for event in repair_in_list:
        # we updated the key "timestamp" one more day, compared with event "diagnostic_out". And save it like a string
        event.timestamp = str(
            datetime.fromisoformat(event.timestamp) + timedelta(days=1)
        )
        event.event = "repair_in"
        event.payload = {}
        event_repository.save_event(event)

    # repair_out:
    repair_out_list = repair_in_list[:-3]

    for event in repair_out_list:
        # we updated the key "timestamp" one more day, compared with event "repair_in". And save it like a string
        event.timestamp = str(
            datetime.fromisoformat(event.timestamp) + timedelta(days=1)
        )
        event.event = "repair_out"
        event.payload = {"next_event": "test"}
        event_repository.save_event(event)

    #################################################### SAVE TEST:

    # test_in:
    test_in_list = repair_out_list[:-3]

    for event in test_in_list:
        # we updated the key "timestamp" one more day, compared with event "repair_out". And save it like a string
        event.timestamp = str(
            datetime.fromisoformat(event.timestamp) + timedelta(days=1)
        )
        event.event = "test_in"
        event.payload = {}
        event_repository.save_event(event)

    # test_out:
    test_out_list = test_in_list[:-3]

    for event in test_out_list:
        # we updated the key "timestamp" one more day, compared with event "test_in". And save it like a string
        event.timestamp = str(
            datetime.fromisoformat(event.timestamp) + timedelta(days=1)
        )
        event.event = "test_out"
        event.payload = {"vibration": "ok", "flow": "ok"}
        event_repository.save_event(event)


if __name__ == "__main__":
    main()
