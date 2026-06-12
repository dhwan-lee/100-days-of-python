import os
from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic

# Optional Troubleshooting Step - Check for browser.json before doing anything else
if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
response = requests.get(url=URL, headers=header)
# print(response.raise_for_status)

soup = BeautifulSoup(response.text, "html.parser")
song_name_spans = soup.select("li ul li h3")
# print(song_name_spans)
song_names = [song.getText().strip() for song in song_name_spans]
# print(song_names)

yt = YTMusic("browser.json")
# playlists = yt.get_library_playlists()
# print(f"Found {len(playlists)} playlists in your library.")

# Create a playlist
PLAYLIST_NAME = f"{date} Billboard 100"
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if PLAYLIST_NAME == p["title"]:
        playlist_id = p["title"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )

    print("playlist created.")

# Search and add songs to the playlist
for song in song_names:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        # print(search_results)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")