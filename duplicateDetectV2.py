import os

FILE_PATH_ONE = ""
cwd = os.getcwd()
firstInput = input("Do you want the first directory to be the Current Folder: \n" + cwd + " ?(Y/N)")
print("firstInput:" + firstInput)

if firstInput.upper() == "Y":
    FILE_PATH_ONE = cwd
else:
    FILE_PATH_ONE = input("Please provide Full Filepath for First folder: ")

FILE_PATH_TWO = input("Please provide Full Filepath for Second folder: ")


largerDirectory = os.listdir(FILE_PATH_ONE)
smallerDirectory = os.listdir(FILE_PATH_TWO)

largerList = []
duplicatesList = []


outputFile = open("duplicates.txt","a")



for entry in largerDirectory:
    if "(" in entry:
        trimmedEntry = entry[:entry.index('(')]
        if not (trimmedEntry in largerList):
            largerList.append(trimmedEntry)
            #print(trimmedEntry)
#print(largerList)
            
for entry in smallerDirectory:
    trimmedEntry = entry[:entry.index('(')]
    if trimmedEntry in largerList:
        if not (trimmedEntry in duplicatesList):
            print("Duplicate: " + trimmedEntry)
            duplicatesList.append(trimmedEntry)
            outputFile.write(trimmedEntry + "\n")



outputFile.close()
