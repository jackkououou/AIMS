from utils.Album import Album
from utils.api.google.gsheets import Gsheet

testsheet = Gsheet()
title = ['Igor', 'Bucket List Project', 'Sax Pax For A Sax']
artist = ['tyler, the creator', 'Saba', 'Moondog']

for index, rec in enumerate(title):
    testsheet.add_album(rec, artist[index])

testsheet.update_sheets()
print(testsheet.get_album(title, artist))

