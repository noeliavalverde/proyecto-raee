def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.events import EventRepository, Event

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-seed-app"))

    event_repository = EventRepository(database_path)

    # REGISTERS

    washer_machine_1 = Event(
        id_machine="washing_machine_1",
        employee="operario-008",
        timestamp="2022-05-06",
        event="register",
        payload={"brand": "samsung", "model": "samsung_3"},
    )

    washer_machine_2 = Event(
        id_machine="washing_machine_2",
        employee="operario-007",
        timestamp="2022-05-10",
        event="register",
        payload={"brand": "Balay", "model": "Balay_2"},
    )
    washer_machine_3 = Event(
        id_machine="washing_machine_3",
        employee="operario-011",
        timestamp="2022-05-20",
        event="register",
        payload={"brand": "LG", "model": "LG_3"},
    )

    washer_machine_4 = Event(
        id_machine="washing_machine_4",
        timestamp="2022-05-30",
        employee="operario-008",
        event="register",
        payload={"brand": "BEKO", "model": "BEKO_4"},
    )

    event_repository.save_event(washer_machine_1)
    event_repository.save_event(washer_machine_2)
    event_repository.save_event(washer_machine_3)
    event_repository.save_event(washer_machine_4)

    # DIAGNOSTIC:

    washer_machine_diagnostic_in = Event(
        id_machine="washing_machine_1",
        employee="operario-008",
        timestamp="2022-05-07",
        event="diagnostic_in",
        payload={},
    )
    event_repository.save_event(washer_machine_diagnostic_in)

    washer_machine_diagnostic_out = Event(
        id_machine="washing_machine_1",
        employee="operario-008",
        timestamp="2022-05-08",
        event="diagnostic_out",
        payload={"next_event": "repair"},
    )
    event_repository.save_event(washer_machine_diagnostic_out)

    # REPAIR
    washer_machine_repair_in = Event(
        id_machine="washing_machine_1",
        employee="operario-011",
        timestamp="2022-05-07",
        event="repair_in",
        payload={},
    )
    event_repository.save_event(washer_machine_repair_in)

    washer_machine_repair_out = Event(
        id_machine="washing_machine_7",
        employee="operario-07",
        timestamp="2022-05-11",
        event="repair_out",
        payload={"next_event": "test"},
    )
    event_repository.save_event(washer_machine_repair_out)

    washer_machine_repair_out = Event(
        id_machine="washing_machine_8",
        employee="operario-09",
        timestamp="2022-05-11",
        event="repair_out",
        payload={"next_event": "test"},
    )
    event_repository.save_event(washer_machine_repair_out)
    washer_machine_repair_out = Event(
        id_machine="washing_machine_9",
        employee="operario-08",
        timestamp="2022-05-12",
        event="repair_out",
        payload={"next_event": "test"},
    )
    event_repository.save_event(washer_machine_repair_out)
    washer_machine_repair_out = Event(
        id_machine="washing_machine_10",
        employee="operario-09",
        timestamp="2022-05-12",
        event="repair_out",
        payload={"next_event": "test"},
    )
    event_repository.save_event(washer_machine_repair_out)
    washer_machine_repair_out = Event(
        id_machine="washing_machine_11",
        employee="operario-08",
        timestamp="2022-05-13",
        event="repair_out",
        payload={"next_event": "test"},
    )
    event_repository.save_event(washer_machine_repair_out)
    washer_machine_repair_out = Event(
        id_machine="washing_machine_12",
        employee="operario-08",
        timestamp="2022-05-14",
        event="repair_out",
        payload={"next_event": "test"},
    )
    event_repository.save_event(washer_machine_repair_out)

    # TEST
    washer_machine_test_in = Event(
        id_machine="washing_machine_1",
        employee="operario-007",
        timestamp="2022-05-15",
        event="test_in",
        payload={},
    )
    event_repository.save_event(washer_machine_test_in)

    washer_machine_test_out = Event(
        id_machine="washing_machine_1",
        employee="operario-007",
        timestamp="2022-05-10",
        event="test_out",
        payload={"vibration": "ok", "flow": "ok"},
    )
    event_repository.save_event(washer_machine_test_out)


if __name__ == "__main__":
    main()
