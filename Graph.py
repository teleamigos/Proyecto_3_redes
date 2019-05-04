from Vertex import *

class Graph:#diccionario de diccionarios
    def __init__(self):
        self.G={}
        self.num_vertices=0
    def add_vertex(self,name):
        new_vertex=Vertex(name)
        self.G[name]=new_vertex
        self.num_vertices=self.num_vertices+1

    def add_edge(self,start,end,weight=0,digraph=0):
        if start not in self.G:
            self.add_vertex(start)
        if end not in self.G:
            self.add_vertex(end)
        if digraph==1:
            self.G[start].add_neighbor(self.G[end],weight)
        else:
            self.G[start].add_neighbor(self.G[end],weight)
            self.G[end].add_neighbor(self.G[start],weight)

    def get_vetices(self):
        return self.G.values()
    def set_startNode(self,star):
        #Pone peso cero a grafo
        self.G[start].key=0
