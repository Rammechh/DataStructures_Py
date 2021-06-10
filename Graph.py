#   A---------C
#   |         | \
#   |         |  E
#   |         | /
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

all_edges=[
    ("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")
]

class Graph:
    #passing the List of Nodes
    def __init__(self,Nodes, is_directed=False):
        self.nodes = Nodes
        self.adj_List = {}
        self.is_directed=is_directed
        #creating an empty list for all nodes
        for node in nodes:
            self.adj_List[node]=[]

    #Adding all the Edges
    def add_edge(self,u,v):
        self.adj_List[u].append(v)
        if self.is_directed== False:
            self.adj_List[v].append(u)

    #Finding the Degree
    def degree(self,node):
        deg = len(self.adj_List[node])
        return deg

    #Printing the Nodes
    def print_adjList(self):
        for node in self.nodes:
            print(node,"->", self.adj_List[node])
    
nodes=["A","B","C","D","E"]
graph=Graph(nodes,is_directed=True)
# graph.print_adjList()
 
# Add the edges ( In both dir)
for u,v in all_edges:
    graph.add_edge(u,v)
graph.print_adjList()

#Printing the degree of any node [degree- no of adj nodes connected to a particular node]
print("Degree of C",graph.degree('C'))
