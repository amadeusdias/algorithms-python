def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    if not all(isinstance(intervalo,tuple)for intervalo in permanence_period):
        return None
    for index, tup in enumerate(permanence_period):
        if isinstance(tup[0],int) == False:
            return None
        if isinstance(tup[1],int) == False: 
            return None
        if tup[0] <= target_time <= tup[1]:
             counter += 1
        return counter
    
