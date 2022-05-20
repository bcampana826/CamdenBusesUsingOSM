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
        if i != 0 and len(lines[i])>5:
            temp = lines[i].split(">>")
            lines[i] = temp[0]
            route.append(lines[i].strip("\n") + ", New Jersey")

    return route, lines[0].strip()


def convertMoovitToLatLong(moovit_file):

    names = []
    lats = []
    longs = []
    miles = []

    latlongfile = open("LatLong/" + moovit_file[0:-4]+"latlong.txt", "w")
    addresses, name = convertFileToRouteNYC(moovit_file)

    latlongfile.write(name+"\n")

    for i in range(len(addresses)):


        address = addresses[i].replace(" ", "+").replace("/", "+")

        print(address)
        print(api)
        geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + api
        print(geocode_url)
        json = requests.get(geocode_url)
        j = json.json()
        print(j)
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
            print(url)
            payload = {}
            headers = {}
            #response = requests.request("GET", url, headers=headers, data=payload)

            response = requests.request("GET", "https://maps.googleapis.com/maps/api/distancematrix/json?origins=E+126+ST+3+AV,+New+York&destinations=LEXINGTON+AV+E+125+ST,+New+York&key=AIzaSyDvv82-IAw44xsHa0mlqfg4XyXEHtmPOFo&mode=driving", headers=headers, data=payload)

            d = response.json()
            v = d['rows'][0]['elements'][0]['distance']['value']
            miles.append(v)


        latlongfile.write(names[j]+">>"+ str(lats[j]) + ">>" + str(longs[j]) + ">>"+str(miles[j])+ "\n")


convertMoovitToLatLong("Manual419Route.txt")
convertMoovitToLatLong("Manual450Route.txt")
convertMoovitToLatLong("Manual452Route.txt")
convertMoovitToLatLong("Manual453Route.txt")
convertMoovitToLatLong("Manual457Route.txt")


