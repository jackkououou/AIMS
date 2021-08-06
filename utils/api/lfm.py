import requests


USER_AGENT = 'AIMS'
API_KEY = '8e047dd8d6b487dec2bc5e98e5f67f21'
URL = 'https://ws.audioscrobbler.com/2.0/'

HEADERS = {'user-agent' : USER_AGENT}

def __lastfm_get_call_albuminfo( artist, album):
    #Private method that calls the lastfm api and returns the metadata for the album as a json
    url = URL
        
    payload = {
    'method'    : 'album.getinfo',
    'api_key'   : API_KEY,
    'artist'    : artist,
    'album'     : album,
    'format'    : 'json'
    }
        
    response = requests.get(url, headers=HEADERS, params=payload)
        
    return response.json()
    
def get_track_list(artist, album):
        
    album_json = __lastfm_get_call_albuminfo(artist, album)
    
    #song list
    track_tags_list = album_json['album']['tracks']['track']
    track_list = []
    for track in track_tags_list:
        track_list.append(track['name'])
        
    return track_list

def get_image_url(artist, album):
    album_json = __lastfm_get_call_albuminfo(artist, album)
    #album art url
    #album->image->4th index (largest album art) ->text
    img_url = ''
    img_url = album_json['album']['image'][4]['#text']
    
    return img_url

def get_genre_list(artist, album):
    album_json = __lastfm_get_call_albuminfo(artist, album)
        
    #genre list
    #album->tags->tag->list of names
    genre_tags_list = album_json['album']['tags']['tag']
    genre_list = []
    for tag in genre_tags_list:
        genre_list.append(tag['name'])
            
    return genre_list