#import all the modules we need, we have imported messagebox and * (all) from tkinter library
from tkinter import *
from tkinter import messagebox
#import regular expression and OS
import re
import os
 
#Callback functioon for validating User Phone number
def validate_phoneno(user_phoneno):
    if user_phoneno.isdigit():
        return True
    elif user_phoneno is "":
        return True
    else:
        messagebox.showinfo('Information','Only Digits are allowed for Phone Number')
        return False
 
#Function for validating User Email ID
def isValidEmail(user_email):
    if len(user_email) > 7:
        if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", user_email) !=None:
            return True
        return False
    else:
           messagebox.showinfo('Information','This is not a valid email address')
           return False
 
#Function for validating all other User Input Fields
        #pwd, confirmpwd, PhoneNo, EmailID
def validateAllFields():
            if v_fName.get() == "":
                messagebox.showinfo('Information','Please Enter Full Name To Proceed')
            elif v_pwd.get() == "":
                messagebox.showinfo('Information','Please Enter Password To Proceed')
            elif v_confirmPwd.get() == "":
                messagebox.showinfo('Information','Please Confirm Password To Proceed')
            elif v_phoneNo.get() == "":
                messagebox.showinfo('Information','Please Enter Phone Number To Proceed')
            elif len(v_phoneNo.get()) != 10:
                messagebox.showinfo('Information','Please Enter 10 digit Phone Number To Proceed')
            elif v_emailId.get() == "":
                messagebox.showinfo('Information','Please Enter Email ID To Proceed')
            elif v_gender.get() == 0:
                messagebox.showinfo('Information','Please Enter Gender To Proceed')
            elif v_pwd.get() != v_confirmPwd.get():
                messagebox.showinfo('Information','Password Mismatch')
            elif v_emailId.get() != "":
                status = isValidEmail(v_emailId.get())
                if(status):
                    messagebox.showinfo('Information','User Registered Successsfully')
            else:
                messagebox.showinfo('Information','User Registered Successsfully')
 
#Function to clear all user inputs in fields
def clearAllFeilds():
    v_fName.set("")
    v_pwd.set("")
    v_confirmPwd.set("")
    v_phoneNo.set("")
    v_emailId.set("")
 
def callNewScreen():
    window.destroy()
 
   #Use os.system('SendEmail.py') if the file is in the same location else use os.system('python SendEmail.py')
    os.system('python LoginScreen.py')
 
#To create the main window of our application we use Tk class.
 
window = Tk()
 
window.title("Welcome To User Registration Screen")
 
#Now set window size and window color
window.geometry('500x500')
window.configure(background="grey");
 
v_fName = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_gender = IntVar()
 
#Label widgets
 
lb_heading=Label(window,text="Registration Screen", width=20, font=("bold",20), bg="grey")
lb_heading.place(x=90,y=53)
 
lb_fullname=Label(window,text="Full Name", width=20, font=("bold",10), bg="grey")
lb_fullname.place(x=80,y=130)
 
#Entry will alow user to enter any kind of value like string, nymvers, special characters, etc,
entry_fullname=Entry(window, textvariable = v_fName)
entry_fullname.place(x=240,y=130)
 
lb_pwd=Label(window,text="Password", width=20, font=("bold", 10), bg="grey")
lb_pwd.place(x=80,y=170)
entry_pwd=Entry(window, show="*", textvariable = v_pwd)
entry_pwd.place(x=240,y=170)
 
lb_confirm_pwd=Label(window,text="Confirm Password", width=20, font=("bold", 10), bg="grey")
lb_confirm_pwd.place(x=80,y=210)
entry_confirm_pwd=Entry(window, show="*", textvariable = v_confirmPwd)
entry_confirm_pwd.place(x=240,y=210)
 
lb_phoneno=Label(window,text="Phone No.", width=20, font=("bold", 10), bg="grey")
lb_phoneno.place(x=80,y=250)
entry_phoneno=Entry(window, show="", textvariable = v_phoneNo)
entry_phoneno.place(x=240,y=250)
 
#Register callback function
valid_phoneno = window.register(validate_phoneno)
 
entry_phoneno.config(validate="key",validatecommand=(valid_phoneno,'%P'))
 
lb_email=Label(window,text="Email", width=20, font=("bold", 10), bg="grey")
lb_email.place(x=80,y=290)
entry_email=Entry(window, textvariable = v_emailId)
entry_email.place(x=240,y=290)
 
lb_gender=Label(window,text="Gender", width=20, font=("bold", 10), bg="grey")
lb_gender.place(x=80,y=330)
Radiobutton(window, text="Male", bg="grey", padx=5, variable=v_gender, value=1).place(x=230,y=330)
Radiobutton(window, text="Female", bg="grey", padx=20, variable=v_gender, value=2).place(x=290,y=330)
 
btn_register = Button(window, text="REGISTER", command = validateAllFields, bg="blue", fg = "white", font=("bold", 10)).place(x=150, y=450)
btn_clear = Button(window, text="CLEAR", command = clearAllFeilds, bg="blue", fg = "white", font=("bold", 10)).place(x=250, y=450)
btn_existinguser = Button(window, text="Existing User", command = callNewScreen, bg="blue", fg = "white", font=("bold", 10)).place(x=330, y=450)
 
#Window.mainloop() function calls the endless loop of the window so it will remain open till user closes it.
window.mainloop()
