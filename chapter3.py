#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:45:36 2018

@author: MAC
"""

# 3.1 Our first turtle program

import turtle

bg_color = input('What color do you want for the background? ')
alex_color = input('What color do you want for Alex? ')
size = int(input("What pen's size do you want? "))


wn = turtle.Screen()
wn.bgcolor(bg_color)
wn.title('Hello, Alex!')

alex = turtle.Turtle()
alex.color(alex_color)
alex.pensize(size)

alex.forward(50)
alex.left(90)
alex.forward(30)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(30)

wn.mainloop()

# Q7

wn = turtle.Screen()
wn.bgcolor('yellow')
wn.title('Hello, Alex!')

alex = turtle.Turtle()
alex.color('red')
alex.pensize(3)

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    alex.forward(100)
    alex.right(i)
wn.mainloop()  

# Q9

wn = turtle.Screen()
wn.bgcolor('yellow')
wn.title('Hello, Alex!')

alex = turtle.Turtle()
alex.color('red')
alex.pensize(3)

for i in range(18):
    alex.forward(70)
    alex.left(20)
wn.mainloop()


# Q11

import turtle
wn = turtle.Screen()
wn.bgcolor('yellow')
wn.title('Hello, Alex!')

alex = turtle.Turtle()
alex.color('red')
alex.pensize(3)

alex.left(72)
for i in range(5):
    alex.forward(70)
    alex.right(144)

alex.left(180)
alex.penup()
alex.forward(90)
alex.right(180)
alex.pendown()
for i in range(5):
    alex.forward(70)
    alex.right(144)
wn.mainloop()


# Q12
import turtle
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Hello, Alex!')

alex = turtle.Turtle()
alex.color('blue')
alex.penup()
for i in range(12):
    alex.forward(100)
    alex.stamp()
    alex.backward(100)
    alex.right(30)
wn.mainloop()

##
import turtle

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smallest square
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10 # Increase the size for next time
    tess.forward(10) # Move tess along a little
    tess.right(18) # and give her some turn

wn.mainloop()
      