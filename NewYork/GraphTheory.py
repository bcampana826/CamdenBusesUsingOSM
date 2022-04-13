import json


def smartChargers(buses, world, battery):
    chargerList = []

    all_chargers = []
    top_chargers = []

    for b in buses.keys():
        for p in buses.get(b):
            if p in top_chargers:
                all_chargers.append(p)
            else:
                top_chargers.append(p)
                all_chargers.append(p)

    inOrder = []

    while len(top_chargers) > 0:
        largest = -1
        count = -1
        for t in top_chargers:
            if all_chargers.count(t) > count:
                largest = t
                count = all_chargers.count(t)

        if largest != -1:
            inOrder.append(largest)
            top_chargers.remove(largest)

    while len(inOrder) > 0:
        charger = inOrder.pop(0)
        chargerList.append(charger)
        for b in buses.keys():
            smartRemoving(buses.get(b), chargerList, world, battery, inOrder)

    return chargerList


def smartRemoving(bus, chargerList, world, battery, inOrderList):
    # follow the bus path, remove from inOrderList
    battery = battery*1609.34


    energy = 0
    for i in range(len(bus) - 1):

        if bus[i] in chargerList:
            energy = battery
            if bus[i] in inOrderList:
                inOrderList.remove(bus[i])

        if energy > 0:
            if bus[i] in inOrderList:
                inOrderList.remove(bus[i])

        energy -= int( world[str(bus[i+1])].get('prev_dist') )
        if energy < 0:
            energy = 0

with open("worlds/StartingWorld2.json") as json_file:
    world = json.load(json_file)
print(smartChargers(world["routes"],world["stops"],5))