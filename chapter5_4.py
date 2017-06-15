import math,os, sys,random,time,turtle

def binarySearch(alist,item):
    first=0
    last=len(alist)-1
    found=False

    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if alist[midpoint]>item:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)

    return found




alist=[1,4,5,6,11,13,27,10]

print(binarySearch(alist,6))
