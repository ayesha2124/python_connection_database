#connection of python to database
import mysql.connector as m
mydb = m.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ki"
)
#using cursors
mycursor = mydb.cursor()

#create table
#mycursor.execute("CREATE TABLE Facultys(name VARCHAR(20),age int,Feedback VARCHAR(30),Salary VARCHAR(30))")

#insert values to table in the database
# n=int(input("Enter no of records"))
# for i in range(n):
#
#         name = input("Enter Faculty name: ")
#         age = input("Enter Faculty age: ")
#         Feedback = input("Enter Faculty's Feedback: ")
#         Salary = input("Enter Faculty Salary: ")
#
#         query = "INSERT INTO Facultys(name, age, Feedback, Salary) VALUES (%s, %s, %s, %s)"
#         mycursor.execute(query, (name, age, Feedback,Salary))

#delete command
# age=input("Enter age")
# mycursor.execute("Delete from Facultys where age=%s",(age,))

#update query
# name = input("Enter Faculty name: ")
# age = input("Enter Faculty age: ")
# Feedback = input("Enter Faculty's Feedback: ")
# Salary = input("Enter Faculty Salary: ")
# mycursor.execute("UPDATE Facultys SET age = %s, Feedback = %s, Salary = %s WHERE name = %s", (age, Feedback, Salary, name))

#select query
# mycursor.execute("select * from Facultys")
# Facultys=mycursor.fetchall();
# for i in Facultys:
#     print(i)

mydb.commit()







