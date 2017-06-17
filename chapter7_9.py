import math,os, sys,random,time,turtle,operator
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

os.chdir("C:\\Users\\LF\\.atom\\inter")

class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id)+ "  Connected to  " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0

    def addVertex(self,key):
        newVertex=Vertex(key)
        self.numVertices=self.numVertices+1
        self.vertList[key]=newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def buildGraph(wordFile):
    d={}
    g=Graph()
    wfile=open(wordFile,'r')

    for line in wfile:
        word=line[:-1]
        for i in range(len(word)):
            bucket=word[:i]+"_"+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]

    for bucket in d.keys():
        print(bucket)
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)

    return g

def bgs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue=Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size()>0):
        currentVert=vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor()=='white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
        currentVert.setColor("black")

def traverse(y):
    x=y
    while(x.getPred()):
        print(x.getId())
        x=x.getpred()
    print(x.getId())

G=buildGraph("wordlist.txt")
traverse(G.getVertex("sage"))
