import matplotlib.pyplot as plt
import numpy as np
"""

Given a TXT file in said format

**route number/name**
Stop Name0 - Miles from previous stop
Stop Name1 - Miles from previous stop
Stop Name2 - Miles from previous stop
so on



"""
def CreateWorld(listOfRoutes, worldName):
    world = open(str(worldName) + ".txt", "w")
    routes = open(str(worldName)+"-routes.txt","w")

    stopDict = dict()
    idCount = 0
    worldDict = dict()
    busRoutes = dict()

    for i in range(len(listOfRoutes)):
        routeFile = open(listOfRoutes[i], "r")
        lines = routeFile.readlines()

        busRoutes[lines[0].strip()] = []

        for j in range(1,len(lines)):
            lines[j] = lines[j].strip()

            data = lines[j].split(">>")

            data[0] = data[0].strip()
            data[1] = data[1].strip()

            if stopDict.get(data[0]) is None:
                stopDict[data[0]] = idCount
                idCount += 1

            if worldDict.get(stopDict.get(data[0])) is None:
                worldDict[stopDict.get(data[0])] = dict()

            if j != 1:
                worldDict.get(prevID)[stopDict.get(data[0])] = float(data[1])

            prevID = stopDict.get(data[0])

            busRoutes[lines[0].strip()].append(prevID)

    for z in worldDict.keys():
        tempString = str(z)+" C\t\t> "
        innerDict = worldDict.get(z)
        for y in innerDict.keys():
            tempString += "("+str(y)+","+str(innerDict.get(y))+"); "


        if len(tempString) > 15:
                tempString = tempString[0:len(tempString) - 2]
        world.write(tempString[0:len(tempString)]+"\n")

    for x in busRoutes.keys():
        routes.write(str(busRoutes.get(x))[1:len(str(busRoutes.get(x)))-1]+"\n")

    return worldDict, busRoutes

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
            smartRemoving(buses.get(b),chargerList,world,battery,inOrder)

    return chargerList

def smartRemoving(bus, chargerList, world, battery, inOrderList):

    #follow the bus path, remove from inOrderList
    energy = 0
    for i in range(len(bus)-1):

        if bus[i] in chargerList:
            energy = battery
            if bus[i] in inOrderList:
                inOrderList.remove(bus[i])

        if energy > 0:
            if bus[i] in inOrderList:
                inOrderList.remove(bus[i])

        energy -= world.get(bus[i]).get(bus[i+1])
        if energy < 0:
                energy = 0

world, buses = CreateWorld(["Manual450Route.txt","Manual453Route.txt"],"test")
print(buses)
print(world)

listToTry = [0.5,1.0,1.2,1.5,2.0,3.0,5.0,10.0]
data = []

for i in listToTry:
    data.append(len(smartChargers(buses,world,i)))

print(data)
plt.plot(listToTry, data)  # Plot some data on the axes.
plt.title("# of Chargers for Different Batteries")
plt.xlabel("Battery Distance in Miles")
plt.ylabel("Number of Chargers needed")
plt.show()

