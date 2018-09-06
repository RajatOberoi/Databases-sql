#Q.1- Write a python script to create a databse of students named Students.

import sqlite3

con=sqlite3.connect('Students.db')
print("Database created successfully")
con.close()

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
list1=[]
for i in range(10):
    a=input("enter name of student")
    b=int(input("enter no from 1-100"))
    if b>100 or b<1:
        print("enter a valid no")
        i=i-1
    else:
        c=a,b
        list1.append(c)     
        

#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.

import sqlite3

try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query="insert into Students(name,marks)values(?,?)"
    record = list1
    cursor.executemany(query,record)
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("DONE")    

#Q.4- Print the names of all the students who scored more than 80 marks.

import sqlite3
try:
    con = sqlite3.connect('Students.db')
    cursor=con.cursor()
    query='select * from Students where marks>80'
    cursor.execute(query)
    data=cursor.fetchall()
    for a in data:
        print('Name:{}'.format(a[0]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("problem occured",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Done")    
    
        

