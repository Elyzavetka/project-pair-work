class MusicTracker():
    # User-facing properties:
    #//As a user
    # We can keep track of my music listening
    # I want to add tracks I've listened to and see a list of them.
    #   

    def __init__(self):
        self.music_list = []
        # Parameters:
        #   No
        # Side effects:
        #   We create self.music_list attribute


    def add(self, song):
        # Parameters:
        #   song: representing a song
        # Returns:
        #   Nothing
        # Side-effects
        #   Adds the song to the music list
        self.music_list.append(song) 
        

    def show_music_list(self):
        # Returns:
        #   Songs list
        # Side-effects:
        return self.music_list
        