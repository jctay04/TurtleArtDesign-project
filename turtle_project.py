import turtle
from design_functions import *

jaden = turtle.Turtle()
jaden.color("yellow")
jaden.speed(0)
window = turtle.Screen()
size = 1

for times in range(180):
    jaden.forward(100)
    jaden.right(30)
    jaden.forward(20)
    jaden.left(60)
    jaden.forward(50)
    jaden.right(30)
  
    jaden.penup()
    jaden.setposition(0,0)
    jaden.pendown()
  
    jaden.right(2)

bob = turtle.Turtle()
bob.color("black")
bob.pensize(2)
bob.speed(0)

for times in range(500):
    bob.color("purple")
    bob.width(6)
    bob.circle(300000)
    bob.right(25)


window.bgcolor("blue")  

