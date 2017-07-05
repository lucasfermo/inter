import math,os, sys,random,time

class Node:
    def __init__(self,initData):
        self.data=initData
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data=newData

    def setNext(self,newNext):
        self.next=newNext

class UnorderedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self, item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.getNext()

        return count

    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()

        return found

    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not Found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()

        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self,item):
        temp=Node(item)
        current=self.head
        size=self.size()
        count=0
        while current.getNext() !=None:
            current=current.getNext()
        current.setNext(temp)

    def insert(self,index,item):
        temp=Node(item)
        count=0
        current=self.head
        previous=None
        while count!=index and current.getNext()!=None:
            previous=current
            current=current.getNext()
            count+=1

        previous.setNext(temp)
        temp.setNext(current)

    def pop(self):
        current=self.head
        previous=None
        while current.getNext()!=None:
            previous=current
            current=current.getNext()
        previous.setNext(None)

    def index(self,item):
        count=0
        current=self.head
        while current.getData()!=item:
            if current.getNext()==None:
                return False
            current=current.getNext()
            count+=1

        return count


Q=UnorderedList()

Q.add(14)
Q.add(25)
Q.insert(1,15)
Q.add(7)

print(Q.search(14))
print(Q.index(7))
