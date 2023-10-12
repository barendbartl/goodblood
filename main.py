#import psycopg2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont

#connect to database

#gui
root = Tk()
root.title("Good Blood - Donor Management System")
mt_tree = ttk.Treeview(root)
width=1080
height=720
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#functions here

#creates and positions the gui
donInfolbl=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
donInfolbl["font"] = ft
donInfolbl["fg"] = "#333333"
donInfolbl["justify"] = "center"
donInfolbl["text"] = "Donor information"
donInfolbl.place(x=370,y=10,width=340,height=33)

GLabel_676=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
GLabel_676["font"] = ft
GLabel_676["fg"] = "#333333"
GLabel_676["justify"] = "center"
GLabel_676["text"] = "Donor ID"
GLabel_676.place(x=50,y=380,width=55,height=30)

GLabel_706=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
GLabel_706["font"] = ft
GLabel_706["fg"] = "#333333"
GLabel_706["justify"] = "center"
GLabel_706["text"] = "Donor Name"
GLabel_706.place(x=50,y=420,width=77,height=30)

GLabel_579=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
GLabel_579["font"] = ft
GLabel_579["fg"] = "#333333"
GLabel_579["justify"] = "center"
GLabel_579["text"] = "Donor Surname"
GLabel_579.place(x=50,y=460,width=94,height=30)

GLineEdit_933=tk.Entry(root)
GLineEdit_933["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
GLineEdit_933["font"] = ft
GLineEdit_933["fg"] = "#333333"
#GLineEdit_933["justify"] = "center"
#GLineEdit_933["text"] = "Entry"
GLineEdit_933.place(x=180,y=380,width=321,height=30)

GLineEdit_566=tk.Entry(root)
GLineEdit_566["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
GLineEdit_566["font"] = ft
GLineEdit_566["fg"] = "#333333"
#GLineEdit_566["justify"] = "center"
#GLineEdit_566["text"] = "Entry"
GLineEdit_566.place(x=180,y=420,width=643,height=30)

GLineEdit_860=tk.Entry(root)
GLineEdit_860["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
GLineEdit_860["font"] = ft
GLineEdit_860["fg"] = "#333333"
#GLineEdit_860["justify"] = "center"
#GLineEdit_860["text"] = "Entry"
GLineEdit_860.place(x=180,y=460,width=641,height=30)

GLabel_502=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
GLabel_502["font"] = ft
GLabel_502["fg"] = "#333333"
GLabel_502["justify"] = "center"
GLabel_502["text"] = "Donor Blood Type"
GLabel_502.place(x=50,y=500,width=105,height=30)

bloodListBox=tk.Listbox(root)
bloodListBox["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
bloodListBox["font"] = ft
bloodListBox["fg"] = "#333333"
bloodListBox["justify"] = "center"
bloodListBox.place(x=180,y=505,width=319,height=20)
bloodListBox.insert(1,"A positive (A+)")
bloodListBox.insert(2,"A negative (A-)")
bloodListBox.insert(3,"B positive (B+)")
bloodListBox.insert(4,"B negative (B-)")
bloodListBox.insert(5,"AB positive (AB+)")
bloodListBox.insert(6,"AB negative (AB-)")
bloodListBox.insert(7,"O positive (O+)")
bloodListBox.insert(8,"O negative (O-)")

GButton_848=tk.Button(root)
GButton_848["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Arial',size=10)
GButton_848["font"] = ft
GButton_848["fg"] = "#000000"
GButton_848["justify"] = "center"
GButton_848["text"] = "Add"
GButton_848.place(x=50,y=620,width=105,height=35)

GButton_992=tk.Button(root)
GButton_992["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Arial',size=10)
GButton_992["font"] = ft
GButton_992["fg"] = "#000000"
GButton_992["justify"] = "center"
GButton_992["text"] = "Update"
GButton_992.place(x=190,y=620,width=105,height=35)

GButton_80=tk.Button(root)
GButton_80["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Arial',size=10)
GButton_80["font"] = ft
GButton_80["fg"] = "#000000"
GButton_80["justify"] = "center"
GButton_80["text"] = "Delete"
GButton_80.place(x=330,y=620,width=105,height=35)

GButton_579=tk.Button(root)
GButton_579["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Arial',size=10)
GButton_579["font"] = ft
GButton_579["fg"] = "#000000"
GButton_579["justify"] = "center"
GButton_579["text"] = "Search"
GButton_579.place(x=470,y=620,width=105,height=35)

GButton_511=tk.Button(root)
GButton_511["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Arial',size=10)
GButton_511["font"] = ft
GButton_511["fg"] = "#000000"
GButton_511["justify"] = "center"
GButton_511["text"] = "Reset"
GButton_511.place(x=610,y=620,width=105,height=35)

root.mainloop()
