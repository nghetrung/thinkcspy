# Q10
""" 
    Write a function find_hypot which, given the length of two sides of a right-angled
    triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square
    root.) 
"""

def find_hyplot(s1, s2):
    l_hypot = (s1**2 + s2**2)**0.5
    return l_hypot

s1 = int(input('What is the length of the first side?: '))
s2 = int(input('What is the length of the second side?: '))
print('The length of the hypotenuse is:', find_hyplot(s1, s2))