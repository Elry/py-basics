# return the max num of tasks running at the exact same time
def busyServer(startArr, endArr):
    if not startArr or not endArr:
        return 0

    events = [(startA, 0) for startA in startArr] + [(endA, 1) for endA in endArr]
    events.sort()
    print(events)


    current_active = 0
    max_active = 0

    for _, event_type in events:
        if event_type == 0:
            current_active += 1
        else:
            current_active -= 1

        if current_active > max_active:
            max_active = current_active
    print(max_active)

A = [1, 2, 10, 20, 30]
B = [10, 15, 25, 40, 50]
busyServer(A, B);

