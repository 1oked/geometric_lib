import unittest

def area(a, b): 
    ''' Возвращает плошадь прямоугольника со сторонами a и b '''
    return a * b 

def perimeter(a, b): 
    ''' Возвращает периметр прямоугольника со сторонами a и b '''
    return (a + b) * 2 


class RectangleTestCase(unittest.TestCase):
    def test_zero_mult(self):
        res = area(15, 0)
        self.assertEqual(res, 0)
    
    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_rectangle_area(self):
        res = area(5, 8)
        self.assertEqual(res, 40)

    def test_square_perimeter(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_rectangle_perimeter(self):
        res = perimeter(7, 8)
        self.assertEqual(res, 30)