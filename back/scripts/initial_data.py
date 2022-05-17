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
        employee="jeff",
        timestamp="2022-05-06",
        event="register",
        payload={"brand": "samsung", "model": "samsung_3"},
    )

    washer_machine_2 = Event(
        id_machine="washing_machine_2",
        employee="jeff_2",
        timestamp="2022-05-10",
        event="register",
        payload={"brand": "Balay", "model": "Balay_2"},
    )
    washer_machine_3 = Event(
        id_machine="washing_machine_3",
        employee="jeff",
        timestamp="2022-05-20",
        event="register",
        payload={"brand": "LG", "model": "LG_3"},
    )

    washer_machine_4 = Event(
        id_machine="washing_machine_4",
        timestamp="2022-05-30",
        employee="jeff_2",
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
        employee="jeff",
        timestamp="2022-05-07",
        event="diagnostic_in",
        payload={},
    )
    event_repository.save_event(washer_machine_diagnostic_in)

    washer_machine_diagnostic_out = Event(
        id_machine="washing_machine_1",
        employee="jeff",
        timestamp="2022-05-08",
        event="diagnostic_out",
        payload={"next_event": "repair"},
    )
    event_repository.save_event(washer_machine_diagnostic_out)

    # REPAIR
    washer_machine_repair_in = Event(
        id_machine="washing_machine_1",
        employee="jeff",
        timestamp="2022-05-07",
        event="repair_in",
        payload={},
    )
    event_repository.save_event(washer_machine_repair_in)


if __name__ == "__main__":
    main()
