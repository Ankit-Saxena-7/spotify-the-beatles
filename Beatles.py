import os
import sys
import spotipy
import spotipy.util as util

# AUTHENTICATION STEPS - START

# Fetch username from terminal

vUserName = sys.argv[1]

# User ID: iul1yva60hzzajvq39ijgefku?si=e-OGLhgbT1OAcitL9xvaVw

# Erase cache and prompt for user permission

try:
    vToken = util.prompt_for_user_token(vUserName)
except:
    os.remove(f".cache)-{vUserName}")
    vToken = util.prompt_for_user_token(vUserName)

# Spotify object
vSpotifyObj = spotipy.Spotify(auth=vToken)

# AUTHENTICATION STEPS - END



# WHERE THE FUN BEGINS

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))

vBeatlesURI = 'spotify:artist:3WrFJ7ztbogyGnTHbHJFl2'

vResults = vSpotifyObj.artist_albums(vBeatlesURI, album_type='album')
vAlbums = vResults['items']
while vResults['next']:
    vResults = vSpotifyObj.next(vResults)
    vAlbums.extend(vResults['items'])

for vAlbum in vAlbums:
    print(vAlbum['name'])
