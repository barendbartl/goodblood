import psycopg2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#connect to database

#gui
root = Tk()
root.title("Good Blood - Donation Management System")
root.geometry("1080x720")
mt_tree = ttk.Treeview(root)

#functions here

#more gui
label=Label(root,text="Welcome to Good Blood", font=('Arial Bold',30))
label.grid(row=0, column=1,columnspan=8,rowspan=2, pady=40)

patfnameLabel=Label(root,text="First Name",font=('Arial',15))
patlnameLabel=Label(root,text="Surname",font=('Arial',15))
patidLabel=Label(root,text="Patient ID",font=('Arial',15))
pataddressLabel=Label(root,text="Address",font=('Arial',15))
patphoneLabel=Label(root,text="Phone",font=('Arial',15))

patfnameLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
patlnameLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
patidLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
pataddressLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
patphoneLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)

patfnameInput=Entry(root,width=55,bd=5,font=('Arial', 15))
patlnameInput=Entry(root,width=55,bd=5,font=('Arial', 15))
patidInput=Entry(root,width=55,bd=5,font=('Arial', 15))
pataddressInput=Entry(root,width=55,bd=5,font=('Arial', 15))
patphoneInput=Entry(root,width=55,bd=5,font=('Arial', 15))

patfnameInput.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
patlnameInput.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
patidInput.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
pataddressInput.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
patphoneInput.grid(row=7,column=1,columnspan=4,padx=5,pady=0)

addBtn=Button(
    root,text="Add", padx=65,pady=25,width=10,bd=5,font=('Arial',15)
)
updateBtn=Button(
    root,text="Update", padx=65,pady=25,width=10,bd=5,font=('Arial',15)
)
deleteBtn=Button(
    root,text="Delete", padx=65,pady=25,width=10,bd=5,font=('Arial',15)
)
searchBtn=Button(
    root,text="Search", padx=65,pady=25,width=10,bd=5,font=('Arial',15)
)
resetBtn=Button(
    root,text="Reset", padx=65,pady=25,width=10,bd=5,font=('Arial',15)
)
selectBtn=Button(
    root,text="Select", padx=65,pady=25,width=10,bd=5,font=('Arial',15)
)

addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

root.mainloop()

