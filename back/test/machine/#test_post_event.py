from domain.events import MachineRepository
from src.lib.utils import temp_file
from src.webserver import create_app

def test_should_post_event():
    machine_repository = MachineRepository(temp_file())
    app = create_app(repositories={"machine": machine_repository})
    client = app.test_client()


    event= {
        "id_machine" : "washing_machine_1",
        "employee": "samsung",
        "timestamp": "samsung_3",
        "observations": "2022-05-06"
    }

    response = client.post("/api/process/diagnostic/enter", json= event)
    assert response.status_code == 200