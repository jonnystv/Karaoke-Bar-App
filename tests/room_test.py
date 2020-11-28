import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Electronic")