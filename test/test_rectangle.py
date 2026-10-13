import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_zero_both(self):
        self.assertEqual(area(0, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_rect(self):
        self.assertEqual(area(5, 7), 35)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_rect(self):
        self.assertEqual(perimeter(5, 7), 24)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(4, 4), 16)


if __name__ == '__main__':
    unittest.main()