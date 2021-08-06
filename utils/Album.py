from .api import lfm

class Album:
    
    
    #So when the album is created Artist and Album are entered for initializtion
    #After that the object passes Art and Alb to the lastfm api the get genre list, song list, and album art
    def __init__(self, artist_in, album_in):
        self.artist = artist_in
        self.album_name = album_in
        self.image_url = lfm.get_image_url(artist_in, album_in)
        self.genre_list = lfm.get_genre_list(artist_in, album_in)
        self.track_list = lfm.get_track_list(artist_in, album_in)
        
    #HERE place alternate __init__ here for reading off the database

    def get_art(self):
        return self.image_url
    
    def get_tracks(self):
        return self.track_list
    
    def get_genres(self):
        return self.genre_list
    
    def get_album_artist(self):
        return self.artist
    
    def get_album_title(self):
        return self.album_name

    
