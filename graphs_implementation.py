# Ways in which we can create graphs:
# 1. Edge List
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent List
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent Matrix
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]


class Graph:

    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show_connections(self):
        print(self.adjacent_list)


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_edge(3, 1)
graph.add_edge(3, 4)
graph.add_edge(4, 2)
graph.add_edge(4, 5)
graph.add_edge(1, 2)
graph.add_edge(1, 0)
graph.add_edge(0, 2)
graph.add_edge(6, 5)
graph.show_connections()