from graphics import*
from keyboard import*
from random import random





def racket1_up(racket1):
   racket1.move(0,-20)  
    

def racket1_down(racket1):
   racket1.move(0,20)  

def racket2_up(racket2):
   racket2.move(0,-20)  

def racket2_down(racket2):
   racket2.move(0,20)  

   

def main():
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

      #move ball
      
      





   
   win.close()


main()





