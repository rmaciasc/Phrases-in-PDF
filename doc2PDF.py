import os
import time
from docx2pdf import convert
import comtypes.client


dir = os.getcwd()
dir = os.path.join(dir, 'CNDH')
print(dir)    


word2 = comtypes.client.CreateObject('Word.Application')
word2.Visible = False
start_time = time.time()

for foldername, subfolders, files in os.walk(os.path.join(dir)):
    for file in files:
        object = os.path.join(foldername, file)
        if object.endswith('.docx'):
            i = object.split("\\")[-1]
            print('\nConvirtiendo archivo: ' + i)
            convert(object) 
            os.remove(object)
        elif object.endswith('.doc'):
            i = object.split("\\")[-1]
            print('Convirtiendo archivo: ' + i)
            newName = object.replace('.doc', '.pdf')
            doc = word2.Documents.Open(object)
            doc.SaveAs(newName, FileFormat = 17)
            doc.Close()
            os.remove(object)
            time.sleep(2)
word2.Quit()

print("--- %s seconds ---" % (time.time() - start_time))

