import pandas as pd

df = pd.read_csv('./Resumen.csv')
df.Title.nunique()

df['Page'] = df['Page'].fillna(0)
# df['Phrase'] = df['Phrase'].fillna('Phrase not found').reset_index()
df['Phrase'].fillna("Phrase not found", inplace=True)
df
df['Page'] = df['Page'].astype(int).astype(str)
df.Title.nunique()

df = df.groupby(['Title', 'Phrase'])['Page'].apply(','.join).reset_index()
df
df.Title.nunique()

df = df.pivot(index='Title', columns= 'Phrase', values='Page')
df = df.fillna(0).reset_index()

df.to_csv('./Reshape Resumen.csv', index = False, encoding = 'utf-8-sig')