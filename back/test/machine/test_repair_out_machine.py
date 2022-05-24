import datetime
from src.domain.events import EventRepository
from src.lib.utils import temp_file
from src.webserver import create_app


def test_should_repair_out_one_machine():
    registered_machine = EventRepository(temp_file())
    app = create_app(repositories={"event": registered_machine})
    client = app.test_client()

    event = {
        "id_machine": "machine_1",
        "employee": "Jeff",
        "timestamp": datetime.datetime.now().isoformat(),
        "event": "repair_out",
        "payload": [
            {"next_event": "test"},
            {
                "procedures": [
                    {
                        "title": "cambio de correa",
                        "steps": [
                            {
                                "step": "retirar tornillos de la pared trasera",
                                "steps": [
                                    {
                                        "step": "retirar tornillos de la pared trasera",
                                        "image": "",
                                        "is_completed": 1,
                                    },
                                    {
                                        "step": "retirar la pared trasera",
                                        "image": "",
                                        "is_completed": 1,
                                    },
                                    {
                                        "step": "retirar la correa Poly-V",
                                        "image": "",
                                        "is_completed": 1,
                                    },
                                ],
                                "is_completed": 1,
                            },
                            {
                                "step": "retirar la pared trasera",
                                "image": "",
                                "is_completed": 1,
                            },
                            {
                                "step": "retirar la correa Poly-V",
                                "image": "",
                                "is_completed": 1,
                            },
                        ],
                        "docs": [],
                    },
                ],
            },
        ],
    }

    response = client.post("/api/process/repair/exit", json=event)
    assert response.status_code == 200
