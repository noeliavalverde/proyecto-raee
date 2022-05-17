import sqlite3
import json

# import datetime
from datetime import datetime, date


class Event:
    def __init__(self, id_machine, employee, timestamp, event, payload):
        self.id_machine = id_machine
        self.employee = employee
        self.timestamp = datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        self.event = event
        self.payload = payload

    def to_dict(self):
        return {
            "id_machine": self.id_machine,
            "employee": self.employee,
            "timestamp": self.timestamp,
            "event": self.event,
            "payload": self.payload,
        }


class EventRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql_events = """
            create table if not exists events (
                id_machine varchar,
                employee varchar,
                timestamp timestamp,
                event varchar,
                payload varchar
            )"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql_events)
        conn.commit()

    date = datetime.today()

    def save_event(self, event):
        sql = """INSERT into events (id_machine, employee, timestamp, event, payload) values (
            :id_machine, :employee, :timestamp, :event, :payload
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id_machine": event.id_machine,
                "employee": event.employee,
                "timestamp": datetime.fromisoformat(event.timestamp),
                "event": event.event,
                "payload": json.dumps(event.payload),
            },
        )
        conn.commit()
