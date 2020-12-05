import os
import pandas as pd

dir = os.getcwd()
dir = os.path.join(dir, 'CNDH')
dir

dic = {
    "Title": [],
}

for foldername, subfolders, files in os.walk(os.path.join(dir)):
    for file in files:
        # print(file)
        dic['Title'].append(file)

fileNames = pd.DataFrame(dic)
fileNames.to_csv('./File Names.csv', index=False, encoding='utf-8-sig')