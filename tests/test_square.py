import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_unit(self):
        self.assertEqual(area(1), 1)

    def test_area_10(self):
        self.assertEqual(area(10), 100)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_unit(self):
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_10(self):
        self.assertEqual(perimeter(10), 40)


if __name__ == '__main__':
    unittest.main()