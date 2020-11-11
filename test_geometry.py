import math
import unittest

from geometry import Circle


class MyTestCase(unittest.TestCase):
    def test_circle_creation(self):
        circ_string = str(Circle(5.2))
        self.assertGreaterEqual(circ_string.find("5.2"), 0)

    def test_circle_area(self):
        circ = Circle(1)
        self.assertEqual(math.pi, circ.area())

