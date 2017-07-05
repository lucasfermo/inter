import math,os, sys,random,time

class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def postfix(string):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=1
    prec["("]=1
    opStack=Stack()
    postfixList=[]
    tokenList=list(string)

    #Sorts input into stack or output list
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "1234567890":
            postfixList.append(token)
        elif token=="(":
            opStack.push(token)
        elif token==")":
            topToken=opStack.pop()
            while topToken!="(":
                postfixList.append(topToken)
                topToken=opStack.pop()
        elif token in "+-*/":
            if not opStack.isEmpty():
                topToken=opStack.peek()

                while prec[topToken]>prec[token] :
                    postfixList.append(topToken)
                    opStack.pop()
                    topToken=opStack.peek()
            opStack.push(token)


    #Appends remaining operators to the output list
    while not opStack.isEmpty():
        topToken=opStack.pop()
        postfixList.append(topToken)
    postfixList="".join(postfixList)

    return postfixList

print(postfix("(A*B)+(C*D)"))
