import pandas as pd

# Obtenemos todos los files
allFiles = pd.read_csv('./File Names.csv')
print(allFiles)

fitz = pd.read_csv('./Results/Bandos Resultados Fitz Text.csv')
print(fitz)

summary = pd.merge(allFiles, fitz, how= 'left')
summary

summary.to_csv('./Resumen.csv', encoding='utf-8-sig', index=False)