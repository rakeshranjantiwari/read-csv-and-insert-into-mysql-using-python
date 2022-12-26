import mysql.connector as mysql
from mysql.connector import Error
import csv
#Connect DB server and database
conn = mysql.connect(user='root', password='root', host='localhost', database='test_db')
cursor = conn.cursor()
#open the csv file
with open('users.csv', mode='r') as csv_file:
    #read csv using reader class
    csv_reader = csv.reader(csv_file)
    #skip header
    header = next(csv_reader)
    #Read csv row wise and insert into table
    for row in csv_reader:
        sql = "INSERT INTO users (name, mobile, email) VALUES (%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")

conn.commit()
cursor.close()
