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


class evaluateFile:
    def __init__(self):
        self.charterDir = "../ProjectCharters/"

    def cleanUnicode(self, str):
        str = str.replace(u'\u2013', '-')
        str = str.replace(u'\u2019', "'")
        str = str.replace(u'\u201c', '"')
        str = str.replace(u'\u201d', '"')
        return str

    def recheckFile(self):
        while (True):
            sleep(30)
            charterName = self.findCharter()
            print(charterName)

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
        bestCharters = []
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

                for key, value in keyCategoriesDict.items():
                    if str(key) == "Project Title":
                        print(str(value))
                        currname = str(value)
                    if str(key) == "Project Type":
                        if str(value) == self.type and currname != self.title and filepath != self.filePath:
                            samecategorypath.append(filename)
                            samecategoryname.append(currname)
                        break

                if currname != self.title and filepath != self.filePath:
                    heapq.heappush(pq, (1 - score, filename))

                print("--------")
                if score > maxScore and currname != self.title:
                    maxScore = score
                    bestCharter = filename
        for i in range(3):
            f2 = heapq.heappop(pq)
            bestCharters.append(f2[1])
        return bestCharters, samecategorypath
            

    def getOpenFile(self):
        wd = self.charterDir
        files = os.listdir(wd)
        file = ""
        fsuff = ""

        for f in files:
            if "~$" in f:
                fsuff = f[2:]
                break
        for f in files:
            if fsuff in f and "~$" not in f:
                file = f
                break
    
        if file != "":
            copyfile(wd + file, os.getcwd()+"/test.docx")
            self.filePath = os.getcwd() + "/test.docx"
            self.dic = self.getDic(self.filePath)
            keyCategoriesDict = self.dic
            for key, value in keyCategoriesDict.items():
                strPrint = str(self.cleanUnicode(key)) + '->' + str(self.cleanUnicode(value))
                if (str(key) == "Project Title"):
                    self.title = str(value)
                if (str(key) == "Project Type"):
                    self.type = str(value)
                print(strPrint)

            cwd = os.getcwd()
            r = rake_classify(cwd + "/output.txt")
            r.extractKeywords()

            text = self.getTextBody(self.dic)
            print(text)
            print("----------")
            return self.findCharter()
            
