import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Pocket Calculator", "Kraftwerk", "electronic")