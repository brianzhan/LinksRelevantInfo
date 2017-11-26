from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, END, LEFT, Frame
from shutil import copyfile
import os
import heapq
from paralleldots import set_api_key, get_api_key, similarity, ner, taxonomy, sentiment, keywords, intent, emotion, multilang, abuse, sentiment_social
import threading
from PIL import ImageTk, Image
import subprocess
#DO NOT randomly test, limited to 100 calls/day, for testing go to: https://www.paralleldots.com/semantic-analysis
# more API examples here: https://github.com/ParallelDots/ParallelDots-Python-API

class MyFirstGUI:
    def createImage(self, frame, openfile):
        filename = 'charter.png'
        img = Image.open(filename)
        w = 766
        h = 998
        frame2 = Frame(frame)
        frame2.pack(side=LEFT)
        img = img.resize((round(w*0.2), round(h*0.2)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(frame2, image = img)
        panel.image = img
        panel.pack()

        self.openfile = openfile
        btn = Button(frame2, text="open", command=self.openDoc)
        btn.pack()

    def openDoc(self):
        subprocess.call(['open', self.openfile])

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

      
        self.label1 = Label(master, text="Other Projects of Type X:")
        self.label1.pack()
        
        
        topFrame = Frame(master)
        topFrame.pack()
 
        master.geometry("1000x1000")
        master.resizable(width=True, height=True)
        #master.configure(background = 'grey')
        self.createImage(topFrame, "charter1.docx")     
        self.createImage(topFrame, "charter1.docx")
        self.createImage(topFrame, "charter1.docx")

        self.label2 = Label(master, text="Similar Projects:")
        self.label2.pack()
    
        bottomFrame = Frame(master)
        bottomFrame.pack()
        self.createImage(bottomFrame, "charter1.docx")
        self.createImage(bottomFrame, "charter1.docx")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
#my_gui.getOpenFile()
