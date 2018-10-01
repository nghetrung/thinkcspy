# Q1

"""
Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write
a function which is given the day number, and it returns the day name (a string).
"""

def day_name(day):
    if day not in range(7):
        print('Day is not existed!')
    else:
        if day == 0:
            dayname = 'Sunday'
        elif day == 1:
            dayname = 'Monday'
        elif day == 2:
            dayname = 'Tuesday'
        elif day == 3:
            dayname = 'Wednesday'
        elif day == 4:
            dayname = 'Thursday'
        elif day == 5:
            dayname = 'Friday'
        elif day == 6:
            dayname = 'Saturday'
    return dayname

print('Today is', day_name(3))

# Q2

"""
You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving
on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general
version of the program which asks for the starting day number, and the length of your
stay, and it will tell you the name of day of the week you will return on.
"""

start_day_num = int(input('What is your start day number?: '))
print('You leave on', day_name(start_day_num))
day_num = start_day_num
stay_length = int(input('What is the length of your stay?: '))
week = 0

for i in range(stay_length):
    if day_num > 6:
        day_num = 0
    day_num = day_num + 1
    if day_num == start_day_num:
        week = week + 1

current_day_name = day_name(day_num)
print('You will return on', current_day_name, 'in', week, 'weeks')kbkasf
