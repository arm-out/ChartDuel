import spotipy
import time
import pandas as pd
import numpy as np
import json
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# augment scraped data with spotify api data
load_dotenv()

scope = 'user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


us = pd.read_csv('us_spotify_clean.csv')
global_df = pd.read_csv('global_spotify_previews.csv')

# us cleanup
# count = 0
# for i, row in us.iterrows():
#     if pd.isnull(us.at[i, 'id']):
#         global_row = global_df.loc[(global_df['title'] ==
#                                    row['title']) & (global_df['artist'] == row['artist'])]
#         if len(global_row) != 0:
#             count += 1
#             row['id'] = global_row['id'].values[0]
#             row['image'] = global_row['image'].values[0]
#             # print(row)
#             # print(global_row)

# print(count)
# print(us.shape[0])
# us.dropna(subset=['id'], inplace=True)
# us.reset_index(drop=True, inplace=True)
# print(us.shape[0])

# us.sort_values(by="streams", ascending=False, inplace=True)
# us.drop_duplicates(subset="id", keep="first", inplace=True)
# us.reset_index(drop=True, inplace=True)

# print(us.shape[0])
# us.to_csv('us_spotify_clean.csv', index=False)


# for i, row in df.iterrows():
#     results = sp.search(
#         q=f'{row["title"]} artist:{row["artist"]}', type='track', limit=1)

#     if len(results['tracks']['items']) == 0:
#         print(f'No results for {row["title"]} by {row["artist"]}')
#         continue

#     track = results['tracks']['items'][0]
#     image = track['album']['images'][0]['url']

#     # add spotify data to dataframe
#     df.at[i, 'id'] = track['id']
#     df.at[i, 'image'] = image

#     if i % 100 == 0:
#         print(f'{i}/{len(df)}')

# df.to_csv('us_spotify_data.csv', index=False)


# create list of tracks
tracks = []
for i, row in us.iterrows():
    tracks.append(row['id'])

# get audio features
for i in range(0, len(tracks), 50):
    results = sp.tracks(tracks[i:i+50])

    for j, track in enumerate(results['tracks']):
        us.at[i+j, 'preview'] = track['preview_url']
        us.at[i+j, 'popularity'] = track['popularity']
        us.at[i+j, 'url'] = track['external_urls']['spotify']
        us.at[i+j, 'release_date'] = track['album']['release_date']

    print(f'{i}/{len(tracks)}')

us.to_csv('us_spotify_previews.csv', index=False)
