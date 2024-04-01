import unittest
from app import *
class BasicsTests(unittest.TestCase):

    def test_number_of_food_groups(self):
        self.assertEqual(number_of_food_groups(), 5)

    def test_number_of_books_on_hold(self):
        self.assertEqual(number_of_books_on_hold(), 5)

    def test_number_of_fingers(self):
        self.assertEqual(number_of_fingers(), 5)

    def test_number_of_great_lakes(self):
        self.assertEqual(number_of_great_lakes(), None)