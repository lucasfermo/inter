import math,os, sys,random,time,turtle,operator
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

os.chdir("C:\\Users\\LF\\.atom\\inter")

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time=0

    def dfs(self):
        for aVertex in self:

            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor()=="white":
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor("gray")
        self.time+=1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor()=='white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')

        self.time+=1
        startVertex.setFinish(self.time)


g=DFSGraph()
g.addEdge("a","b")
g.addEdge("b","c")
g.addEdge("a","d")
g.addEdge("d","e")
g.addEdge("b","d")
g.addEdge("e","f")
g.addEdge("f","c")
g.addEdge("e","b")

g.dfs()
print(g.vertices.keys())
for v in g:
    print("Vertex %s has a finish time of %s" %(v.id,v.fin))
