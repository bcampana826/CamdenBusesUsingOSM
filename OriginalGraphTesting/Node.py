class Node:

    def __init__(self, num, charger):

        self.edges = {"node":"temp"}
        self.charger = charger
        self.num = num

    def add_edge(self, nodeNum, length):
        self.edges.update({str(nodeNum) : length})

    def get_edge(self, nodeNum):
        return self.edges[str(nodeNum)]
