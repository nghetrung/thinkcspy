import unittest

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
        print('Argument is not valid!')
    return next_point

class TestStringMethods(unittest.TestCase):

    def test_north(self):
        self.assertEqual(turn_clockwise('N'), 'E')
    def test_east(self):
        self.assertEqual(turn_clockwise('E'), 'A', 'WRONGGGG')
    def test_south(self):
        self.assertEqual(turn_clockwise('S'), 'N')

if __name__ == '__main__':
    unittest.main()
