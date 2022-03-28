import collections


def greedyChargingArrays(buses, city, battery):

    all_chargers = []
    top_chargers = []

    for b in range(len(buses)):
        for p in buses[b]:
            if p in top_chargers:
                all_chargers.append(p)
            else:
                top_chargers.append(p)
                all_chargers.append(p)

    inOrder = []

    while len(top_chargers)>0:
        largest = -1
        count = -1
        for t in top_chargers:
            if all_chargers.count(t) > count:
                largest = t
                count = all_chargers.count(t)

        if largest != -1:
            inOrder.append(largest)
            top_chargers.remove(largest)



    testing = True
    count = 0
    while testing:
        mid_boolean = True
        count += 1
        chargers = []
        for x in range(count):
            chargers.append(inOrder[x])

        for b in range(len(buses)):
            route = {'route': buses[b], 'battery':battery}
            if mid_boolean and len(validChargerLists(route,city,chargers)) > 0:
                #good
                mid_boolean = True
            else:
                mid_boolean = False

        if mid_boolean:
            return chargers


def validChargerLists(bus, city, chargers):
    """
    :param bus: Buses route over city nodes
    :param city: Graph of nodes
    :return: List of different charging station options.
    """
    valid_answers = []
    chargers_on_route = intersection(bus, chargers, True)

    # We are going to iterate over each charger being on and off
    # doing this binary-ily? so one binary number per charger
    for i in range(2 ** len(chargers_on_route)):

        # this is what picks what one were doing right now?
        # yeah i confirmed this - for each run it converts the i to a binary number for chargers
        temp = "{0:b}".format(i)
        charger_to_test = []

        for c in range(len(temp)):
            if temp[len(temp) - 1 - c:len(temp) - c] == "1":
                charger_to_test.append(int(chargers_on_route[c]))

        # Testing this number
        test_energy = bus['battery']
        success = True

        for p in range(len(bus['route']) - 1):

            # subtract the energy cost from starting location to next spot
            test_energy -= float(city[bus['route'][p]].get_edge(float(bus['route'][p + 1])))

            if test_energy < 0:
                # bus ran out of energy before reaching recharge
                # Fail
                success = False
                break

            if bus['route'][p + 1] in charger_to_test:
                # recharge
                test_energy = bus['battery']

        if success:
            valid_answers.append(charger_to_test)

    return valid_answers

def smartChargers(buses, world, battery):

    chargerList = []


    all_chargers = []
    top_chargers = []

    for b in range(len(buses)):
        for p in buses[b]:
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
        for b in buses:
            smartRemoving(b,chargerList,world,battery,inOrder)

    return chargerList

def smartRemoving(bus, chargerList, world, battery, inOrderList):

    #follow the bus path, remove from inOrderList
    energy = 0
    for i in range(len(bus)-1):

        if i != 0:
            energy -= world[world.index(bus[i])].get_edge(i+1)
            if energy < 0:
                energy = 0

        if bus[i] in chargerList:
            energy = battery
            if bus[i] in inOrderList:
                inOrderList.remove(bus[i])

        if energy > 0:
            if bus[i] in inOrderList:
                inOrderList.remove(bus[i])










def intersection(lst1, city):
    nodes = []
    for i in range(len(city)):
        if city[i].charger:
            nodes.append(city[i].num)

    lst3 = [value for value in lst1['route'] if value in nodes]
    return lst3

def intersection(lst1, lst2, boolean):

    lst3 = [value for value in lst1['route'] if value in lst2]
    return lst3

