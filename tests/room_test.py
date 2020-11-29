import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("electronic")
        self.room_2 = Room("art rock")

        self.guest_1 = Guest("Steve")
        self.guest_2 = Guest("Bill")
        self.guest_3 = Guest("Vint")
        self.guest_4 = Guest("Tim")
        self.guest_5 = Guest("Ada")
        self.guest_6 = Guest("Grace")

        self.song_1 = Song("Pocket Calculator", "Kraftwerk", "electronic")
        self.song_2 = Song("Paranoid Android", "Radiohead", "art rock")
        self.song_3 = Song("Saviour Machine", "David Bowie", "rock")
        self.song_4 = Song("Daisy", "HAL9000", "electronic")
        self.song_5 = Song("Satellite of Love", "Lou Reed", "art rock")
        self.song_6 = Song("Cannonball", "The Breeders", "rock")

        #Create lists to use for PDA requirements
         
        self.list_of_guests = [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5, self.guest_6]

        self.list_of_songs = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5, self.song_6]
         
    #Second Tests

    def test_add_guests_from_list(self):
        self.room_2.check_in_guests_from_list(self.list_of_guests[])
        self.assertEqual(1, self.room_2.guest_counter())
    
    #First Tests Below
    
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