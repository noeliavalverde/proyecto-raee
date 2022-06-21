# The name of this function has changed (previous one :def supply_line_current_state(repository))
def supply_line_state_collector(repository):
    """
    Function that counts every event has happened
    Example -
    :param repository: Event repository
    :return state: Diccionary with the name of events as key and the number of them as a value

    return data example:
        {
        "diagnostic_in": 1,
        "diagnostic_out": 1,
        "registered": 2,
        "repair_in": 0,
        "repair_out": 0,
        "test_in": 0,
        "test_out": 0
        }
    """

    events = repository.get_events()

    state = {
        "registered": 0,
        "diagnostic_in": 0,
        "diagnostic_out": 0,
        "repair_in": 0,
        "repair_out": 0,
        "test_in": 0,
        "test_out": 0,
    }
    for event in events:
        try:

            if event.event == "register":
                state["registered"] += 1

            elif event.event == "diagnostic_in":
                state["diagnostic_in"] += 1

            elif event.event == "diagnostic_out":
                state["diagnostic_out"] += 1

            elif event.event == "repair_in":
                state["repair_in"] += 1

            elif event.event == "repair_out":
                state["repair_out"] += 1

            elif event.event == "test_in":
                state["test_in"] += 1

            elif event.event == "test_out":
                state["test_out"] += 1
        except KeyError:
            print(f"Error! No existe {event.event}")

    print("state", str(state))

    return state


##################################################################


def get_all_events_classified_by_id_machine(event_list):
    """
    It returns a dictionary with each ID Machine as key and the List of its Events as value
    :param event_list: List of events
    :return all_events_by_id_machine: Dictionary that contains the name of ID machines as key and the value
                        is the events list of each washing machine

    return data example:
    {
        "machine-1": [
            {
                "id_machine": "machine-1",
                "employee": "operario-007",
                "timestamp": "2035-05-08 10:06:00",
                "event": "register",
                "payload": {"brand": "balay", "model": "bal2525"},
            }
        ],
        "machine-2": [
            {
                "id_machine": "machine-2",
                "employee": "operario-007",
                "timestamp": "2035-05-08 10:06:00",
                "event": "register",
                "payload": {"brand": "balay", "model": "bal6666"},
            },
            {
                "id_machine": "machine-2",
                "employee": "operario-007",
                "timestamp": "2035-05-09 10:16:00",
                "event": "diagnostic_in",
                "payload": {},
            },
        ],
    }
    """

    event_dictionary_list = []

    for event in event_list:
        # Mapping Event objects to dictionaries and storing them in a list
        event_dictionary_list.append(event.to_dict())

    all_events_by_id_machine = {}

    for event in event_dictionary_list:
        oneId = event["id_machine"]

        if oneId not in all_events_by_id_machine.keys():
            all_events_by_id_machine[oneId] = [event]

        else:
            all_events_by_id_machine[oneId].append(event)

    # devuelve diccionario {{'machine-1': [{event1}, {event2}], 'machine-2': [...]}
    return all_events_by_id_machine


#######


def get_all_events_by_id(id, repository):
    events = repository.get_events()

    event_list_of_one_machine = []
    for event in events:
        if event.id_machine == id:
            event_list_of_one_machine.append(event)
    return event_list_of_one_machine


#####################


def supply_line_current_state(id_machine_with_its_events_dict):
    """
    It returns all the info of the current event of each washing machine
    :param id_machine_with_its_events_dict: Diccionary returned from function "get_all_events_classified_by_id_machine"
                         It has each ID Machine as key and the Listof its Events as value

    :return current_status_supply_chain_list: List of current state of each machine

    return data example:
    List = [
        {
            "id_machine": "machine-1",
            "brand": "balay",
            "model": "bal2525",
            "employee": "operario-007",
            "event": "diagnostic_in",
            "payload": {"brand": "balay", "model": "bal2525"},
            "timestamp": "2035-05-10 10:06:00",
        },
        {
            "id_machine": "machine-2",
            "brand": "balay",
            "model": "bal6666",
            "employee": "operario-007",
            "event": "diagnostic_out",
            "payload": {"brand": "balay", "model": "bal6666"},
            "timestamp": "2035-05-12 10:06:00",
        },
    ]


    """

    register_data = []
    current_status_supply_chain_list = []
    contador = 0
    for one_id_machine in id_machine_with_its_events_dict:
        # Dictionary:
        # key "one_id_machine"
        # value (list of its events)   "events_list_of_this_machine"
        events_of_this_machine_list = id_machine_with_its_events_dict[one_id_machine]

        for event in events_of_this_machine_list:
            if event["event"] == "register":
                register_data.append(event)

            # Current event is the last one (supported by validations)
            current_event = events_of_this_machine_list[-1]

            if event["event"] == current_event["event"]:

                current_status_supply_chain_list.append(
                    {
                        "id_machine": current_event["id_machine"],
                        "brand": register_data[contador]["payload"]["brand"],
                        "model": register_data[contador]["payload"]["model"],
                        "employee": current_event["employee"],
                        "event": current_event["event"],
                        "payload": current_event["payload"],
                        "timestamp": current_event["timestamp"],
                    }
                )
                contador += 1

    return current_status_supply_chain_list


######
def get_number_of_machines_in_each_event(current_state_list):
    """
    :param current_state_list: List of dictionaries of the current info of each machine
    :return state: A dictionary with the number of machines that are currently in each event

    return data example:
    state = {
        "diagnostic_in": 1,
        "diagnostic_out": 1,
        "registered": 0,
        "repair_in": 0,
        "repair_out": 0,
        "test_in": 0,
        "test_out": 0
        }

    """
    state = {
        "registered": 0,
        "diagnostic_in": 0,
        "diagnostic_out": 0,
        "repair_in": 0,
        "repair_out": 0,
        "test_in": 0,
        "test_out": 0,
    }
    for event in current_state_list:
        try:

            if event["event"] == "register":
                state["registered"] += 1

            elif event["event"] == "diagnostic_in":
                state["diagnostic_in"] += 1

            elif event["event"] == "diagnostic_out":
                state["diagnostic_out"] += 1

            elif event["event"] == "repair_in":
                state["repair_in"] += 1

            elif event["event"] == "repair_out":
                state["repair_out"] += 1

            elif event["event"] == "test_in":
                state["test_in"] += 1

            elif event["event"] == "test_out":
                state["test_out"] += 1
        except KeyError:
            print(f"Error! No existe {event['event']}")

    return state
