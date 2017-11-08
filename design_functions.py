
import turtle
from random import randint

def draw_square(turtle):
  
    for times in range(4):
        turtle.forward(200)
        turtle.right(90)
  
  
def draw_art():
  
  #Turtle Bob
  bob = turtle.Turtle()
  bob.color("black")
  bob.pensize(2)
  bob.speed(0)
  
  
for times in range(36):
    draw_square(turtle)
    turtle.right(10)

    size=1
for times in range(50):
    turtle.forward(size)
    turtle.right(91)
    size += 1


    #Turtle Taylor
    taylor = turtle.Turtle()
    taylor.color("orange")
    taylor.pensize(2)
    taylor.speed(0)
    
    #Turtle Chris
    Chris =turtle.Turtle()
    Chris.color("red")
    Chris.begin_fill()
    Chris.circle(50)
    Chris.end_fill()
    
