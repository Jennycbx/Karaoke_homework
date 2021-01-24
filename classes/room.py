class Room:

    def __init__(self, capacity):
        self.guests = []
        self.capacity = capacity
        self.songs = []

    def check_room_quantity(self):
        return len(self.guests)
        
    def check_in_guest(self, guest):
        self.guests.append(guest)
        return self.guests
        
    # def check_out_guest(self, guest):
    #     self.guests.remove(guest)
    #     return self.guests

    def add_song(self, song):
        self.songs.append(song)
        return self.songs
        