from PyPDF2 import PdfFileReader, PdfFileWriter

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from os import remove, rename


def Fragen():
    global Eingabe
    Eingabe = input("Bitte geben Sie 'read' oder 'write' oder 'exit' ein: ")
    if Eingabe != "exit":
        global pfad
        Tk().withdraw()
        pfad = askopenfilename(filetypes=[('PDF-Dateien', '.pdf'), ('PDF-Dateien', '.PDF')])

Fragen()

while True:
    if Eingabe == "read":
        file = PdfFileReader(pfad)


        def read_meta(path):
            with open(path, 'rb') as _in:
                pdf = PdfFileReader(_in)
                global meta
                meta = pdf.getDocumentInfo()
                global pages
                pages = pdf.getNumPages()


        if file.isEncrypted:
            print("Bitte entschlüsseln Sie das PDF")
            Fragen()
        else:
            read_meta(pfad)


        print(meta)
        print("Seitenanzahl:",pages)
        Fragen()


    elif Eingabe == "write":
        file = PdfFileReader(pfad)


        def write_meta(full_path, metadata):
            filename = full_path.split('/')[-1]
            path = full_path.replace(filename, '')
            writer = PdfFileWriter()
            tmp = f'{path}tmp.{filename}'
            with open(tmp, 'wb') as out:
                with open(full_path, 'rb') as pdf_in:
                    pdf = PdfFileReader(pdf_in)
                    for page in range(pdf.getNumPages()):
                        writer.addPage(pdf.getPage(page))
                        writer.write(out)
                    writer.addMetadata(metadata)
                    writer.write(out)
            remove(full_path)
            rename(tmp, path + filename)

        metadata = {
            '/Title' : '',
            '/Subject' : '',
            '/Author' : '',
            '/Creator' : '',
            '/Producer' : '',
            '/CreationDate' : '',
            '/ModDate' : ''
        }

        if file.isEncrypted:
            print("Bitte entschlüsseln Sie das PDF")
            Fragen()
        else:
            write_meta(pfad, metadata)

    elif Eingabe == "exit":
        exit(0)
        exit(0)
    else:
        print("Bitte geben Sie einen gültigen Wert an!")
        Fragen()
