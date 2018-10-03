import unittest

"""
    Functions
"""

# Q1
def turn_clockwise(p):
    next_point = 'None'
    if p == 'N':
        next_point = 'E'
    elif p == 'E':
        next_point = 'S'
    elif p == 'S':
        next_point = 'W'
    elif p == 'W':
        next_point = 'N'
    else:
        next_point = 'None'
    return next_point

# Q2
def day_name(daynum):
    if daynum not in range(7):
        dayname = 'None'
    else:
        if daynum == 0:
            dayname = 'Sunday'
        elif daynum == 1:
            dayname = 'Monday'
        elif daynum == 2:
            dayname = 'Tuesday'
        elif daynum == 3:
            dayname = 'Wednesday'
        elif daynum == 4:
            dayname = 'Thursday'
        elif daynum == 5:
            dayname = 'Friday'
        elif daynum == 6:
            dayname = 'Saturday'
    return dayname

# Q3
def day_num(dayname):
    daynames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if dayname not in daynames:
        daynum = 'None'
    else:
        if dayname == 'Sunday':
            daynum = 0
        elif dayname == 'Monday':
            daynum = 1
        elif dayname == 'Tuesday':
            daynum = 2
        elif dayname == 'Wednesday':
            daynum = 3
        elif dayname == 'Thursday':
            daynum = 4
        elif dayname == 'Friday':
            daynum = 5
        elif dayname == 'Saturday':
            daynum = 6
    return daynum

# Q4
def day_add(dayname, ndays):
    current_day_num = day_num(dayname)
    for i in range(ndays):
        if current_day_num + 1 > 6:
            current_day_num = 0
        else:
            current_day_num = current_day_num + 1
    holiday_day_num = current_day_num
    holiday_day_name = day_name(holiday_day_num)
    return holiday_day_name


"""
    Test cases
"""    

class TestCompass(unittest.TestCase):

    def test_north(self):
        self.assertEqual(turn_clockwise('N'), 'E', 'Next point should be East!')
    def test_east(self):
        self.assertEqual(turn_clockwise('E'), 'S', 'Next point should be South!')
    def test_south(self):
        self.assertEqual(turn_clockwise('S'), 'W', 'Next point should be West!')
    def test_west(self):
        self.assertEqual(turn_clockwise('W'), 'N', 'Next point should be North!')
    def test_none(self):
        self.assertEqual(turn_clockwise('haha'), 'None')


class TestDayName(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(day_name(3), 'Wednesday', '3 should be Wednesday')
        self.assertEqual(day_name(6), 'Saturday', '6 should be Saturday')
    def test_invalid_daynum(self):
        self.assertEqual(day_name(42), 'None')


class TestDayNum(unittest.TestCase):

    def test_general(self):
        self.assertEqual(day_num('Friday'), 5)
        self.assertEqual(day_num('Sunday'), 0)
        self.assertEqual(day_num(day_name(3)), 3)
        self.assertEqual(day_name(day_num('Thursday')), 'Thursday')
        self.assertEqual(day_num('Halloween'), 'None')


class TestDayAdd(unittest.TestCase):

    def test_day_add(self):
        self.assertEqual(day_add('Monday', 4), 'Friday')
        self.assertEqual(day_add('Tuesday', 0), 'Tuesday')
        self.assertEqual(day_add('Tuesday', 14), 'Tuesday')
        self.assertEqual(day_add('Sunday', 100), 'Tuesday')

# Running the tests
if __name__ == '__main__':
    unittest.main()
