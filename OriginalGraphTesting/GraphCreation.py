from Node import Node


def parse_edge(node, stringEdge):
    '''
    Helper method for the read graph method
    :param stringEdge: to parse into an edge to add
    '''
    nums = stringEdge.strip(')').strip('(').strip(';').split(',')
    if nums[0] != '':
        node.add_edge(float(nums[0]), float(nums[1]))


def read_graph(strLocation):
    '''
    Returns a list of nodes
    '''
    graph = []
    world = open(strLocation, "r").readlines()

    for i in range(len(world)):

        splitStr = world[i].split(">")
        node = Node(int(splitStr[0].split(" ")[0].strip()), splitStr[0].count("C") >= 1)

        splitStr = splitStr[1].split(";")
        for j in range(len(splitStr)):
            parse_edge(node, splitStr[j].strip())

        graph.append(node)

    return graph
