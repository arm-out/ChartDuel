import pandas as pd
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


us_clean = us.copy()
us_clean.drop(columns=['genres'], inplace=True)

global_clean = global_df.copy()
global_clean.drop(columns=['genres'], inplace=True)


for i, row in global_df.iterrows():
    if (pd.isnull(row['genres'])):
        continue

    genre_list = getGenre(row['genres'])
    for genre in genre_list:
        global_clean.at[i, genre] = True

    print(f'{i}/{len(global_df)}')

global_clean.to_csv('global_data_clean.csv', index=False)

for i, row in us.iterrows():
    if (pd.isnull(row['genres'])):
        continue

    genre_list = getGenre(row['genres'])
    for genre in genre_list:
        us_clean.at[i, genre] = True

    print(f'{i}/{len(us)}')

us_clean.to_csv('us_data_clean.csv', index=False)
