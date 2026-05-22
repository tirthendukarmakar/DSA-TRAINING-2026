# A:[B,C,D],
# B:[A,E],
# C:[]

class Graph:
    # Fixed: Added double underscores before and after init
    def __init__(self):
        self.adjacency_list = {} 

    def add_vertex(self, vertex):
        # Tip: Dropping .keys() makes this run faster
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "A")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "A")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "A")
my_graph.add_edge("D", "C")
my_graph.add_edge("D", "E")
my_graph.add_edge("E", "B")
my_graph.add_edge("E", "D")

my_graph.print_graph()