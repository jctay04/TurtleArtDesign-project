"""
def draw_square(some_turtle):

    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():

    # Turtle Brad
    brad = Turtle(shape="turtle")
    brad.color("yellow")
    brad.pensize(2)
    brad.speed("normal")  # 6/normal is the default so don't need to do it

    for _ in range(36):
        draw_square(brad)
        brad.right(10)

    # Turtle Angie
    angie = Turtle(shape="turtle")
    angie.color("blue")
    angie.pensize(2)
    angie.speed(5)  # slightly slower than brad

    size = 1

    for _ in range(300):
        angie.forward(size)
        angie.right(91)
        size += 1

window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()
"""
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

    Chris =turtle.Turtle()
    Chris.color("red")
    Chris.begin_fill()
    Chris.circle(50)
    Chris.end_fill()
    
"""    
def moveToRandomLocation():
    turtle.penup()
    turtle.setpos( randint(-400,400) , randint(-400,400) )
    turtle.pendown()

def draw_star(starSize, starColor):
    turtle.color(starColor)
    turtle.pendown()
    begin_fill()
    for times in range(5):
        t.left(144)
        t.forward(starSize)
    end_fill()
    penup()

for star in range(30):
    moveToRandomLocation()
    drawStar( randint(5,25) , "blue")
 
""" 
