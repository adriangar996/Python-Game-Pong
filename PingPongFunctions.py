from graphics import *
import time, random

def racket1_up(racket1):
   racket1.move(0,20)  
    

def racket1_down(racket1):
   racket1.move(0,-20)  

def racket2_up(racket2):
   racket2.move(0,20)  

def racket2_down(racket2):
   racket2.move(0,-20)  

def bounceBall(shape, dx, dy, xLow, xHigh, yLow, yHigh):

    delay = .005
    for i in range(600):
        shape.move(dx, dy)
        center = shape.getCenter()
        x = center.getX()
        y = center.getY()
        if x < xLow:
            dx = -dx
        elif x > xHigh:
            dx = -dx
        if y < yLow:
            dy = -dy
        elif y > yHigh:
            dy = -dy            
        time.sleep(delay)

def getRandomPoint(xLow, xHigh, yLow, yHigh):
    x = random.randrange(xLow, xHigh+1)
    y = random.randrange(yLow, yHigh+1)
    return Point(x, y)   

def createBall(center, radius, win):
    ball = Circle(center, radius)
    ball.setOutline("orange")
    ball.setFill("orange")
    ball.draw(win)
    return ball

def createRacket1(win):
    #racket 1
    racket1 = Rectangle(Point(5,1),Point(10,70))
    racket1.setOutline("red")
    racket1.setFill("red") 
    racket1.draw(win)
    racket1.move(580,170)
    return racket1

def createRacket2(win):
    racket2 = Rectangle(Point(5,1),Point(10,70))
    racket2.setOutline("blue")
    racket2.setFill("blue") 
    racket2.draw(win)
    racket2.move(5,170)
    return racket2

def movePaddles(racket1,racket2,win):
  
    while True:
    #move racket
        key = win.checkKey()
        if key == "q":
            break
        elif key == "Up":
            racket1_up(racket1)
        elif key == "Down":
            racket1_down(racket1)
        elif key == "a":
            racket2_up(racket2)
        elif key == "z":
            racket2_down(racket2)


def Pong(dx, dy):
    
    
    winWidth = 600
    winHeight = 400
    win = GraphWin("Ping Pong", winWidth, winHeight)
    win.setBackground("green")
    win.setCoords(0,0,winWidth, winHeight)


    radius = 8
    xLow = radius 
    xHigh = winWidth - radius
    yLow = radius
    yHigh = winHeight - radius

    center = getRandomPoint(xLow, xHigh, yLow, yHigh) 
    ball = createBall(center, radius, win)
    paddle1 = createRacket1(win)
    paddle2 = createRacket2(win)

    bounceBall(ball, dx, dy, xLow, xHigh, yLow, yHigh)
    movePaddles(paddle1,paddle2,win) 
   
     

    
    win.close()
Pong(3, 5)
