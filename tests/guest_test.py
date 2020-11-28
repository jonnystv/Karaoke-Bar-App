import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Steve")


    def test_guest_has_name(self):
        self.assertEqual("Steve", self.guest_1.name)