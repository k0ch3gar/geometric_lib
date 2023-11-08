import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
       
    def test_float_mul(self):
        self.assertEqual(area(12.4, 2.5), float(31))
        
    def test_zero_per_mul(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)
        
    def test_square_per_mul(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
       
    def test_float_per_mul(self):
        self.assertEqual(perimeter(12.4, 2.5), 29.8)


def area(a, b):
    '''принимает стороны прямоугольника a и b и считает его площадь'''
    return a * b



def perimeter(a, b):
    '''принимает стороны прямоугольника a и b и считает его периметр'''
    return 2 * (a + b)
