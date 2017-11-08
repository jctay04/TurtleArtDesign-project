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
"""    
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
 
  #Turtle Taylor
  taylor = turtle.Turtle()
  taylor.color("orange")
  taylor.pensize(2)
  taylor.speed(0)
  
  

for times in range(36):
    draw_square(turtle)
    turtle.right(10)

for times in range(size):
    turtle.forward(50)
    turtle.right(91)
    size += 1


window = Screen()
window.bgcolor("green")

draw_art()

window.exitonclick()


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
  
    turtle.done()


window = Screen()  
window.bgcolor("green")

draw_art()
"""
