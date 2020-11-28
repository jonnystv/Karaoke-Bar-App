import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Pocket Calculator", "Kraftwerk", "electronic")


    def test_song_has_title(self):
        self.assertEqual("Pocket Calculator", self.song_1.title)


    def test_song_has_artist(self):
        self.assertEqual("Kraftwerk", self.song_1.artist)


    def test_song_has_genre(self):
        self.assertEqual("electronic", self.song_1.genre)