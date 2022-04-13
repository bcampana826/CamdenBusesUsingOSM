import json

import googlemaps

api_file = open("../APIFILE_DO_NOT_GIT.txt", "r")
api = api_file.read().strip()
gmaps = googlemaps.Client(key=api)

def print_map(world, route, chargers_in_id, picture_name):

    chargers = []
    for i in chargers_in_id:
        chargers.append(world["stops"][str(i)].get("name"))

    locations = []
    for j in route:
        locations.append(world["stops"][str(j)].get("name"))



    markers = ["color:blue|size:tiny|label:" + chr(65+i) + "|"
                       + r for i, r in enumerate(chargers)]

    result_map = gmaps.static_map(
                     center=locations[5],
                     scale=2,
                     zoom=12,
                     size=[1280, 1280],
                     format="jpg",
                     maptype="roadmap",
                     markers=markers,
                     path="color:0x0000ff|weight:2|" + "|".join(locations))

    with open("driving_route_map3.jpg", "wb") as img:
        for chunk in result_map:
            img.write(chunk)

with open("worlds/StartingWorld2.json") as json_file:
    world = json.load(json_file)

print_map(world, world["routes"]["M1"], [89, 62, 128, 168, 0, 33, 60, 61, 135, 136, 166, 171, 204, 212], "pict.jpg")