from graphics import*
from keyboard import*
import time, random





def racket1_up(racket1):
   racket1.move(0,-20)  
    

def racket1_down(racket1):
   racket1.move(0,20)  

def racket2_up(racket2):
   racket2.move(0,-20)  

def racket2_down(racket2):
   racket2.move(0,20)  

   

def main():
   winWidth = 600
   winHeight = 400
   win = GraphWin('Ping Pong',winWidth,winHeight)
   win.setBackground("green")
   win.setCoords(0,0,winWidth, winHeight)

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
   radius = 8
   xLow = radius
   xHigh = winWidth - radius
   yLow = radius
   yHigh = winHeight - radius
   a = random.randrange(xLow,xHigh +1)
   b = random.randrange(yLow,yHigh +1)
   center = Point(a, b)

   ball = Circle(center,radius)
   ball.setOutline("orange")
   ball.setFill("orange") 
   ball.draw(win) 


   #move racket
   while True:
      
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
      break
   
   
   #move ball
   dx = 3
   dy = 5
   delay = .005
   for i in range(600): 
       ball.move(dx, dy)
       center = ball.getCenter()
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
    
   
   
    
     win.close()


main()







