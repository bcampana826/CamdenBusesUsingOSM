import random

import GraphCreation
import GraphMethods

world = GraphCreation.read_graph("worlds\\M1RouteLatLong.txt.txt")

#bus = {'route': [0, 2, 4, 6, 8, 6, 4, 2, 0, 1, 3, 5, 7, 5, 3, 1, 0], 'battery': 5}
# print(GraphMethods.validChargerLists(bus, world))

buses = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 33, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
    [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 88, 89, 90, 91]
]

run_data = open(("CamdenManual450-453.csv"), "w")

run_data.write(str(GraphMethods.smartChargers(buses,world,3)))