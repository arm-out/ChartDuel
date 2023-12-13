import pandas as pd
import numpy as np
import json

us = pd.read_csv('us_data.csv')
global_df = pd.read_csv('global_data.csv')

# us_genres = {}
# global_genres = {}

# for i, row in us.iterrows():
#     if (pd.isnull(row['genres'])):
#         continue

#     genres = row['genres'].split(',')
#     for genre in genres:
#         if genre in us_genres:
#             us_genres[genre] += 1
#         else:
#             us_genres[genre] = 1

# for i, row in global_df.iterrows():
#     if (pd.isnull(row['genres'])):
#         continue
#     genres = row['genres'].split(',')
#     for genre in genres:
#         if genre in global_genres:
#             global_genres[genre] += 1
#         else:
#             global_genres[genre] = 1

# # sort dictionaries by value
# us_genres = dict(
#     sorted(us_genres.items(), key=lambda item: item[1], reverse=True))
# global_genres = dict(
#     sorted(global_genres.items(), key=lambda item: item[1], reverse=True))

# with open('us_genres.json', 'w') as f:
#     json.dump(us_genres, f)

# with open('global_genres.json', 'w') as f:
#     json.dump(global_genres, f)


def getGenre(genres):

    genre_set = set()
    for genre in genres.split(','):
        current = set()
        if 'rap' in genre.lower() or 'hip hop' in genre.lower() or 'r&b' in genre.lower() or 'drill' in genre.lower():
            current.add('rap')
        if 'pop' in genre.lower() and 'k-pop' not in genre.lower():
            current.add('pop')
        if 'rock' in genre.lower() or 'metal' in genre.lower():
            current.add('rock')
        if 'country' in genre.lower():
            current.add('country')
        if 'edm' in genre.lower() or 'electro' in genre.lower() or 'house' in genre.lower() or 'techno' in genre.lower() or 'dance' in genre.lower():
            current.add('edm')
        if 'latin' in genre.lower() or 'reggae' in genre.lower() or 'argentino' in genre.lower() or 'espanol' in genre.lower():
            current.add('latin')
        if 'k-pop' in genre.lower() and genre.lower() != 'folk-pop':
            current.add('kpop')

        if 'pop' in current and 'kpop' in current:
            current.remove('pop')
        if 'pop' in current and 'latin' in current:
            current.remove('pop')

        genre_set = genre_set.union(current)

    return list(genre_set)


# us_clean = us.copy()
# us_clean.drop(columns=['genres'], inplace=True)

# global_clean = global_df.copy()
# global_clean.drop(columns=['genres'], inplace=True)


for i, row in global_df.iterrows():
    if (row['latin'] == True):
        global_df.at[i, 'rap'] = np.nan
        global_df.at[i, 'rock'] = np.nan
        global_df.at[i, 'country'] = np.nan
        global_df.at[i, 'edm'] = np.nan
        global_df.at[i, 'kpop'] = np.nan
        global_df.at[i, 'pop'] = np.nan
    elif (row['kpop'] == True):
        global_df.at[i, 'rap'] = np.nan
        global_df.at[i, 'rock'] = np.nan
        global_df.at[i, 'country'] = np.nan
        global_df.at[i, 'edm'] = np.nan
        global_df.at[i, 'latin'] = np.nan
        global_df.at[i, 'pop'] = np.nan

    if i % 1000 == 0:
        print(f'{i}/{len(global_df)}')

global_df.to_csv('global_data_clean.csv', index=False)

for i, row in us.iterrows():
    if (row['latin'] == True):
        us.at[i, 'rap'] = np.nan
        us.at[i, 'rock'] = np.nan
        us.at[i, 'country'] = np.nan
        us.at[i, 'edm'] = np.nan
        us.at[i, 'kpop'] = np.nan
        us.at[i, 'pop'] = np.nan
    elif (row['kpop'] == True):
        us.at[i, 'rap'] = np.nan
        us.at[i, 'rock'] = np.nan
        us.at[i, 'country'] = np.nan
        us.at[i, 'edm'] = np.nan
        us.at[i, 'latin'] = np.nan
        us.at[i, 'pop'] = np.nan

    if i % 1000 == 0:
        print(f'{i}/{len(global_df)}')

us.to_csv('us_data_clean.csv', index=False)
