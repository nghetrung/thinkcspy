#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:49:01 2018

@author: MAC
"""

# Q5

p = 10000
n = 12
r = 8
t = int(input('How many years will the money be compounded for?: '))
total_amount = p * ((1 + r/n) ** (n*t))
print('The final amount is: $', total_amount, sep = '')


# Q7
''' You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At
what time does the alarm go off? '''

hour = 2
at = 'pm'
counter = 0
time_remaining = 51
for i in range(1, 52):
    if hour == 12:
        hour = 0
        counter = counter + 1
        hour = hour + 1
    else:
        hour = hour + 1
if counter%2 == 0:
    at = 'pm'
else:
    at = 'am'
print('Time at the moment is:', hour, at)

# Q8 (General version of Q7)

time_now = input('What time is it? ')
hour = int(time_now[0])
at = time_now[1] + time_now[2]
wait = int(input('How many hours do u want until the alarm goes off? '))
counter = 0
for i in range(1, wait+1):
    if hour == 12:
        hour = 0
        counter = counter + 1
        hour = hour + 1
    else:
        hour = hour + 1
if counter%2 == 0:
    at = at
else:
    if at == 'am':
        at = 'pm'
    else:
        at = 'am'
print('Time at the moment is:', hour, at)
