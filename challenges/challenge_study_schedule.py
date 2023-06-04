def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for index, tup in enumerate(permanence_period):
        if isinstance(tup[0], int) is False or if isinstance(tup[1], int) is False:
            return None
        if tup[0] <= target_time <= tup[1]:
            counter += 1
        return counter
