import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Bruce", 50)
        self.guest_2 = Guest("Sheila", 75)

