import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("electronic")

        self.guest_1 = Guest("Steve")
        self.guest_2 = Guest("Bill")
        self.guest_3 = Guest("Vint")
        self.guest_4 = Guest("Tim")

        self.song_1 = Song("Pocket Calculator", "Kraftwerk", "electronic")
        self.song_1 = Song("Paranoid Android", "Radiohead", "art rock")
        self.song_1 = Song("Saviour Machine", "David Bowie", "rock")

    
    def test_room_has_name(self):
        self.assertEqual("electronic", self.room_1.name)

    
    def test_check_in_guest_to_room(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guest_counter())


    def test_check_out_guest_from_room(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_out_guest(self.guest_1)
        self.assertEqual(2, self.room_1.guest_counter())


    def test_add_song_to_room(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, self.room_1.song_counter())