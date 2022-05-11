import sqlite3
from src.webserver import create_app
from src.domain.info import InfoRepository
from src.domain.machines import MachineRepository
# from src.domain.diagnostic import DiagnosticRepository


database_path = "data/database.db"
print(database_path)

repositories = {
    "info": InfoRepository(database_path),
    "machine": MachineRepository(database_path),
    # "diagnostic": DiagnosticRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
