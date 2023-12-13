import spotipy
import time
import pandas as pd
import numpy as np
import json
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = 'user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

us = pd.read_csv('us_spotify_previews.csv')
global_df = pd.read_csv('global_spotify_previews.csv')

artistGLOBAL = []
artistUS = []
for i, row in global_df.iterrows():
    artistGLOBAL.append(row['artistId'])
for i, row in us.iterrows():
    artistUS.append(row['artistId'])

for i in range(0, len(artistGLOBAL), 50):
    results = sp.artists(artistGLOBAL[i:i+50])

    for j, artist in enumerate(results['artists']):
        global_df.at[i+j,
                     'genres'] = ','.join(genre for genre in artist['genres'])

    print(f'{i}/{len(artistGLOBAL)}')

global_df.to_csv('global_data.csv', index=False)

for i in range(0, len(artistUS), 50):
    results = sp.artists(artistUS[i:i+50])

    for j, artist in enumerate(results['artists']):
        us.at[i+j, 'genres'] = ','.join(genre for genre in artist['genres'])

    print(f'{i}/{len(artistUS)}')

us.to_csv('us_data.csv', index=False)
