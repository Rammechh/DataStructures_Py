#   A---------C
#   | \       | \
#   |   \     |  E
#   |     \   | /
#   B---------D
adj_List = {
    "A":["B","C"],
    "B":["A","D"],
    "C":["A","D","E"],
    "D":["B","C","E"],
    "E":["C","D"]
}

# #To find adj node or vertice of node "B"
# print(adj_List["B"])

# #To add another edge between A and D, Sine it is undirected graph append on both sides
# adj_List["A"].append("D")
# adj_List["D"].append("A")

# #print list
# print(adj_List)

class Graph:
    #passing the List of Nodes
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_List = {}
        #creating an empty list for all nodes
        for node in nodes:
            self.adj_List[node]=[]
            
    #Printing the Nodes
    def print_adjList(self):
        for node in self.nodes:
            print(node,"->", self.adj_List[node])
    
nodes=["A","B","C","D","E"]
graph=Graph(nodes)
graph.print_adjList()

