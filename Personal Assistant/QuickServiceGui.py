from Tkinter import *
from ttk import *
import tkMessageBox




class QuickService  :
    def __init__(self):
        self.window=Tk()

        self.window.title("QuickService")
        self.keywordLabel=Label(self.window,text='Keyword     : ')
        self.descriptionLabel=Label(self.window,text='Description : ')
        self.insertBtn=Button(self.window, text="Cancel")
        self.cancelBtn=Button(self.window, text="Add")
        self.entry=Entry(self.window,width=40)
        self.entry2=Entry(self.window,width=40)
    def insertQuickServiceTOFile(self):
        openFile = open("quickservicedataset", "a")
        openFile.write(self.entry.get()+"|"+self.entry2.get()+"\n")

        # readFromFile = open("/home/abdo/PycharmProjects/new_Gui_Project/quickservicedataset", "r")

        # for line in readFromFile:
        #     if line.split()[0]==keyword:
        #         pass
        openFile.close()
        self.entry.delete(0,END)
        self.entry2.delete(0, END)

    def QS(self):
        self.keywordLabel.grid(row=0, column=0, sticky='snew', padx=10, pady=10)
        self.descriptionLabel.grid(row=1,column=0,sticky='snew',padx=10,pady=10)

        self.entry.grid(row=0, column=1, sticky='snew')
        self.entry2.grid(row=1, column=1, sticky='snew')
        self.insertBtn.grid(row=2, column=0, padx=10, pady=10)
        self.cancelBtn.grid(row=2, column=1, padx=10, pady=10)
        self.insertBtn.config( command=lambda :self.insertQuickServiceTOFile())
        self.cancelBtn.config(command=lambda :self.insertQuickServiceTOFile())
        self.window.mainloop()




#





