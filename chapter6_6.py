import math,os, sys,random,time,turtle
from current import Stack
#Quick sort

class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self, newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key=obj

    def getRootVal(self):
        return self.key

def parseEquation(equation):
    return list(equation)

print(parseEquation("(3+(4*5))"))

def buildTree(equation):
    pStack=Stack()
    T=buildTree("")
    current=T
    for i in equation:
        if i=="(":
            current.insertLeft("")
            pStack.push(current)
            current=current.getLeftChild()
        elif i not in ["+","-","*","/",")"]:
            current.setRootVal(int(i))
            parent=pStack.pop()
            current=parent
        elif i in ["+","-","*","/"]:
            current.setRootVal(i)
            current.insertRight("")
            pStack.push(current)
            current=current.getRightChild()
        elif i==")":
            current=pStack.pop()
        else:
            raise ValueError

    return T

def evaluate(parseTree):
    pass

print(operator.add(4,5))
