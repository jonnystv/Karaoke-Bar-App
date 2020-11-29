import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Steve")
        self.guest_2 = Guest("Bill")
        self.guest_3 = Guest("Vint")
        self.guest_4 = Guest("Tim")


    def test_guest_has_name(self):
        self.assertEqual("Steve", self.guest_1.name)