import unittest
import functions as f

def area(a, h): 
    ''' Возвращает площадь треугольника
        с высотой h и длиной стороны a '''
    if not f.IsNumber(a) or not f.IsNumber(h):
        return 0
    
    return a * h / 2 

def perimeter(a, b, c): 
    ''' Возвращает периметр треугольника со сторонами a, b и c '''
    if not f.IsNumber(a) or not f.IsNumber(b) or not f.IsNumber(c):
        return 0
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_trangle_area(self):
        res = area(5, 8)
        self.assertEqual(res, 20)
    
    def test_triangle_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_height_zero_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_not_a_number(self):
        res = perimeter("not", "a", "number")
        self.assertEqual(res, 0)