from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, END
from shutil import copyfile
from docx_to_txt import docx_to_txt, html_to_txt, rake_classify
import os

docParse = docx_to_txt("../ProjectCharters/Project Charter_DivA1.docx")
keyCategoriesDict = docParse.parseDocx()
for key,value in keyCategoriesDict.items():
    strPrint = str(key) + '->' + str(value)
    print(strPrint)

