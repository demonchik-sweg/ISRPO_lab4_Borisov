import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_unit(self):
        self.assertAlmostEqual(area(1), math.pi, places=5)

    def test_area_radius_10(self):
        self.assertAlmostEqual(area(10), math.pi * 100, places=5)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_unit(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=5)

    def test_perimeter_radius_10(self):
        self.assertAlmostEqual(perimeter(10), 20 * math.pi, places=5)


if __name__ == '__main__':
    unittest.main()