import unittest

from classes.room import *
from classes.guest import *

class TestRoom(unittest.TestCase): 
    def setUp(self):
        self.room_1 = Room(1)
        self.room_2 = Room(2)
        self.guest_1 = Guest("Bruce", 50)
        self.guest_2 = Guest("Sheila", 75)

    def test_check_room_quantity(self):
        self.assertEqual(0, self.room_1.check_room_quantity())

    def test_check_room_guests(self):
        self.assertEqual([], self.room_1.guests)

    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_2.name)
        self.assertEqual(["Sheila"], self.room_1.guests)

    # def test_check_out_guest(self):
    #     self.guests = [self.guest_2]
    #     self.room_1.check_out_guest(self.guest_2)
    #     self.assertEqual([], self.room_1.guests)
        
    def test_add_song(self):
        self.assertEqual(["I Will Survive"], self.room_1.add_song("I Will Survive"))

