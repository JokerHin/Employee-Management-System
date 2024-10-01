import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor,conn
    try:
        conn=pymysql.connect(host='localhost',user='root',password='Kar@050506')
        mycursor=conn.cursor() #execute sql command
    except:
        messagebox.showerror('Error','Something went wrong,Please open mysql app before running')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(30),Name VARCHAR(50),Phone VARCHAR(15),Role VARCHAR(50), Gender VARCHAR(20), Salary DECIMAL(10,2))')

def insert(id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))  #put placeholder to our actual data
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result=mycursor.fetchone()  #store the input from mySQL
    return result[0]>0

def fetch_employee():
    mycursor.execute('SELECT * from data')
    result=mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()   #commit the changes to update the table

def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    conn.commit()

def search(option,value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()      #store the result from SQL to python
    return result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data')     #delete all data from the table
    conn.commit()

connect_database()