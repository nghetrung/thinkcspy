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
    # for i in range(ndays):
    #     if current_day_num + 1 > 6:
    #         current_day_num = 0
    #     else:
    #         current_day_num = current_day_num + 1
    holiday_day_num = current_day_num + ndays
    holiday_day_name = day_name(holiday_day_num % 7)
    return holiday_day_name

# Q6
def days_in_month(month_name):
    if month_name not in['January', 'February', 'March', 'April', 
                        'May', 'June', 'July', 'August', 'September', 
                        'October', 'November', 'December']:
        ndays = 'None'
    else:
        if month_name in['January', 'March', 'May', 'July', 'August', 'October', 'December']:
            ndays = 31
        elif month_name == 'February':
            ndays = 28
        else:
            ndays = 30
    return ndays

# Q7, 8
def to_secs(hours, minutes, seconds):
    total_second = hours*60*60 + minutes*60 + seconds
    return int(total_second)

# Q9
# part a
def hours_in(tsec):
    hours = tsec//3600
    return hours
# part b
def minutes_in(tsec):
    minutes = (tsec - hours_in(tsec)*3600)//60
    return minutes
# part c
def seconds_in(tsec):
    seconds = tsec - hours_in(tsec)*3600 - minutes_in(tsec)*60
    return seconds

# Q13, 14
def slope(x1, y1, x2, y2):
    slope = (y2-y1)/(x2-x1)
    return slope

def intercept(x1, y1, x2, y2):
    intercept = y1 - slope(x1, y1, x2, y2)*x1
    return intercept

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
    def test_day_add_negative(self):
        self.assertEqual(day_add('Sunday', -1), 'Saturday')
        self.assertEqual(day_add('Sunday', -7), 'Sunday')
        self.assertEqual(day_add('Tuesday', -100), 'Sunday')


class TestDayInMonths(unittest.TestCase):

    def test_days_in_month(self):
        self.assertEqual(days_in_month('February'), 28)
        self.assertEqual(days_in_month('March'), 31)
        self.assertEqual(days_in_month('April'), 30)
        self.assertEqual(days_in_month('Februaryy'), 'None')

class TestToSecs(unittest.TestCase):

    def test_to_secs(self):
        self.assertEqual(to_secs(2, 30, 10), 9010)
        self.assertEqual(to_secs(2, 0, 0), 7200)
        self.assertEqual(to_secs(0, 2, 0), 120)
        self.assertEqual(to_secs(0, 0, 42), 42)
        self.assertEqual(to_secs(0, -10, 10), -590)
    def test_to_secs_float(self):
        self.assertEqual(to_secs(2.5, 0, 10.71), 9010)
        self.assertEqual(to_secs(2.433, 0, 0), 8758)


class TestInverseToSecs(unittest.TestCase):

    def test_inverse_tosecs(self):
        self.assertEqual(hours_in(9010), 2)
        self.assertEqual(minutes_in(9010), 30)
        self.assertEqual(seconds_in(9010), 10)

class TestIntercept(unittest.TestCase):

    def test_intercept(self):
        self.assertEqual(intercept(1, 6, 3, 12), 3.0)
        self.assertEqual(intercept(6, 1, 1, 6), 7.0)
        self.assertEqual(intercept(4, 6, 12, 8), 5.0)

# Running the tests
if __name__ == '__main__':
    unittest.main()
