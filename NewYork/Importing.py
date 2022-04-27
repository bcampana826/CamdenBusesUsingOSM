from os import walk

import matplotlib.pyplot as plt
import numpy as np
import json

"""

Given a TXT file in said format

**route number/name**
Stop Name0 >> Lat >> Long
Stop Name1 >> Lat >> Long
Stop Name2 >> Lat >> Long
so on
"""


def CreateWorld(listOfRoutes, worldName):
    worldDictionary = dict()

    stopDict = dict()
    nameToIdDict = dict()
    busRoutes = dict()
    idCount = 0

    for i in range(len(listOfRoutes)):
        routeFile = open(listOfRoutes[i], "r")
        lines = routeFile.readlines()

        busRoutes[lines[0].strip()] = list()

        tempDict = dict()
        for j in range(1, len(lines)):
            lines[j] = lines[j].strip()

            data = lines[j].split(">>")

            data[0] = data[0].strip()
            data[1] = data[1].strip()
            data[2] = data[2].strip()
            data[3] = data[3].strip()

            tempDict = dict()
            tempDict['name'] = data[0]
            tempDict['lat'] = data[1]
            tempDict['long'] = data[2]
            tempDict['prev_dist'] = data[3]

            if nameToIdDict.get(data[0]) is None:
                nameToIdDict[data[0]] = idCount
                idCount += 1

            if stopDict.get(data[0]) is None:
                stopDict[nameToIdDict.get(data[0])] = tempDict

            busRoutes.get(lines[0].strip()).append(nameToIdDict.get(data[0]))

    worldDictionary['stops'] = stopDict
    worldDictionary['name_to_id'] = nameToIdDict
    worldDictionary['routes'] = busRoutes
    worldDictionary['filename'] = worldName+".json"

    with open("Worlds/"+worldDictionary['filename'], "w") as writing_file:
        json_dumps_str = json.dumps(worldDictionary, indent=4)
        print(json_dumps_str, file=writing_file)

    return worldDictionary


f = []
for (dirpath,dirnames,filenames) in walk("LatLong/"):
    count = 0
    for j in filenames:
        f.append("LatLong/"+j)
        count+=1
        if count > 2:
            break


world = CreateWorld(f, "gruby-test")
print(world)