import spotipy
import time
import pandas as pd
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# augment scraped data with spotify api data
load_dotenv()
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def getTrackID(df):
    for i, row in df.iterrows():
        results = sp.search(
            q=f'{row["title"]} artist:{row["artist"]}', type='track', limit=1)

        while 'error' in results.keys():
            print('Rate Limited, waiting 30 seconds...')
            time.sleep(30)
            results = sp.search(
                q=f'{row["title"]} artist:{row["artist"]}', type='track', limit=1)

        if len(results['tracks']['items']) == 0:
            print(f'No results for {row["title"]} by {row["artist"]}')
            continue

        track = results['tracks']['items'][0]
        image = track['album']['images'][0]['url']

        # add spotify data to dataframe
        df.at[i, 'id'] = track['id']
        df.at[i, 'image'] = image

        if i % 100 == 0:
            print(f'{i}/{len(df)}')


df = pd.read_csv('spotify_data_preview.csv')

# cleanup
# df.sort_values(by="streams", ascending=False, inplace=True)
# df.drop_duplicates(subset="id", keep="first", inplace=True)
# df.reset_index(drop=True, inplace=True)

# get preview url
for i, row in df.iterrows():
    print(row['title'], row['artist'])
    track = sp.track(row['id'])

    while 'error' in track.keys():
        print('Rate Limited, waiting 30 seconds...')
        time.sleep(30)
        results = sp.search(
            q=f'{row["title"]} artist:{row["artist"]}', type='track', limit=1)

    preview_url = track['preview_url']
    df.at[i, 'preview_url'] = preview_url

    if i % 10 == 0:
        print(f'{i}/{len(df)}')


df.to_csv('spotify_data_preview.csv', index=False)
