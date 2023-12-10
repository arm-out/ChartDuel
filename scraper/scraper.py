import pandas as pd

# scrape table
df = pd.read_html(
    'https://kworb.net/spotify/country/global_daily_totals.html')[0]
cleaned = pd.DataFrame(columns=['title', 'artist', 'streams'])

for i, row in df.iterrows():
    # skip rows with no artist/title
    if i in [4612, 5280, 5923, 7243, 7467] or row['Artist and Title'].startswith('Various Artists'):
        continue

    artist = row['Artist and Title'].split(' - ', 1)[0]
    title = row['Artist and Title'].split(' - ', 1)[1]
    streams = row['Total']

    temp = pd.DataFrame({'title': [title], 'artist': [
                        artist], 'streams': [streams]})
    cleaned = pd.concat([cleaned, temp], ignore_index=True)

print(cleaned)
cleaned.to_csv('data.csv', index=False)
