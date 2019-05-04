#Dijkstra class ClassName(object):

from Graph import*

class Dijkstra:
    def __init__(self,G,start):
        self.graph=G
        self.Q=G.get_vetices()#queue
        G.set_startNode(start)#start path
    def shortestPath(self):
        while self.Q:
            self.Q.sort(key=lambda x:x.key)
            u=self.Q.pop(0)

            for v in u.adjacent.keys():
                if v.key > u.key + u.adjacent[v]:
                    if v.key> u.key + u.adjacent[v]:
                        v.key=u.key + u.adjacent[v]
                        v.pi=u
    def printPath(self,start,end):
        l=[]
        current=self.graph.G[graph]
        while current!=None:
            l.append(current.id)
            current=current.pi
        l.reverse()
        print l
