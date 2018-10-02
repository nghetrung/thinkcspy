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


# Q11, 12
"""
    Write a function is_rightangled which, given the length of three sides of a triangle,
    will determine whether the triangle is right-angled. Assume that the third argument to
    the function is always the longest side. It will return True if the triangle is right-angled,
    or False otherwise.
"""

def is_rightangled(s1, s2, s3):
    if s1**2 == (s2**2 + s3**2) or s2**2 == (s1**2 + s3**2) or s3**2 == (s1**2 + s2**2):
        return True
    return False

is_rightangled(5, 2, 4)