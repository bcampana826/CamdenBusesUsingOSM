import osmnx as ox
import networkx as nx
import geopandas as gp
import geopy
from datetime import timedelta

def convertFileToRoute(filename):
    routeFile = open(filename, "r")
    route = []
    lines = routeFile.readlines()

    for i in lines:
        route.append(i.strip("\n") + ", New York")

    return route


def geocodeDistance(list, graphName):
    # Load the graph
    G = ox.load_graphml(graphName)

    distances = []
    total = 0

    first = None
    second = None

    for l in list:
        if first is None:
            second = ox.geocode(l)
            first = second
            continue
        else:
            first = second
            second = ox.geocode(l)

            origin_node = ox.get_nearest_node(G, first)
            destination_node = ox.get_nearest_node(G, second)

            # Get the distance in meters
            distance_in_meters = nx.shortest_path_length(G, origin_node, destination_node, weight='length')

            distances.append(distance_in_meters)
            total += distance_in_meters

    return distances, total








d, t = geocodeDistance(convertFileToRoute("BusRoutes/M1Route.txt"),"CityGraphs/Camden.graphml")
print(d)
print(t)
