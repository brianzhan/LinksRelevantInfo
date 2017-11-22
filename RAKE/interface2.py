from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, END, LEFT, Frame
from shutil import copyfile
from docx_to_txt import docx_to_txt, html_to_txt, rake_classify
import os
import heapq
from time import sleep
from paralleldots import set_api_key, get_api_key, similarity, ner, taxonomy, sentiment, keywords, intent, emotion, multilang, abuse, sentiment_social
import threading
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
        
        self.type=""
        self.title=""

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

        self.threads = []

    def getDic(self, path):
        docParse = docx_to_txt(path)
        keyCategoriesDict = docParse.parseDocx()
        return keyCategoriesDict

    def getTextBody(self, dic):
        return dic["Business Need"]

    def findCharter(self):
        text1 = self.getTextBody(self.dic)
        
        pq = []
        samecategoryname = []
        samecategorypath = []
        maxScore = 0
        bestCharter = ""
        for filename in os.listdir(self.charterDir):
            if filename[0] == '~':
                continue
            if filename.endswith(".docx"):
                filepath = self.charterDir + filename
                dic = self.getDic(filepath)
                text2 = self.getTextBody(dic)
                print(text2)
                scoreDic = similarity(text1, text2)
                print(scoreDic)
                score = scoreDic["actual_score"]
                print(type(score))
                print(score, " ", filename)
                currname = ""
                keyCategoriesDict = self.getDic(filepath)
                
                for key,value in keyCategoriesDict.items():
                    if str(key)=="Project Title":
                        print(str(value))
                        currname=str(value)
                    if str(key)=="Project Type":
                        if str(value)==self.type and currname!=self.title and filepath!=self.filePath:
                            samecategorypath.append(filepath)
                            samecategoryname.append(currname)
                        break
            
                if currname!=self.title and filepath!=self.filePath:
                    heapq.heappush(pq,(1-score, currname))
                
                print("--------")
                if score > maxScore and currname!=self.title:
                    maxScore = score
                    bestCharter = filename

        
        print("Current Project: ",self.title)
        print("--------")
        print("Here is the list of projects with the same project type:")
        for i in range (0,len(samecategoryname)):
            print("--------")
            print("Project Name: ",samecategoryname[i])
            print(samecategorypath[i])
        print("--------")
        
        
        amount = 3
        if len(pq)<amount:
            amount = len(pq)
        print("Here is the list of similar projects:")
        for i in range (0,amount):
            best = heapq.heappop(pq)
            print("--------")
            print("Project Name: ", best[1])
            print("Percentage of Similarity: ", 1-best[0])
        print("--------")

        return bestCharter

    def recheckFile(self):
        while(True):
            sleep(30)
            charterName = self.findCharter()
            print(charterName)

    #constraint: only one file can be open at a time
    def getOpenFile(self):
        files = os.listdir("~/Users/pierce/Documents/Projects/BigBrother/LinksRelevantInfo/ProjectCharters/")
        file = ""
        for f in files:
            if "~$" in f:
                file = f
                break
        if file != "":
            copyfile(file, os.getcwd()+"/test.docx")
            self.filePath = cwd+"/test.docx"

            self.dic = self.getDic(self.filePath)
            keyCategoriesDict = self.dic
            for key,value in keyCategoriesDict.items():
                strPrint = str(self.cleanUnicode(key)) + '->' + str(self.cleanUnicode(value))
                if(str(key)=="Project Title"):
                    self.title=str(value)
                if(str(key)=="Project Type"):
                    self.type=str(value)
                print(strPrint)

            cwd = os.getcwd()
            r = rake_classify(cwd+"/output.txt")
            r.extractKeywords()

            text = self.getTextBody(self.dic)
            print(text)
            print("----------")
            charterName = self.findCharter()
            print(charterName)
            t = threading.Thread(target=self.recheckFile)
            self.threads.append(t)
            t.start()


    def uploadFile(self):
        cwd = os.getcwd()
        filename = filedialog.askopenfilename()
        copyfile(filename, cwd+"/test.docx")
        self.filePath = cwd+"/test.docx"

        self.dic = self.getDic(self.filePath)
        keyCategoriesDict = self.dic
        for key,value in keyCategoriesDict.items():
            strPrint = str(self.cleanUnicode(key)) + '->' + str(self.cleanUnicode(value))
            if(str(key)=="Project Title"):
                self.title=str(value)
            if(str(key)=="Project Type"):
                self.type=str(value)
            print(strPrint)

        cwd = os.getcwd()
        r = rake_classify(cwd+"/output.txt")
        r.extractKeywords()

        text = self.getTextBody(self.dic)
        print(text)
        print("----------")
        charterName = self.findCharter()
        print(charterName)
        t = threading.Thread(target=self.recheckFile)
        self.threads.append(t)
        t.start()


    def confirmText(self):
        self.inputText1 = self.v1.get()
        print(self.inputText1)
        self.inputText2 = self.v2.get()
        print(self.inputText2)
        self.inputText3 = self.v3.get()
        print(self.inputText3)

    def cleanUnicode(self, str):
        str = str.replace(u'\u2013', '-')
        str = str.replace(u'\u2019', "'")
        str = str.replace(u'\u201c','"')
        str = str.replace(u'\u201d', '"')
        return str


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
