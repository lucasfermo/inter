from current import Stack
import turtle

def moveTower(height,fromPole,toPole,withPole):
    if height>= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        movePole(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def movePole(fromPole,toPole):
    print("Moving disk from {} to {}".format(fromPole,toPole))


moveTower(3,"A","B","C")
