import math,os, sys,random,time

class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0

    def tick(self):
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None

    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currentTime):
        return currentTime-self.timestamp

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

def simulation(numSeconds,pagesPerMinute):
    labPrinter=Printer(pagesPerMinute)
    printerQueue=Queue()
    waitingTimes=[]

    for currentSecond in range(numSeconds):
        if newPrinterTask():
            task=Task(currentSecond)
            printerQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printerQueue.isEmpty()):
            newTask=printerQueue.dequeue()
            waitingTimes.append(newTask.waitTime(currentSecond))
            labPrinter.startNext(newTask)

        labPrinter.tick()

    averageWaitTime=sum(waitingTimes)/len(waitingTimes)
    print("Average wait is %6.2f,%3d tasks remaining"%(averageWaitTime,printerQueue.size()) )


def newPrinterTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False

simulation(1000,10)
