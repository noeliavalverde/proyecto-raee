def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.events import EventRepository, Event

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-seed-app"))

    event_repository = EventRepository(database_path)

    washer_machine_1 = Event(
        id_machine="washing_machine_1",
        employee="jeff",
        timestamp="2022-05-06",
        event="register",
        observations={"brand": "samsung", "model": "samsung_3"},
    )
    """
     washer_machine_2 = Event(
        id_machine="washing_machine_2",
        brand="Balay",
        model="Balay_2",
        register_date="2022-05-10",
        employee="jeff_2",
    )
    washer_machine_3 = Event(
        id_machine="washing_machine_3",
        brand="LG",
        model="LG_3",
        register_date="2022-05-20",
        employee="jeff_3",
    )
    washer_machine_4 = Event(
        id_machine="washing_machine_4",
        brand="BEKO",
        model="BEKO_4",
        register_date="2022-05-30",
        employee="jeff_4",
    )
    
    """

    event_repository.save_event(washer_machine_1)
    """
      event_repository.save_machines(washer_machine_2)
    event_repository.save_machines(washer_machine_3)
    event_repository.save_machines(washer_machine_4)
    
    """


if __name__ == "__main__":
    main()
