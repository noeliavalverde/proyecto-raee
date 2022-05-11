from src.domain.machines import MachineRepository
from src.lib.utils import temp_file
from src.webserver import create_app

def test_should_register_one_machine():
    machine_repository = MachineRepository(temp_file())
    app = create_app(repositories={"machine": machine_repository})
    client = app.test_client()


    washer_machine= {
        "id_machine" : "washing_machine_1",
        "brand": "samsung",
        "model": "samsung_3",
        "register_date": "2022-05-06",
        "employee": "jeff"
    }

    response = client.post("/api/process/register", json= washer_machine)
    assert response.status_code == 200