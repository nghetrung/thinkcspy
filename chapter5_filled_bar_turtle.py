#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 09:27:23 2018

@author: MAC
"""

# Chapter 5 - Conditionals

# 5.12
import turtle
xs = [-48, 117, 200, 240, 160, 260, 220]

def create_window_and_turtle(wcolor, tcolor, fillcolor, pensz, title):
    # Create the window
    wn = turtle.Screen()
    wn.bgcolor(wcolor)
    wn.title(title)

    # Create a turtle
    t = turtle.Turtle()
    t.color(tcolor, fillcolor)
    t.pensize(pensz)

    return t, wn

def draw_bar(t, height):
    if height < 0:
        t.begin_fill()
        t.left(90)
        t.forward(height)
        t.penup()
        t.forward(-20)
        t.write('  ' + str(height), font=("Arial", 12, "normal"))
        t.forward(20)
        t.pendown()
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(10)
        t.pendown()
    else:
        t.begin_fill()
        t.left(90)
        t.forward(height)
        t.write('  ' + str(height), font=("Arial", 12, "normal"))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(10)
        t.pendown()

tess, wn = create_window_and_turtle('hotpink', 'green', 'yellow', 3, 'BAR!')

tess.left(180)
tess.penup()
tess.forward(200)
tess.right(180)
tess.pendown()

for v in xs:
    if v >= 200:
        tess.color('green', 'red')
    elif v >= 100 and v < 200:
        tess.color('green', 'yellow')
    else:
        tess.color('green', 'green')
    draw_bar(tess, v)
wn.mainloop()


# Q8

"""
    Modify the turtle bar chart program so that the bar for any value of 200 or more is filled
    with red, values between [100 and 200) are filled with yellow, and bars representing
    values less than 100 are filled with green.
"""

# Q9

"""
    In the turtle bar chart program, what do you expect to happen if one or more of the data
    values in the list is negative? Try it out. Change the program so that when it prints the
    text value for the negative bars, it puts the text below the bottom of the bar
"""