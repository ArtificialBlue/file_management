import os
import re


cwd = os.getcwd()
FILE_PATH = cwd
print(FILE_PATH)


dir_list = os.listdir(FILE_PATH)

for dir in dir_list:
    regexNumber = re.compile("[0-9 ]+\s") #Matches for Any number of digits followed by a space
    print(dir)
    NumMatch = regexNumber.match(dir)
    print(type(NumMatch))
    if not(NumMatch is None):
        print(NumMatch.group())
        print(dir[len(NumMatch.group()):])
        newName = dir[len(NumMatch.group()):] + " (" + NumMatch.group()[:-1] + ")"
        print(newName)
        try:
            os.rename(FILE_PATH + "/" + dir, FILE_PATH + "/" + newName)
        except OSError as exc:
            print(exc)


                     
