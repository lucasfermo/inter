import turtle


def drawTriangle(points,color,t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    t.end_fill()


def sierpinski(points,degree, t):
    colormap=["blue","red","green","white","yellow","violet"]
    drawTriangle(points,colormap[degree],t)
    if degree>0:
        sierpinski([points[0],
            getmid(points[0],points[1]),
            getmid(points[0],points[2])],
            degree-1,t)
        sierpinski([points[1],
            getmid(points[1],points[0]),
            getmid(points[1],points[2])],
            degree-1,t)
        sierpinski([points[2],
            getmid(points[2],points[0]),
            getmid(points[2],points[1])],
            degree-1,t)

def getmid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)


def main():
    t=turtle.Turtle()
    myWin=turtle.Screen()
    t.up()
    t.goto(100,-50)
    t.down()
    myPoints=[[-100,-50],[0,100],[100,-50]]
    sierpinski(myPoints,4,t)

main()
