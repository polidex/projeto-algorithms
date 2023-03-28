def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    count = 0

    for logIn, logOut in permanence_period:
        if type(logIn) != int or type(logOut) != int:
            return None
        if logIn <= target_time <= logOut:
            count += 1

    return count

