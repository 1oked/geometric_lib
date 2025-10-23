import unittest

def area(a):
    ''' Возвращает площадь квадрата со стороной a '''
    return a * a


def perimeter(a):
    ''' Возвращает периметр квадрата со стороной a '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        res = area(8)
        self.assertEqual(res, 64)
    
    def test_square_perimeter(self):
        res = perimeter(7)
        self.assertEqual(res, 28)
    
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
