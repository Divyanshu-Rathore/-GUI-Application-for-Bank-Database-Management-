#imports Libraries
from tkinter import *
import os
import image

from tkinter import Entry, IntVar, Tk
from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter.ttk import Combobox


#Main Screen of GUI
master = Tk()
master.title('Bank Management System')

#Import image from folder

#img = Image.open('SBI.png')
#img = img.resize((150,150))
#img = ImageTk.PhotoImage(img)

img = PhotoImage(file = r"C:\Users\asus\Documents\Placement\Bank database managment system\SBI.png")

#Labels


#Functions

def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg = "red", text= "All fields are required *")
        return
     
    print ("good to go mate")

def register():

    global temp_name 
    global temp_age
    global temp_gender 
    global temp_password
    global notif



    
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    #Labels
    Label(register_screen, text="Please enter your details below to register", font=('Calibri',12)).place(row=0, sticky=N, pady=10)
    Label(register_screen, text="Name", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=('Calibri',12)).grid(row=2, sticky=W)
    Label(register_screen, text="Gender", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=('Calibri',12)).grid(row=4, sticky=W)
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=6, sticky=N, pady=10)
    #Entries
    Entry(register_screen, textvariable=temp_name).grid(row= 1,column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0)
    #Buttons
    Button(register_screen, text="Register", command = finish_reg, font=('Calibri',12)).grid(row=5, sticky=N, pady=10)



def login():
    print("This is login page")







Label(master, text = "State Bank of India", font =('Calibri',14) ).place(x=700, y=18)
Label(master, text = "SBI is the most secure bank you've probably used", font=('Calibri',12)).place(x =700, y = 40)
Label(master, image=img).place(x =500,y = 80 )

Label(master, text = "Select Features", font =('Calibri',14) ).place(x=30, y=300)

Label(master, text = "Display: ", font =('Calibri',14) ).place(x=150, y=400)


lps = ttk.Combobox(master, width = 27)
  
B_LPS = ['Bank details','Customer Details','Loan Details', 'Empolyee Details','deposit Details']

# Adding combobox drop down list
lps['values'] = B_LPS

lps.place(x= 300, y= 400)
lps.current()




#Buttons
#Button(master, text="Register", font=('Calibri',12),width=20, command =register).place(x=600, y = 300)
#Button(master, text="Login", font=('Calibri',12),width=20, command=login).place(x=600, y = 380)

master.mainloop()
