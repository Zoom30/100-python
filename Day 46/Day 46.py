from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import api_keys

time_to_travel = "2015-01-30"

#input("What year do you want to travel? Type in the following format: YYYY-MM-DD \n")
url = f"https://www.billboard.com/charts/hot-100/{time_to_travel}"

response = requests.get(url=url)
bp_web_page = response.text
soup = BeautifulSoup(bp_web_page, "html.parser")


all_names = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = [song.getText() for song in all_names]
sample_song = song_names[0]
# print(song_names)



x = SpotifyOAuth(scope="playlist-modify-private", client_id=api_keys.spotifyOAuth_client_id, client_secret=api_keys.spotifyOAuth_client_secret, redirect_uri="http://example.com", cache_path="token.txt")

sp = spotipy.Spotify(auth_manager=x)


user_id = sp.current_user()["id"]


song_uri = []
year = time_to_travel.split("-")[0]
for song in song_names:
    r = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = r["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesnt exist in spotify, skipped")


playlist = sp.user_playlist_create(user=user_id, name=f"{time_to_travel} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)

