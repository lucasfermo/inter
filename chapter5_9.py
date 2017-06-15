import math,os, sys,random,time,turtle

def insertion(myList):
    for i in range(1,len(myList)):
        current=myList[i]
        position=i

        while position>0 and myList[position-1]>myList[position]:
            myList[position-1]=myList[position]
            position=position-1

        myList[position]=current


def shell(myList):
    sublistcount=len(alist)//2
    while sublistcount>0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        sublistcount=sublistcount//2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentValue=alist[i]
        position=i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position=position-gap

        alist[position]=currentvalue

myList=[54,26,93,17,77,31,44,55,20]




print(sort(myList))
