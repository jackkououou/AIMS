import gspread
from utils.Album import Album
from gspread.models import Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("utils\\api\\google\\credentials.json", SCOPE)
DRIVE = 'albumTEMP'
SHEET = 'Sheet1'


class Gsheet():
    
    
    def __init__(self):
        self.client = gspread.authorize(CREDS)
        self.inventory = self.client.open(DRIVE).worksheet(SHEET)
        self.inv_extract = self.inventory.get_all_values()
    
    def refresh(self):
        self.inv_extract = self.inventory.get_all_values()
            
    #return list with album data, if not found return empty list
    def get_album(self, title, artist):
        for row in self.inv_extract:
            if((title in row ) and (artist in row)):
                str_to_list = row[2]
                row[2] =  list(str_to_list.split("*!*"))
                str_to_list = row[3]
                row[3] =  list(str_to_list.split("*!*"))
                return row
        
        return []
    
    #Appends the album to the end of the inventory.
    #When adding to Google Sheets string and int and floats are really the only safe option so any list has to be converted into a string
    #Genre and Track are converted to string with '*!*' used to flag where the sticthes are to seperated them later
    def add_album(self, title, artist):
        new_album = Album(artist_in=artist, album_in=title)
        genre_str = '*!*'.join(new_album.get_genres())
        track_str = '*!*'.join(new_album.get_tracks())
        value = [new_album.get_album_title(), new_album.get_album_artist(), genre_str, track_str, new_album.get_art() , 0, 0, 0]
        
        #Check if already in inv
        clear = True
        for row in self.inv_extract:
            if((title in row) and (artist in row)):
                clear = False
                break
        if clear:
            self.inv_extract.append(value)
            
    def remove_album(self, title, artist):
        
        line = 1
        found = False
        for row in self.inv_extract:
            if(title in row ) and (artist in row ):
                found = True
                break
            else:
                line += 1
                
        if found:
            self.inventory.delete_row(line)
            
    #Changes made to inv_ext are merged into the sheets page
    def update_sheets(self):
        for row_index, row in enumerate (self.inv_extract):
            for col_index, col in enumerate (row):
                print(col)
                self.inventory.update_cell(row_index + 1, col_index + 1, col)
                
         
    
        
    
        


    
    

