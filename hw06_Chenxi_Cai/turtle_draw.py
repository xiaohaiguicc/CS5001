"""
draws the star with red outline
and yellow filled arms
and the circle with blue outline and cyan fill
"""

from turtle import Turtle, Screen
import math
ANGLE_1 = 144
ANGLE_2 = math.radians(72)
ANGLE_3 = math.radians(54)
t = Turtle()
s = Screen()

def star(distance):
    """
    star part

    key argument:
    distance -- length of star
    """
    t.pencolor("red")
    t.fillcolor("yellow")
    x = distance / 2
    y = (distance * math.cos(ANGLE_2)
         / (2 + 2 * math.cos(ANGLE_2))
         * math.tan(ANGLE_3))
    t.penup()
    t.goto(-x, y) # start point(-x, y)
    t.pendown()

    t.begin_fill()
    for i in range(5):
        t.forward(distance)
        t.right(ANGLE_1)
    t.end_fill()

def circle(distance):
    """
    star part

    key argument:
    distance -- length of star
    """
    t.pencolor("blue")
    t.fillcolor("cyan")

    radius = (distance * math.cos(ANGLE_2)
              / (2 + 2 * math.cos(ANGLE_2))
              * (math.tan(ANGLE_3) + math.tan(ANGLE_2)))

    t.penup()
    t.goto(0, -radius)
    t.pendown()

    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def main():
    s.setup(800, 800)
    circle(500)
    star(500)
    s.mainloop()


main()
