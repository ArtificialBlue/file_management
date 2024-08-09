import os
import pandas as pd

cwd = os.getcwd()
FILE_PATH = cwd
print(FILE_PATH)

dir_list = os.listdir(FILE_PATH)

folderNames = []

for dir in dir_list:
    print(dir)
    folderNames.append(dir)

df = pd.DataFrame(index=folderNames)

print(df, "\n")

df.to_excel('Folders.xlsx')

                     
