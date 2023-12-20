import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        


def area(a, b):
    '''принимает стороны прямоугольника a и b и считает его площадь'''
    return a * b



def perimeter(a, b):
    '''принимает стороны прямоугольника a и b и считает его периметр'''
    return 2 * (a + b)
