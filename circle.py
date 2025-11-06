import math
import unittest
import functions as f


def area(r):
    ''' Возвращает площадь круга с радиусом r '''
    if not f.IsNumber(r):
        return 0
    return math.pi * r * r


def perimeter(r):
    ''' Возвращает длину окружности с радиусом r '''
    if not f.IsNumber(r):
        return 0
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        res = area(3)
        self.assertEqual(res, math.pi * 9)

    def test_radius_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_circle_perimeter(self):
        res = perimeter(4)
        self.assertEqual(res, math.pi * 8)

    def test_radius_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_not_a_number(self):
        res = perimeter("not a number")
        self.assertEqual(res, 0)