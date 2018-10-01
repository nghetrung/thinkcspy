#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:13:39 2018

@author: MAC
"""

# Chapter 4: FUNCTION

# Q1
import turtle

def create_window_and_turtle(wcolor, tcolor, pensz, title):
    # Create the window
    wn = turtle.Screen()
    wn.bgcolor(wcolor)
    wn.title(title)
    
    # Create a turtle
    t = turtle.Turtle()
    t.color(tcolor)
    t.pensize(pensz)
    
    return t, wn

'''def draw_square(turtle, length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    
def draw_5_square(wcolor, tcolor, sz, pensz, title):
    """
      Draw 5 same size square on 1 line
    """
    # Create the window
    wn = turtle.Screen()
    wn.bgcolor(wcolor)
    wn.title(title)
    
    # Create a turtle
    t = turtle.Turtle()
    t.color(tcolor)
    t.pensize(pensz)
    
    # Drawing
    for i in range(5):
        draw_square(t, sz)
        #t.left(0)
        t.penup()
        t.forward(sz*2)
        t.pendown()
    wn.mainloop()
    
draw_5_square('yellow', 'red', 25, 4, '5 Boxes!')

# Q2

def draw_overlap(wcolor, tcolor, sz, pensz, title):
    """ 
      Draw 5 squares inside each other
    """
    # Create the window
    wn = turtle.Screen()
    wn.bgcolor(wcolor)
    wn.title(title)
    
    # Create a turtle
    t = turtle.Turtle()
    t.color(tcolor)
    t.pensize(pensz)
    
    # Drawing
    for i in range(5):
        draw_square(t, sz)
        sz = sz + 20
        t.left(180)
        t.penup()
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.pendown()
draw_overlap('yellow', 'red', 30, 3, 'Targettt!') '''

# Q3

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)
    
'''t, wn = create_window_and_turtle('yellow', 'red', 4, 'POLYMOLY!') 
draw_poly(t, 8, 50)
wn.mainloop()'''

'''
# Q4

def draw_flower(t, sz, nsquares):
    for i in range(nsquares):
        draw_square(t, sz)
        t.left(360 / nsquares)
t, wn = create_window_and_turtle('yellow', 'red', 2, 'POLYMOLY!') 
draw_flower(t, 70, 50)
wn.mainloop()


# Q5

def draw_spiral(t, sz, n, angle):
    for i in range(n):
        t.forward(sz)
        t.right(angle)
        sz = sz + 3
        
t, wn = create_window_and_turtle('yellow', 'red', 2, 'SPIRAL@@@@!') 
t.left(180)
draw_spiral(t, 8, 100, 89)
wn.mainloop()'''


# Q6

'''def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)
    
t, wn = create_window_and_turtle('yellow', 'red', 4, 'IQ-Triangle!') 
draw_equitriangle(t, 50)
wn.mainloop()


# Q7

def sum_to(n): 
    """
        Return the sum of all integer numbers up to and including n
    """
    total = 0
    for i in range(n+1):
        total = total + i
    return total

sum_to(10)


# Q8

def area_of_circle(r):
    pi = 3.14
    area = pi*(r**2)
    return area

print('The area of the circle with is:', area_of_circle(5), 'cm**2') '''  


# Q9

def draw_star(t, sz):
    for i in range(5):
        t.right(144)
        t.forward(sz)
        
def draw_multi_star(t, n):
    for i in range(n):
        draw_star(t, 50)
        t.penup()
        t.forward(250)
        t.right(144)
        t.pendown()
        
        
t, wn = create_window_and_turtle('yellow', 'red', 3, 'Star!') 
draw_multi_star(t, 5)
wn.mainloop()
    
       
        
        