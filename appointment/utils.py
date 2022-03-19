from datetime import datetime, time, timedelta

def date_range(start, end):
    start, end = datetime.strptime(start, '%Y-%m-%d'), datetime.strptime(end, '%Y-%m-%d')
    delta = end - start
    if delta.days < 0:raise ValueError('end must be greater than start')
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days

def combine_dt_time(dt, t_time):
    return datetime.combine(dt,t_time)

def is_overlapped(range1, range2):
    if max(range1[0], range2[0]) < min(range1[1], range2[1]):
        return True
    else:
        return False

def get_free_epochs(hours, occupied_epochs, duration=timedelta(hours=1)):
    available = []
    slots = sorted([(hours[0], hours[0])] + occupied_epochs + [(hours[1], hours[1])])
    for start, end in ( (slots[i][1], slots[i+1][0]) for i in range(len(slots)-1) ):
        assert start <= end
        while start + duration <= end:
            free_slot = {}
            done = start + duration
            free_slot["start"] = start.strftime("%H:%M:%S")
            free_slot["end"] = done.strftime("%H:%M:%S")
            available.append(free_slot)
            start = start+duration
    return available