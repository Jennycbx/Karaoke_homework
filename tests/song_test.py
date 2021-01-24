import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("I Will Survive")
        self.song_2 = Song("Unstoppable")

