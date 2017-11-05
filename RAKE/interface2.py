from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, END, LEFT, Frame
from shutil import copyfile
from docx_to_txt import docx_to_txt, html_to_txt, rake_classify
import os

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.filePath = ""
        self.input1 = ""
        self.input2 = ""
        self.input3 = ""

        master.title("Big Brother")

        self.label1 = Label(master, text="Choose file to upload")
        self.label1.pack()

        self.browse_button = Button(master, text="Browse for file", command=self.uploadFile)
        self.browse_button.pack()

        frameTop = Frame(master)
        frameTop.pack()

        frameBottom = Frame(master)
        frameBottom.pack()
        self.label2 = Label(frameTop, text="Input Project Type")
        self.label2.pack(side= LEFT)
        self.v1 = StringVar()
        e1 = Entry(frameBottom, textvariable=self.v1)
        e1.delete(0, END)
        e1.pack(side=LEFT)


        self.label3 = Label(frameTop, text="Input Department/Function")
        self.label3.pack(side = LEFT)
        self.v2 = StringVar()
        e2 = Entry(frameBottom, textvariable=self.v2)
        e2.delete(0, END)
        e2.pack(side= LEFT)

        self.label4 = Label(frameTop, text="Input Operating Company")
        self.label4.pack(side = LEFT)
        self.v3 = StringVar()
        e3 = Entry(frameBottom, textvariable=self.v3)
        e3.delete(0, END)
        e3.pack(side= LEFT)

        self.confirm_button = Button(master, text="Confirm", command=self.confirmText)
        self.confirm_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def uploadFile(self):
        cwd = os.getcwd()
        filename = filedialog.askopenfilename()
        copyfile(filename, cwd+"/test.docx")
        self.filePath = cwd+"/test.docx"

        docParse = docx_to_txt(self.filePath)
        keyCategoriesDict = docParse.parseDocx()
        for key,value in keyCategoriesDict.items():
            strPrint = str(key) + '->' + str(value)
            print(strPrint)

        cwd = os.getcwd()
        r = rake_classify(cwd+"/output.txt")
        r.extractKeywords()

    def confirmText(self):
        self.inputText1 = self.v1.get()
        print(self.inputText1)
        self.inputText2 = self.v2.get()
        print(self.inputText2)
        self.inputText3 = self.v3.get()
        print(self.inputText3)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
