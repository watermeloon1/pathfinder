import math

MAX_int = 9999999

def distance(vertex1, vertex2):
    return math.sqrt(pow(vertex1.x-vertex2.x,2)+pow(vertex1.y-vertex2.y,2))

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = []

        self.distance = MAX_int
        self.heuristic = MAX_int
        self.visited = False
        
    def add_neighbour(self, vertex):
        self.neighbours.append(vertex)

class Graph:

    vertices = []
    first = True

    def add_vertex(self,vertex):
        self.vertices.append(vertex) 

    def add_edge(self,u,v):
        self.vertices[u].add_neighbour(self.vertices[v])
        self.vertices[v].add_neighbour(self.vertices[u])

    def algorithm(self, start_index, end_index):

        if not self.first:
            for z in self.vertices:
                if z.distance != MAX_int:   
                    z.distance = MAX_int
                    z.visited = False
                    
        self.first = False

        queue = []
        queue.append(self.vertices[start_index])
        self.vertices[start_index].distance = 0
        self.vertices[start_index].heuristic = distance(self.vertices[start_index],self.vertices[end_index])

        while not self.vertices[end_index].visited:
            v = queue.pop(self.minimum_index(queue))
                  
            for i in v.neighbours:
                if not i.visited:
                    if i.distance > v.distance + distance(v, i) :
                        i.distance = v.distance + distance(v, i)
                        i.heuristic = i.distance + distance(i,self.vertices[end_index])

                    queue.append(i)

            v.visited = True

        return round(self.vertices[end_index].distance,2)

    def minimum_index(self,array):
        index = 0
        for i in range(1,len(array)):
            if array[index].heuristic > array[i].heuristic :
                index = i
        return index
                
graph = Graph()

num_paths = int(input())
num_nodes = int(input())
num_edges = int(input())

input()
paths = []

for i in range(num_paths):
    temp = input()
    list_temp = temp.split('\t')

    paths.append(int(list_temp[0]))
    paths.append(int(list_temp[1]))

input()

for i in range(num_nodes):
    temp = input()
    list_temp = temp.split('\t')

    graph.add_vertex(Vertex(int(list_temp[0]),int(list_temp[1])))

input()

for i in range(num_edges):
    temp = input()
    list_temp = temp.split('\t')

    graph.add_edge(int(list_temp[0]), int(list_temp[1]))

for i in range(0,len(paths),2):
    print(graph.algorithm(paths[i],paths[i+1]))
    print('\t')