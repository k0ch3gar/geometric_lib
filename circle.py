import math
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_area_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
        
    def test_square_area_mul(self):
        res = area(10)
        self.assertEqual(res, math.pi * 100)
       
    def test_float_area_mul(self):
        self.assertEqual(area(2 / (math.pi ** 0.5)), float(4))
        
    def test_zero_per_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        
    def test_square_per_mul(self):
        res = perimeter(10)
        self.assertEqual(res, math.pi * 20)
       
    def test_float_per_mul(self):
        self.assertEqual(perimeter(2 / math.pi), float(4))



def area(r):
    '''принимает радиус круга r и считает его площадь'''
    return math.pi * r * r


def perimeter(r):
    '''принимает радиус круга r и считает длину его окружности'''
    return 2 * math.pi * r
