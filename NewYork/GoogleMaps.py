import requests
import osmnx as ox
import networkx as nx
import geopandas as gp
import geopy

api_file = open("../APIFILE_DO_NOT_GIT.txt", "r")
api = api_file.read().strip()


def convertFileToRouteNYC(filename):

    routeFile = open(filename, "r")
    route = []
    lines = routeFile.readlines()

    for i in range(len(lines)):
        if i != 0:
            route.append(lines[i].strip("\n") + ", New York")

    return route, lines[0].strip()


def convertMoovitToLatLong(moovit_file):

    names = []
    lats = []
    longs = []
    miles = []

    latlongfile = open("LatLong/" + moovit_file[0:-4]+"latlong.txt", "w")
    addresses, name = convertFileToRouteNYC("NycRoutes/" + moovit_file)

    latlongfile.write(name+"\n")

    for i in range(len(addresses)):
        address = addresses[i].replace(" ", "+").replace("/", "+")

        geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + api
        json = requests.get(geocode_url)
        j = json.json()
        t = j['results'][0]['geometry']['location']

        names.append(addresses[i].strip())
        lats.append(t['lat'])
        longs.append(t['lng'])

    for j in range(len(names)):

        if j == 0:
            miles.append(0)
        else:
            start = names[j-1].replace(" ", "+").replace("/", "+")
            end = names[j].replace(" ", "+").replace("/", "+")

            url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + start + "&destinations=" + end + "&key=" + api + "&mode=driving"
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)

            d = response.json()
            v = d['rows'][0]['elements'][0]['distance']['value']
            miles.append(v)


        latlongfile.write(names[j]+">>"+ str(lats[j]) + ">>" + str(longs[j]) + ">>"+str(miles[j])+ "\n")


convertMoovitToLatLong("M1Route.txt")



