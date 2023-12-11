import pandas as pd

# scrape table
df = pd.read_html(
    'https://kworb.net/spotify/country/us_daily_totals.html')[0]
cleaned = pd.DataFrame(columns=['title', 'artist', 'streams'])

for i, row in df.iterrows():
    print(i, row['Artist and Title'])
    # skip rows with no artist/title
    if i in [6113, 6899, 7968, 9105] or row['Artist and Title'].startswith('Various Artists'):
        continue

    artist = row['Artist and Title'].split(' - ', 1)[0]
    title = row['Artist and Title'].split(' - ', 1)[1]
    streams = row['Total']

    temp = pd.DataFrame({'title': [title], 'artist': [
                        artist], 'streams': [streams]})
    cleaned = pd.concat([cleaned, temp], ignore_index=True)

    if i == 10000:
        break

print(cleaned)
cleaned.to_csv('us_data.csv', index=False)
