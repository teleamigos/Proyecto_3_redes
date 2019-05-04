import sys
infinity = sys.maxint-1

class Vertex:
    def __init__(self, name ):#Constructor
        self.id = name
        self.adjacent = {}
        self.pi = None#Padre
        self.key = infinity

    def add_neighbor(self,neighbor,weight=0):
        self.adjacent[neighbor]=weight

    def adjacentlist(self):

        return self.adjacent.keys()

    def getKey(self):
        return self.key
    def setKey(self,k):
        self.key=k
