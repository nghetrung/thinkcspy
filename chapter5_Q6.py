# Q6

"""
    Write a function which is given an emarkam mark, and it returns a string — the grade for
    that mark — according to this scheme:
    >= 75   | First
    [70-75) | Upper Second
    [60-70) | Second
    [50-60) | Third
    [45-50) | F1 Supp
    [40-45) | F2
    < 40    | F3
"""

def grade(mark):
    if mark < 40:
        grade = 'F3'
    elif mark >= 40 and mark < 45:
        grade = 'F2'
    elif mark >= 45 and mark < 50:
        grade = 'F1 Supp'
    elif mark >= 50 and mark < 60:
        grade = 'Third'
    elif mark >= 60 and mark < 70:
        grade = 'Second'
    elif mark >= 70 and mark < 75:
        grade = 'Upper Second'
    elif mark >= 75:
        grade = 'First'
    return grade

marks = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in marks:
    print("Student's mark is", i, "with grade:", grade(i))   