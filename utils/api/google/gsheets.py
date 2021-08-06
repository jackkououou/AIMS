import gspread
from utils.Album import Album
from gspread.models import Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("utils\\api\\google\\credentials.json", scope)
DRIVE = 'albumTEMP'
SHEET = 'Sheet1'

class gsheet():
    
    
    def __init__(self):
        self.client = gspread.authorize(CREDS)
        self.inventory = self.client.open(DRIVE).worksheet(SHEET)
        self.inv_extract = self.inventory.get_all_values()
    
    #return list with album data, if not found return empty list
    
    def get_album(self, title, artist):
        
        for row in self.inv_extract:
            if((title in row ) and (artist in row)):
                return row
        
        return []
    
    def add_album(self, title, artist):
        new_album = Album(artist_in=artist, album_in=title)
        value = [new_album.get_album_title, new_album.get_album_artist, new_album.get_genres, new_album.get_tracks]
        #Check if already in inv
        clear = True
        for row in self.inv_extract:
            if((title in row) and (artist in row)):
                clear = False
                break
        if clear:
            self.inv_extract.append(value)
            
    def remove_album(self, title, artist):
        self.inventory.ro
                
        
        
    
        
    
        


    
    

