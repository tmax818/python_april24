import unittest
from app import *


class MyTestCase(unittest.TestCase):
    def test_x(self):
        self.assertEqual(x, [[5, 2, 3], [15, 8, 9]])

    def test_students(self):
        self.assertEqual(students[0]['last_name'], "Bryant")

    def test_sports_directory(self):
        self.assertEqual(sports_directory['soccer'][0], 'Andres')

    def test_z(self):
        self.assertEqual(z, [{'x': 10, 'y': 30}])


if __name__ == '__main__':
    unittest.main()
