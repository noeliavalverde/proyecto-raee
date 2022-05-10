import sqlite3

class Regists:
    def __init__(self, id_machine, brand, model, register_date, employee):
        self.id_machine= id_machine
        self.brand= brand
        self.model= model
        self.register_date= register_date
        self.employee= employee

    def to_dict(self):
        return {
           "id_machine": self.id_machine,
            "brand": self.brand,
            "model": self.model,
            "register_date": self.register_date,
            "employee": self.employee
        }

class RegistsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists the_regists (
               id_machine varchar,
                brand varchar,
                model varchar,
                register_date varchar,
                employee varchar 
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_services_by_category(self):
        sql = """select * from the_regists"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        washers = []
        for item in data:
            washer_machine = Regists(
                id= item["id_machine"],
                cat_id= item["brand"],
                user_name= item["model"],
                text= item["register_date"],
                intro= item["employee"]
            )
            washers.append(washer_machine)
        return washers

    def get_by_id(self, id_machine):
        sql = """SELECT * FROM the_regists WHERE id_machine= :id_machine"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_machine": id_machine})
        data = cursor.fetchall()
        washers = []
        for item in data:
            washer_machine = Regists(
                id= item["id_machine"],
                cat_id= item["brand"],
                user_name= item["model"],
                text= item["register_date"],
                intro= item["employee"]
            )
            washers.append(washer_machine)
        return washers

    def save(self, washer):
        sql = """INSERT into the_regists (id_machine, brand, model, register_date, employee) values (
            :id_machine, :brand, :model, :register_date, :employee
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            washer.to_dict(),
        )
        conn.commit()