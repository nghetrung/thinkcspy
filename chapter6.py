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
        next_point = 'None'
    return next_point

class TestStringMethods(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
