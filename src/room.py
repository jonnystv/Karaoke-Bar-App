class Room:

    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    
    def guest_counter(self):
        return len(self.guests)

    
    def check_in_guest(self, guest):
        self.guests.append(guest)


    def check_out_guest(self, guest):
        self.guests.remove(guest)


    def song_counter(self):
        return len(self.songs)
    
    
    def add_song(self, song):
        self.songs.append(song)