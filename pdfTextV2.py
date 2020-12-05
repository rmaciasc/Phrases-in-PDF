import fitz
import os
import pandas as pd

frases = ['derechos humanos', 
'Derecho a una vida libre de violencia',
'Igualdad entre mujeres y hombres', 'Igualdad entre hombres y mujeres', 
'personas con discapacidad', 'discapacitados', 'con alguna discapacidad', 'personas con capacidades diferentes', 'inválidos', 
'comunidades indígenas', 'pueblos indígenas', 'personas indígenas', 'indígena',
'derechos de adultos mayores', 'personas de la tercera edad', 'ancianos', 
'niñas, niños', 'adolescentes', 'niñez', 'menores de edad', 
'igualdad de género', 'equidad de género', 'perspectiva de género', 
'mujer', 'mujeres']
dir = os.getcwd()
dir = os.path.join(dir, 'CNDH')
dir

dic = {
    "Title": [],
    "Page": [],
    "Phrase": []
}
dic

errorsDic = []

for foldername, subfolders, files in os.walk(os.path.join(dir)):
    for file in files:
        try:
            object = fitz.open(os.path.join(foldername, file))
            i = 0
            print(file)
            for page in object:
                # text = page.getText('text')
                # text = text.replace('\n', '')
                i += 1
                for frase in frases:
                    if page.searchFor(frase):
                        print('Pattern ' + frase.upper() + ' found on page: ' + str(i))
                        dic['Title'].append(file)
                        dic['Page'].append(i)
                        dic['Phrase'].append(frase.upper())
        except:
            errorsDic.append(file)
            pass

# dic
df = pd.DataFrame(dic)
df

errorsDF = pd.DataFrame(errorsDic)

df.to_csv('./Results/Bandos Resultados Fitz Text.csv', index=False, encoding= 'utf-8-sig')
errorsDF.to_csv('./Results/Errores Bandos Fitz Text.csv', index=False, encoding= 'utf-8-sig')