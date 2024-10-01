from customtkinter import *
from PIL import Image #use for image
from tkinter import ttk,messagebox
import database

def delete_all():
    result=messagebox.askyesno('Confirm','Do you really want to delete all the records?')
    if result:  #result = True
        database.deleteall_records()
        treeview_data()
    else:
        pass

def show_all():
    treeview_data()
    searchEntry.delete(0,END)   #empty the search bar
    searchBox.set('Search By')

def search_employee():
    if searchEntry.get()=='':   #if get empty return False
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get()=='Search By':  #if user didnt click anything return False
        messagebox.showerror('Error', 'Please select an option')
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())  # delete all first before print to avoid data duplication
        for employee in searched_data:
            tree.insert('', END, values=employee)

def delete_employee():
    selected_items=tree.selection()
    if not selected_items:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error','Data is deleted')


def update_employee():
    selected_item=tree.selection() #check if any selected item
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data() #display all data
        clear()
        messagebox.showinfo('Success','Data is updated')

def selection(event):
    selected_item = tree.selection()
    if selected_item:   #if select with something
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])

def clear(value=False):    #clear all input box when added a data
    if value:           #by default is false and still will clear, when true it will clearn and remove selection
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0,END)

def treeview_data():    #display data
    employees=database.fetch_employee()     #get all data from database and call the fetch function
    tree.delete(*tree.get_children())   #delete all first before print to avoid data duplication
    for employee in employees:
        tree.insert('',END,values=employee)

def add_employee():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif database.id_exists(idEntry.get()): #check if the id already exists
        messagebox.showerror('Error', 'Id already Exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error',"Invalid ID format. Use 'EMP' followed by a number (e.g., 'EMP1').")
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is added')


#GUI Part
window = CTk()
window.geometry('930x580+100+100')
window.resizable(False,False) #cannot resize
window.title('Employee Management System')
window.configure(fg_color='#161C30') #window background color
logo= CTkImage(Image.open('img.png'),size=(930,158)) #Store the image to a variable
imageLabel=CTkLabel(window,image=logo,text="") #Label the image
imageLabel.grid(row=0,column=0,columnspan=2) #locate the image using grid instead of place

leftFrame = CTkFrame(window,fg_color='#161C30')
leftFrame.grid(row=1,column=0) #easy to separate the location
#id
idLabel = CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=(20,20),pady=(15,15),sticky='w') #padx = add padding add space between left and right

idEntry = CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)
#name
nameLabel = CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=(20,20),pady=(15,15),sticky='w') #padx = add padding add space between left and right

nameEntry = CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)
#phone
phoneLabel = CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=2,column=0,padx=(20,20),pady=(15,15),sticky='w') #padx = add padding add space between left and right

phoneEntry = CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)
#role
roleLabel = CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=3,column=0,padx=(20,20),pady=(15,15),sticky='w')

role_options=['Web Developer','Cloud Architect','Technical Writer','Network Engineer',
              'DevOps Engineer','Data Scientist','IT Consultant','UI/UX Designer']
roleBox = CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',14,'bold'),state='readonly') #comboBox as a option for user to chose
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0]) #show the first option
#gender
genderLabel = CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'),text_color='white')
genderLabel.grid(row=4,column=0,padx=(20,20),pady=(15,15),sticky='w')

gender_options=['Male','Female','Other']
genderBox = CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',14,'bold'),state='readonly') #state='readonly' so user cannot change the option word
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0]) #show the first option
#Salary
salaryLabel = CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'),text_color='white')
salaryLabel.grid(row=5,column=0,padx=(20,20),pady=(15,15),sticky='w') #padx = add padding add space between left and right

salaryEntry = CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)

#rightFrame
rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1)
#searchBox
search_options = ['Id','Name','Phone','Role','Gender','Salary']
searchBox = CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row = 0,column=2)
#show all
showallButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showallButton.grid(row = 0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)     #add tree to create table like screen
tree.grid(row = 1,column=0,columnspan=4)

tree['column']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings') #delete the first column just only show heading

tree.column('Id',width=70) #anchor=CENTER can be add to align center for word in cell
tree.column('Name',width=140)
tree.column('Phone',width=140)
tree.column('Role',width=180)
tree.column('Gender',width=80)
tree.column('Salary',width=120)

style=ttk.Style()   #put style to the front

style.configure('Treeview.Heading',font=('arial',14,'bold'))
style.configure('Treeview',font=('arial',12),rowheight=30,background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview) #craete a scroll bar with vertical or horizontal
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame = CTkFrame(window,fg_color='#161C30') #back to the main and add button
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()     #display data everytime we run

window.bind('<ButtonRelease>',selection) #select data and show it

window.mainloop() #hold the window keep looping