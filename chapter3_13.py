import math,os, sys,random,time

class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

namelist=["lucas","fermo","keith","luke"]


def hotPotato(namelist,num):
    q=Queue()
    length=len(namelist)
    for name in namelist:
        q.enqueue(name)

    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

print(hotPotato(namelist,3))

q=Queue()

q.enqueue("lucas")
q.enqueue("fermo")
q.enqueue("reily")
print(q.dequeue())
