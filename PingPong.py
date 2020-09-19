from graphics import*
from keyboard import*

win = GraphWin('Ping Pong',600,400)
win.setBackground("green")

#racket 1
racket1 = Rectangle(Point(5,1),Point(10,70))
racket1.setOutline("red")
racket1.setFill("red") 
racket1.draw(win)
racket1.move(580,170)

#racket 2
racket2 = Rectangle(Point(5,1),Point(10,70))
racket2.setOutline("blue")
racket2.setFill("blue") 
racket2.draw(win)
racket2.move(5,170)

#ball
ball = Circle(Point(20,20),8)
ball.setOutline("orange")
ball.setFill("orange") 
ball.draw(win)
ball.move(290,170)

#Functions
def racket1_up():
    p = racket1.getP1()
    y = p.getY()
    y += 20
    racket1.move(580,190)

def racket1_down():
   p = racket1.getP1()
   y = p.getY()
   y -= 20
   racket1.move(580,-150)

def racket2_up():
   p = racket2.getP1()
   y = p.getY()
   y += 20
   racket2.move(5,190)

def racket2_down():
   p = racket2.getP1()
   y = p.getY()
   y -= 20
   racket2.move(5,-150)

   keyboard = win.getKey()

   keyboard.is_pressed(racket1_up,"a")
   keyboard.is_pressed(racket1_down,"z")
   keyboard.is_pressed(racket2_up,"Up")
   keyboard.is_pressed(racket2_down,"Down")


win.getMouse()
win.close()






