def supply_line_current_state(repository):
    events = repository.get_events()
    state = {"registered": 0, "repair_in": 0}
    for event in events:
        if event.event == "repair_in":
            state["repair_in"] += 1
    return state
