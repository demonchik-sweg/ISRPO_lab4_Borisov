import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_base(self):
        self.assertEqual(area(0, 10), 0)

    def test_area_zero_height(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_simple(self):
        self.assertEqual(area(4, 6), 12)

    def test_area_float(self):
        self.assertAlmostEqual(area(3, 7), 10.5, places=5)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_simple(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(perimeter(5, 5, 5), 15)


if __name__ == '__main__':
    unittest.main()