def study_schedule(permanence_period, target_time):
    counter = 0
    if not target_time:
        return None
    for index, tup in enumerate(permanence_period):
        if not isinstance(tup[0], int) or not isinstance(tup[1], int):
            return None
        if tup[0] <= target_time <= tup[1]:
            counter += 1
        return counter
