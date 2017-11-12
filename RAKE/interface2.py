from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, END, LEFT, Frame
from shutil import copyfile
from docx_to_txt import docx_to_txt, html_to_txt, rake_classify
import os
from paralleldots import set_api_key, get_api_key, similarity, ner, taxonomy, sentiment, keywords, intent, emotion, multilang, abuse, sentiment_social
#DO NOT randomly test, limited to 100 calls/day, for testing go to: https://www.paralleldots.com/semantic-analysis
# more API examples here: https://github.com/ParallelDots/ParallelDots-Python-API

set_api_key("rjIdkelw0TpgqoMXvVm3GU6ZSmrlIQCawicY5mGyB0I")

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.filePath = ""
        self.input1 = ""
        self.input2 = ""
        self.input3 = ""
        self.dic = ""
        self.charterDir = "../ProjectCharters/"

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

    def getDic(self, path):
        docParse = docx_to_txt(path)
        keyCategoriesDict = docParse.parseDocx()
        return keyCategoriesDict

    def getTextBody(self, dic):
        return dic["Business Need"]

    def findCharter(self):
        text1 = self.getTextBody(self.dic)

        maxScore = 0
        bestCharter = ""
        for filename in os.listdir(self.charterDir):
            if filename[0] == '~':
                continue
            if filename.endswith(".docx"):
                filepath = self.charterDir + filename
                dic = self.getDic(filepath)
                text2 = self.getTextBody(dic)
                scoreDic = similarity(text1, text2)
                score = scoreDic["actual_score"]
                print(type(score))
                print(score, " ", filename)
                print("--------")
                if score > maxScore:
                    maxScore = score
                    bestCharter = filename

        return bestCharter
                
    def uploadFile(self):
        cwd = os.getcwd()
        filename = filedialog.askopenfilename()
        copyfile(filename, cwd+"/test.docx")
        self.filePath = cwd+"/test.docx"

        self.dic = self.getDic(self.filePath)
        keyCategoriesDict = self.dic
        for key,value in keyCategoriesDict.items():
            strPrint = str(key) + '->' + str(value)
            print(strPrint)

        cwd = os.getcwd()
        r = rake_classify(cwd+"/output.txt")
        r.extractKeywords()

        text = self.getTextBody(self.dic)
        print(text)
        print("----------")
        charterName = self.findCharter()
        print(charterName)

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
