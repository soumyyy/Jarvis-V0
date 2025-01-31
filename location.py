import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

os.environ["SPOTIPY_CLIENT_ID"] = "fc14267db73a4147bf273c346e4c8de1"
os.environ["SPOTIPY_CLIENT_SECRET"] = "8e01ca88d16348f595540b5431b7b0c9"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"

scope = "user-read-playback-state,user-modify-playback-state,streaming"

sp = Spotify(auth_manager=SpotifyOAuth(scope=scope))

def play_music(song_name, laptop_device_id):
    """Play a song on a specific Spotify device (e.g., a laptop)."""
    # Search for the song
    results = sp.search(q=song_name, limit=1, type='track')
    tracks = results.get('tracks', {}).get('items', [])
    if not tracks:
        print(f"No track found for: {song_name}")
        return
    track_uri = tracks[0]['uri']
    sp.start_playback(device_id=laptop_device_id, uris=[track_uri])
    print(f"Playing: {tracks[0]['name']} by {tracks[0]['artists'][0]['name']} on your laptop")

laptop_device_id = '1c7dfad65289ab2e1f2848ddc9e83c02695cf02a'
play_music("Stand Off", laptop_device_id)




def list_spotify_devices():
    """List available Spotify devices and print their IDs."""
    devices = sp.devices().get('devices', [])
    if not devices:
        print("No active Spotify devices found.")
    else:
        for device in devices:
            print(f"{device['name']} ({device['type']}), ID: {device['id']}")