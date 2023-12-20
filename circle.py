import math
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_area_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
        



def area(r):
    '''принимает радиус круга r и считает его площадь'''
    return math.pi * r * r


def perimeter(r):
    '''принимает радиус круга r и считает длину его окружности'''
    return 2 * math.pi * r
