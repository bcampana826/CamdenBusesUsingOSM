import json


def method(world, battery):
    temp_dict = dict()

    stops = []
    for i in world["routes"]:
        for y in range(len(world["routes"][i]) - 1):
            if ("n" + str((world["routes"][i][y]))) not in stops:
                stops.append("n" + str((world["routes"][i][y])))

    print(stops)
    print(len(stops))

    b = "-[";
    A = "-[";

    for j in world["routes"]:

        temp_route = world["routes"][j]
        temp_dist = 0
        working_temp_route = []

        for k in range(len(temp_route) - 1):
            combo = str(temp_route[0]) + ">" + str(temp_route[k + 1])

            temp_dist += int(world["stops"][str(k + 1)]["prev_dist"]) / 1609
            b += str(temp_dist)+";"

            working_temp_route.append(temp_route[k])

            for z in stops:

                if int(z[1:]) in working_temp_route:
                    A += str(battery)+","
                else:
                    A += str(0)+","

            A = A[:-1]+";"

    b = b[:-1]

    A +="];"
    b +="];"

    f = "["
    for p in range(len(stops)):
        f+="1,"
    f = f[:-1] + "];"
    return A, b, f, (b.count(";"))


with open("worlds/full-world.json") as json_file:
    world = json.load(json_file)

stops = []
for i in world["routes"]:
    for j in range(len(world["routes"][i])-1):
        stops.append("n" + str((world["routes"][i][j])))

A, b, f, num = method(world, 20)

file = open("matlabFiles/optimize.txt","w")

file.write(A)
file.write("\n")
file.write(b)
file.write("\n")
file.write(f)
file.write("\n")
file.write(str(num))


print(A.count(";"))
print(b)
print(f.count(","))
print(num)