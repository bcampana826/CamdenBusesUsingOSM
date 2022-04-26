import json

import gurobipy as gp
from gurobipy import GRB


def method(world,battery):
    temp_dict = dict()
    stops = []
    for i in world["stops"]:
        stops.append("n"+str(i))
    constraints = []

    target_distances = []

    for j in world["routes"]:
        temp_route = world["routes"][j]
        temp_dist = 0
        for k in range(len(temp_route) - 1):
            combo = str(temp_route[0]) + ">" + str(temp_route[k + 1])
            constraints.append(combo)

            temp_dist += int(world["stops"][str(k+1)]["prev_dist"])/1609
            target_distances.append(temp_dist)

            for z in stops:
                if int(z[1:]) in temp_route:
                    temp_dict[(combo, z)] = battery
                else:
                    temp_dict[(combo, z)] = 0

    combinations, scores = gp.multidict(temp_dict)

    return combinations, scores, stops, constraints, target_distances


with open("worlds/full-world.json") as json_file:
    world = json.load(json_file)

combinations, scores, stops, constraints, target_distances = method(world,5)

print(stops)
# Resource and job sets
R = constraints
J = stops

# Declare and initialize model
m = gp.Model('RAP')

# Create decision variables for the RAP model
x = m.addVars(combinations, name="assign")

# ---------------------------------------------------------------
# Create stop constraints
jobs = m.addConstrs((x.sum('*',J[p]) == target_distances[p] for p in range(len(J))), name='stops')


