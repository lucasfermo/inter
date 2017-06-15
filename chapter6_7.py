import math,os, sys,random,time,turtle
from current import Stack, BinaryTree,buildTree,evaluate


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree!=None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def postOrderEval(tree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    res1=None
    res2=None
    if tree:
        res1=postOrderEval(tree.getLeftChild())
        res2=postOrderEval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

def inorder(tree):
    if tree!=None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild)

eq="(3+(4*5))"
t=buildTree(eq)
postorder(t)
