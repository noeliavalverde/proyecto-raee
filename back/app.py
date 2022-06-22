import sqlite3
from src.webserver import create_app
from src.domain.events import EventRepository


database_path = "data/database.db"
print(database_path)

repositories = {
    "event": EventRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
