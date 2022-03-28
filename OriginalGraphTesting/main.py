import random

import GraphCreation
import GraphMethods

world = GraphCreation.read_graph("worlds\kindaCityWorld")

bus = {'route': [0, 2, 4, 6, 8, 6, 4, 2, 0, 1, 3, 5, 7, 5, 3, 1, 0], 'battery': 5}
# print(GraphMethods.validChargerLists(bus, world))

buses = [
    [0, 2, 4, 6, 8, 6, 4, 2, 0, 1, 3, 5, 7, 5, 3, 1, 0],
    [0, 2, 9, 10, 14, 17, 12, 6, 4, 2, 0],
    [0, 1, 28, 20, 22, 25, 23, 24, 25, 26, 5, 3, 1, 0],
    [0, 1, 3, 5, 31, 32, 33, 34, 35, 29, 1, 0],
    [0, 40, 41, 38, 36, 37, 34, 35, 29, 1, 0],
    [0, 40, 39, 38, 42, 43, 50, 49, 46, 47, 6, 4, 2, 0],
    [0, 2, 4, 6, 12, 18, 16, 17, 14, 13, 19, 20, 28, 1, 0],
    [0, 1, 3, 5, 26, 25, 24, 23, 22, 21, 20, 28, 1, 0],
    [0, 1, 29, 30, 31, 32, 33, 34, 35, 29, 1, 0],
    [0, 40, 39, 38, 41, 44, 45, 2, 0],
   # [0, 2, 4, 6, 47, 46, 48, 49, 50, 43, 42, 41, 40, 0],
   # [0, 2, 9, 13, 19, 20, 22, 25, 26, 5, 3, 1, 0],
]

run_data = open(("average_run_data3.csv"), "w")

for i in range(25):
    for j in range(10):
        run_data.write(str(len(GraphMethods.greedyChargingArrays(buses, world, 5*(1+j))))+",")
    run_data.write("\n")

