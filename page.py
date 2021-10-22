# import sqlite
import sqlite3

#import tkinter packages
import tkinter                                                       # The GUI package
from tkinter import *                                                #for widgets
import tkinter.messagebox as tkm
from typing import NewType                                           # for message box
from PIL import ImageTk, Image                                       # import pillow for image files
# from tkinter.ttk import *                                          # to replace tk widgets with ttk widgets  (CAUSED A BIG ERROR)

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

# tkWindow = Tk()                                                     #for button's new page (CREATED EXCEPTION IN TKINTER CALLBACK)
class Mainfile:

    def __init__(self,master):
        self.master=master

        #frame creation in master
        self.left = Frame(master, width=800, height=720, bg='#B3AEDE')
        self.left.pack(side=LEFT)
        self.right=Frame(master, width=800, height=720, bg='beige')
        self.right.pack(side=RIGHT)
        self.c1 = ImageTk.PhotoImage(Image.open('flower.jpg')) #adding background image to the frame
        self.c1_label = Label(self.right, image=self.c1)   # adding image in label 
        self.c1_label.pack()

        #HEADING
        self.heading=Label(self.left, text="Know Your Disease",font=('Helvica 60 bold'),fg='black',bg='beige')
        self.heading.place(x=0,y=0)

        #username
        self.name=Label(self.left,text="Username",font=('arial 18 bold'),fg='black',bg='beige')
        self.name.place(x=50,y=200)

        #password of patient
        self.password=Label(self.left,text="Password",font=('arial 18 bold'),fg='black',bg='beige')
        self.password.place(x=50,y=250)

        #labels to accept entry        
        #name entry
        self.nameEntry=Entry(self.left,width=50)
        self.nameEntry.place(x=250,y=210)

        #password entry
        self.passwordEntry=Entry(self.left,width=10)
        self.passwordEntry.place(x=250,y=260)

        #creating a button
        #login button
        self.done=Button( self.left,text='Login',width=20,height=3,bg='white',command=self.description)
        self.done.place(x=250,y=300)

        #new user button
        self.done=Button(self.left , text = 'New User?',width=20,height=3,bg='white',command=self.newpage) 
        self.done.place(x=50,y=300)

        #test button
        self.done=Button(self.left , text = 'test',width=20,height=3,bg='white',command=self.testpage) 
        self.done.place(x=400,y=500)
        
        
    
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
        
        self.lii= Label(self.newWindow,  text="Enter All The Details",font=('Helvica 40 bold'),fg='white',bg='skyblue')
        self.lii.place(x=0,y=0)
        self.lii.pack()
        
        #name
        self.newname=Label(self.newWindow , text='Patient Name',font=('arial 18 bold'),fg='white',bg='Green')
        self.newname.place(x=50,y=200)
        # self.nameEntry=Entry(self.newWindow,width=50)
        # self.nameEntry.place(x=250 ,y=210)
        self.newname.pack()

        #age
        self.age=Label(self.newWindow , text='Age',font=('arial 18 bold'),fg='white',bg='blue')
        self.age.place(x=100,y=400)
        # self.ageEntry=Entry(self.newWindow,width=50)
        # self.ageEntry.place(x=300 ,y=410)
        self.age.pack()

        #gender
        self.gender=Label(self.newWindow , text='Gender',font=('arial 18 bold'),fg='white',bg='green')
        self.gender.place(x=150,y=600)
        # self.genderEntry=Entry(self.newWindow,width=50)
        # self.genderEntry.place(x=350 ,y=610)
        self.gender.pack()

        #contact number
        self.contact=Label(self.newWindow , text='Contact',font=('arial 18 bold'),fg='white',bg='blue')
        self.contact.place(x=200,y=800)
        # self.contactEntry=Entry(self.newWindow,width=50)
        # self.contactEntry.place(x=400 ,y=810)
        self.contact.pack()

        #address
        self.address=Label(self.newWindow , text='Patient Name',font=('arial 18 bold'),fg='white',bg='green')
        self.address.place(x=250,y=1000)
        # self.addressEntry=Entry(self.newWindow,width=50)
        # self.addressEntry.place(x= 650,y=1010)
        self.address.pack()

   
            
    # definition for button login
    def description(self): 

        self.newWindow1= Toplevel(root)
        self.newWindow1.title('USER REFERENCE PORTAL')
        self.newWindow1.geometry("1200x720+0+0")
        
        self.heading= Label(self.newWindow1,  text="WELCOME TO THE DASHBOARD",font=('Helvica 40 bold'),fg='white',bg='seagreen')
        self.heading.place(x=0,y=0)

        # self.content = Frame(self.newWindow,width=800, height=720, bg='pink')
        # self.content.pack(side=LEFT)

        # self.try = Label(self.content, text='PNEMONIA' , bg='red')
        # self.try.pack(side=LEFT)
        

    # definition for test button
    def testpage(self):
        self.image=Image.open("bg flower.jpg")
        self.test=ImageTk.PhotoImage(self.image)

        self.top = Toplevel()
        self.top.geometry("180x100")
        self.top.title("toplevel")
        self.l2 = Label(self.top, image=self.test, text = "This is toplevel window")
        # Resize the image using resize() method
        self.resize_image = self.image.resize((180, 100))
        self.l2.pack()
        self.l2.image=self.test
 
        

        
    



        


        
        
          
        

        

#objects
root=Tk()                                                            # creates a tk object
# photo=PhotoImage(file="flower.jpg")
# PhotoImage=photo.subsample(1,2)
b=Mainfile(root)
root.geometry("1200x720+0+0")                                        # creates geometry of main window
root.resizable(False,False)
root.mainloop()





