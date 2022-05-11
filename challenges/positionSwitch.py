def positionSwitch(list):
    lastElement = len(list) - 1
    print('Initial list', list)
    list[0], list[lastElement] = list[lastElement], list[0]
    print('Switched list', list)

aList = [1, 2, 3, 4]
print
positionSwitch(aList)