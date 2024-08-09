import os
from PyPDF2 import PdfReader, PdfWriter


cwd = os.getcwd()
FILE_PATH_ONE = cwd
FolderName = FILE_PATH_ONE.split("\\")[-1]


Directory = os.listdir(FILE_PATH_ONE)
PDF_File = Directory[0]


print(FILE_PATH_ONE)
print(PDF_File)
print(FolderName)


inputpdf = PdfReader(open(PDF_File, "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open(FolderName + "-%s.pdf" % (i+1), "wb") as outputStream:
        output.write(outputStream)

