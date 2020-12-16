import pandas as pd

df = pd.read_csv('./Reshape Resumen.csv')
df['Title'] = df['Title'].replace('_', '-', regex=True)
# df = df[1:]
df

df[['Bando', 'Edo', 'Municipio']] = df.Title.str.split('-', expand = True)
df['Municipio'] = df['Municipio'].replace('.pdf', '', regex = True)

newOrder = list(df)
newOrder.insert(0, newOrder.pop(newOrder.index('Municipio'))) 
newOrder.insert(0, newOrder.pop(newOrder.index('Edo')))
newOrder.insert(0, newOrder.pop(newOrder.index('Bando')))

df = df.loc[:, newOrder].sort_values(['Edo', 'Municipio'], ascending = True)
df.drop(labels='Phrase not found', axis=1, inplace=True)
df
df.to_csv('./Results/Resumen con Edo y Municipio ESTADOS.csv', index=False, encoding='utf-8-sig')