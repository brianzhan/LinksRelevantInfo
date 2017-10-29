from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, END
from shutil import copyfile
import os

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.filePath = ""
        self.url = ""
        
        master.title("Big Brother")

        self.label1 = Label(master, text="Choose file to upload")
        self.label1.pack()

        self.browse_button = Button(master, text="Browse for file", command=self.uploadFile)
        self.browse_button.pack()

        self.label2 = Label(master, text="Input website url")
        self.label2.pack()
        self.v = StringVar()
        e = Entry(master, textvariable=self.v)
        e.delete(0, END)
        e.pack()
        
        self.confirm_button = Button(master, text="Confirm", command=self.confirmUrl)
        self.confirm_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def uploadFile(self):
        cwd = os.getcwd()
        filename = filedialog.askopenfilename()
        copyfile(filename, cwd+"/test.txt")
        self.filePath = filename

    def confirmUrl(self):
        self.url = self.v.get()
        

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
