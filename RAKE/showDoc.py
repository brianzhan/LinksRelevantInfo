from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, END, LEFT, Frame
from shutil import copyfile
import os
import heapq
from paralleldots import set_api_key, get_api_key, similarity, ner, taxonomy, sentiment, keywords, intent, emotion, multilang, abuse, sentiment_social
import threading
from PIL import ImageTk, Image
import subprocess
import threading
from time import sleep
from evaluateFile import evaluateFile
#DO NOT randomly test, limited to 100 calls/day, for testing go to: https://www.paralleldots.com/semantic-analysis
# more API examples here: https://github.com/ParallelDots/ParallelDots-Python-API

class MyFirstGUI:
    def createImage(self, frame, openfile):
        filename = 'charter.png'
        img = Image.open(filename)
        w, h = img.size

        frame2 = Frame(frame)
        frame2.pack(side=LEFT)
        img = img.resize((round(w*0.2), round(h*0.2)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(frame2, image = img)
        panel.image = img
        panel.pack()

        self.openfile = "../ProjectCharters/" + openfile
        btn = Button(frame2, text=openfile, command=self.openDoc)
        btn.pack()

    def openDoc(self):
        subprocess.call(['open', self.openfile])

    def __init__(self, master):
        self.master = master
        self.filePath = ""
        self.dic = ""
        self.charterDir = "../ProjectCharters/"
        
        self.type=""
        self.title=""

        master.title("Big Brother")
        self.master = master
        self.GUILoop()

    def printGUI(self, similar, category):
        master = self.master
        master.geometry("1000x1000")
        master.resizable(width=True, height=True)
        
        self.label1 = Label(master, text="Other Projects of Type X:")
        self.label1.pack()
        
        topFrame = Frame(master)
        topFrame.pack()

        l = len(category)
        l = min(l, 5)
        for i in range(l):
            self.createImage(topFrame, category[i])

        self.label2 = Label(master, text="Similar Projects:")
        self.label2.pack()
    
        bottomFrame = Frame(master)
        bottomFrame.pack()
        for i in range(len(similar)):
            self.createImage(bottomFrame, similar[i])

    def clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()
    
    def refreshGUI(self):
        while (True):
            self.clear()
            ev = evaluateFile()
            similarCharters, sameCategory = ev.getOpenFile()
#            similarCharters = ["Project Charter_DivA2.docx"]
#           sameCategory = []
            self.printGUI(similarCharters, sameCategory)
            self.notify(title    = 'Big Brother',
                       subtitle = 'Similar Project Charters',
                       message  = 'Found project charters similar to what you are working on! Click here to find out more!',
                       execute = 'python showDoc.py',
                       activate = 'com.apple.Terminal')
            sleep(100)

    def notify(self, title, subtitle, message,execute,activate):
        t = '-title {!r}'.format(title)
        s = '-subtitle {!r}'.format(subtitle)
        m = '-message {!r}'.format(message)
        e = '-execute {!r}'.format(execute)
        a = '-activate {!r}'.format(activate)

        os.system('terminal-notifier {}'.format(' '.join([m, t, s, e, a])))
        
    def GUILoop(self):
        t = threading.Thread(target=self.refreshGUI)
        t.start()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
#my_gui.getOpenFile()
