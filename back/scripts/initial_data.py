def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.regists import RegistsRepository, Regists

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-seed-app"))

    regists_repository = RegistsRepository(database_path)

    washer_machine_1= Regists(
        id_machine= "washing_machine_1",
        brand= "samsung",
        model= "samsung_3",
        register_date= "2022-05-06",
        employee= "jeff"
        )
    washer_machine_2= Regists(
        id_machine= "washing_machine_2",
        brand= "Balay",
        model= "Balay_2",
        register_date= "2022-05-10",
        employee= "jeff_2"
        )
    washer_machine_3= Regists(
        id_machine= "washing_machine_3",
        brand= "LG",
        model= "LG_3",
        register_date= "2022-05-20",
        employee= "jeff_3"
        )
    washer_machine_4= Regists(
        id_machine= "washing_machine_4",
        brand= "BEKO",
        model= "BEKO_4",
        register_date= "2022-05-30",
        employee= "jeff_4"
        )
    regists_repository.save(washer_machine_1)
    regists_repository.save(washer_machine_2)
    regists_repository.save(washer_machine_3)
    regists_repository.save(washer_machine_4)



if __name__ == '__main__':
    main()
