# import sqlite
import sqlite3

#import tkinter packages
import tkinter         # The GUI package
from tkinter import *  #for widgets
import tkinter.messagebox as tkm   # for message box
# from tkinter.ttk import * # to replace tk widgets with ttk widgets  (CAUSED A BIG ERROR)

# create database test.db
conn = sqlite3.connect('test.db') 
print('databse created successfully')

#create cursor
cur=conn.cursor()

# /*# create table
# cur.execute('''CREATE TABLE stocks
# (date text,
# trans text,
# symbol text,
# price real); ''')

# # save the changes by commit
# conn.commit()
# print(cur.fetchall())
# conn.close()*/

#GUI window using tkinter
# tkWindow = Tk()     #for button's new page (CREATED EXCEPTION IN TKINTER CALLBACK)
class Mainfile:

    def __init__(self,master):
        self.master=master

        #frame creation in master
        self.left = Frame(master, width=800, height=720, bg='pink')
        self.left.pack(side=LEFT)
        self.right=Frame(master, width=800, height=720, bg='white')
        self.right.pack(side=RIGHT)
        #HEADING
        self.heading=Label(self.left, text="Know Your Disease",font=('Helvica 60 bold'),fg='white',bg='black')
        self.heading.place(x=0,y=0)

        #username
        self.name=Label(self.left,text="Username",font=('arial 18 bold'),fg='white',bg='black')
        self.name.place(x=50,y=200)
        #password of patient
        self.password=Label(self.left,text="Password",font=('arial 18 bold'),fg='white',bg='black')
        self.password.place(x=50,y=250)

        #labels to accept entry
        self.nameEntry=Entry(self.left,width=50)
        self.nameEntry.place(x=250,y=210)

        self.passwordEntry=Entry(self.left,width=10)
        self.passwordEntry.place(x=250,y=260)

        #creating a button
        #login button
        self.done=Button( self.left,text='Login',width=20,height=3,bg='white',command=self.addAppointment)
        self.done.place(x=250,y=300)

        #new user button
        self.done=Button(self.left , text = 'New User?',width=20,height=3,bg='white',command=self.newpage) 
        self.done.place(x=50,y=300)
        
    
    def addAppointment(self):
        
        self.x1=self.nameEntry.get()
        self.x2=self.passwordEntry.get()
        conn.execute(sqlite3,(self.x1,self.x2))
        conn.commit()
        print("database retrieval successful")

    # definition for button new user
    def newpage(self):
        self.newWindow= Toplevel(root)
        self.newWindow.title('USER REGISTRATION PORTAL')
        self.newWindow.geometry("1200x720+0+0")
        self.newWindow= Label(self.newWindow,  text="Enter All The Details",font=('Helvica 40 bold'),fg='white',bg='black')
        self.newWindow.place(x=0,y=0)   
        

        

#objects
root=Tk()   # creates a tk object
b=Mainfile(root)
root.geometry("1200x720+0+0")  # creates geometry of main window
root.resizable(False,False)
root.mainloop()





