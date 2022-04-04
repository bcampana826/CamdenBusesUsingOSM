import osmnx as ox
import networkx as nx
import geopandas as gp
import geopy
from datetime import timedelta

'''
graph_area = ("Manhattan, New York, USA")

# Create the graph of the area from OSM data. It will download the data and create the graph
G = ox.graph_from_place(graph_area, network_type='drive')

# OSM data are sometime incomplete so we use the speed module of osmnx to add missing edge speeds and travel times
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)

# Save graph to disk if you want to reuse it
ox.save_graphml(G, "CityGraphs/Camden.graphml")
'''
# Load the graph
G = ox.load_graphml("CityGraphs/Camden.graphml")

# Plot the graph
fig, ax = ox.plot_graph(G, figsize=(10, 10), node_size=0, edge_color='y', edge_linewidth=0.2)


# Two pairs of (lat,lng) coordinates
origin_coordinates = ox.geocode("Madison Av/E 101 St, New York, New York")
destination_coordinates = (40.73036078549269, -73.99142278844137)

# If you want to take an address (osmx will use Nominatim service for this)

# In the graph, get the nodes closest to the points
origin_node = ox.get_nearest_node(G, origin_coordinates)
destination_node = ox.get_nearest_node(G, destination_coordinates)


# Get the shortest route by distance
shortest_route_by_distance = ox.shortest_path(G, origin_node, destination_node, weight='length')

# Plot the shortest route by distance
fig, ax = ox.plot_graph_route(G, shortest_route_by_distance, route_color='y', route_linewidth=6, node_size=0)
'''
# Get the shortest route by travel time
shortest_route_by_travel_time = ox.shortest_path(G, origin_node, destination_node, weight='length')

# Plot the shortest route by travel time
fig, ax = ox.plot_graph_route(G, shortest_route_by_travel_time, route_color='y', route_linewidth=6, node_size=0)

# Plot the 2 routes
fig, ax = ox.plot_graph_routes(G, routes=[shortest_route_by_distance, shortest_route_by_travel_time], route_colors=['r', 'y'], route_linewidth=6, node_size=0)
'''
# Get the travel time, in seconds
# Note here that we use "nx" (networkx), not "ox" (osmnx)
travel_time_in_seconds = nx.shortest_path_length(G, origin_node, destination_node, weight='travel_time')
print(travel_time_in_seconds)

#The travel time in "HOURS:MINUTES:SECONDS" format
travel_time_in_hours_minutes_seconds = str(timedelta(seconds=travel_time_in_seconds))
print(travel_time_in_hours_minutes_seconds)

# Get the distance in meters
distance_in_meters = nx.shortest_path_length(G, origin_node, destination_node, weight='length')
print(distance_in_meters)
# Distance in kilometers
distance_in_kilometers = distance_in_meters / 1000
print(distance_in_kilometers)
