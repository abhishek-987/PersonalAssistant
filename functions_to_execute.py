import mysql.connector
import datetime

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="function_database"

)
x = datetime.datetime.now()

s=input("enter the keyword function: ")

mycursor = mydb.cursor()
mycursor.execute("SELECT function_operation FROM functions_table WHERE function_name = '"+s+"';")
myresult = mycursor.fetchone()
print(eval(myresult[0]))

'''x = datetime.datetime.now()

s=input("Enter the key word you want to search for: ")

if s == "date":
	print(x.strftime("%d"))
elif s == "day":
	print(x.strftime("%A"))
elif s == "year":
	print(x.strftime("%Y"))'''