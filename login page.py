from tkinter import*
root=Tk()
def getvals():
    print("It works")
root.geometry("644x344")
#Heading
Label(root,text="Welcome to My Page",font="CalifornianFB 13 italic",pady=15).grid(row=0,column=3)
root.title('Login Page')
#Text for our form
name=Label(root,text="Name")
Class=Label(root,text="Class")
Roll=Label(root,text="Roll No")
Contact=Label(root,text="Contact")
Add=Label(root,text="Address")
#Pack text for our form
name.grid(row=1,column=2)
Class.grid(row=2,column=2)
Roll.grid(row=3,column=2)
Contact.grid(row=4,column=2)
Add.grid(row=5,column=2)
#Tkinter variable for storing entries
namevalue=StringVar()
Classvalue=StringVar()
Rollvalue=StringVar()
Contactvalue=StringVar()
Addvalue=StringVar()
#Entries for our form
nameentry=Entry(root,textvariable=namevalue)
Classentry=Entry(root,textvariable=Classvalue)
Rollentry=Entry(root,textvariable=Rollvalue)
Contactentry=Entry(root,textvariable=Contactvalue)
Addentry=Entry(root,textvariable=Addvalue)
#Packing the Entries
nameentry.grid(row=1,column=3)
Classentry.grid(row=2,column=3)
Rollentry.grid(row=3,column=3)
Contactentry.grid(row=4,column=3)
Addentry.grid(row=5,column=3)
#Button & packing it and assigning it a command
Button(text="Submit your details",command=getvals,bg="blue",fg="white").grid(row=7,column=3,pady=13)
root.mainloop()
