from customtkinter import *
from PIL import Image #use for image
from tkinter import messagebox #messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='Karhin' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success', 'Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid Input')

root = CTk() #create window
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
image= CTkImage(Image.open('img_1.png'),size=(930,478)) #Store the image to a variable
imageLabel=CTkLabel(root,image=image,text="") #Label the image
imageLabel.place(x=0,y=0) #locate the image
headingLabel = CTkLabel(root,text='Employee Management System', bg_color='#FAFAFA', font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headingLabel.place(x=20,y=100)


usernameEntry = CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=50,y=150)

passwordEntry = CTkEntry(root,placeholder_text='Enter Your Password',width=180, show='x')
passwordEntry.place(x=50,y=200)

loginButton = CTkButton(root,text='Login',cursor='hand2',command=login) #cursor make the click mouse to hand #command is a function to call when click
loginButton.place(x=70,y=250)

root.mainloop() #hold the window keep looping

