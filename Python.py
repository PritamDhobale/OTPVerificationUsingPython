from cProfile import label
from tkinter import *
from tkinter import messagebox
import smtplib
import random

from matplotlib.pyplot import fill, text


def otp():
    root= Tk(className=" OTP VERIFICATION BY MAIL")
    # root.title()
    root.geometry("666x518")


    email_label = Label(root, text="Enter Your Email: ", font=("yu gothic ui", 13, "bold"), relief=RAISED)
    email_label.grid(row=0, column=0, padx=13, pady=60)
    email_entry = Entry(root, font=("ariel 13 bold"), width=35, relief=GROOVE, bd=2)
    email_entry.grid(row=0, column=1, padx=12, pady=60)
    email_entry.focus()

    otp_label = Label(root, text="Enter OTP: ", font=("yu gothic ui", 13, "bold"), relief=RAISED)
    otp_label.grid(row=1, column=0, padx=13, pady=60)
    otp_entry = Entry(root, font=("ariel 13 bold"), width=35, relief=GROOVE, bd=2)
    otp_entry.grid(row=1, column=1, padx=12, pady=60)
    otp_entry.focus()

    otp =''.join([str(random.randint(0,9)) for i in range(6)])

    #Access Gmail using SMTP
    #Create gmail server using smtp
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    #Now we Login the server
    server.login("bharatdapke24@gmail.com",'olerbanfpymrfusk')
    msg="Hello, Your OTP is "+str(otp)


        
    def send():
        try:    
            server.sendmail("bharatdapke24@gmail.com" , email_entry.get() , msg)
            messagebox.showinfo("Send OTP via Email", f"OTP sent to {email_entry.get()}")

        except:
            messagebox.showinfo("Send OTP via Email", "Please enter the valid email address OR check an internet connection")
        
    send_button = Button(root, text="Send Email", font=("yu gothic ui", 13, "bold"), width=10, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=send)
    send_button.place(x=190, y=100)

    def getvalue():

        try: 
            verify = otp_entry.get()
            if(verify==otp):
                messagebox.showinfo("Send OTP via Email", f"OTP is verify")
            else:
                messagebox.showinfo("Send OTP via Email", f"Please enter valid OTP")
        

        except:
            messagebox.showinfo("Send OTP via Email", "Please enter the valid OTP Number OR check an internet connection")

    otp_button = Button(root, text="Check OTP",font=("yu gothic ui", 13, "bold"), width=10, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=getvalue)
    otp_button.place(x=190, y=250)
    root.mainloop()