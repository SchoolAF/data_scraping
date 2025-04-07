import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_custom_Android_distributions'
tables = pd.read_html(url, match='Name')

df = tables[0]
print(df.head())

df.to_csv('custom_roms.csv', index=False)
print("Saved as 'custom_roms.csv'")