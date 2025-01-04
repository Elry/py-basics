def position_switch(list):
    last_element = len(list) - 1
    print('Initial list', list)
    list[0], list[last_element] = list[last_element], list[0]
    print('Switched list', list)

aList = [1, 2, 3, 4]
print
position_switch(aList)