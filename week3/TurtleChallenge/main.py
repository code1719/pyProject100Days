import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "LightGreen"]

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3, 11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)


tom = Turtle()
tom.shape("turtle")
tom.pensize(10)
tom.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]

for _ in range(200):
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))











screen = Screen()
screen.exitonclick()