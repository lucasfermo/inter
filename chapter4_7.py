import math,os, sys,random,time,turtle

t=turtle.Turtle()
myWin=turtle.Screen()

def triangle(branchLen,t):
    if branchLen>0:
        t.forward(120)
        t.left(135)
        t.forward(100)
        t.left(90)
        t.forward(100)
        triangle(branchLen-10,t)

triangle(10,t)


def tree(branchLen,t):
    if branchLen>5:
        print(branchLen)
        t.forward(branchLen)
        t.right(20)
        print("firstCall")
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t=turtle.Turtle()
    myWin=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()
