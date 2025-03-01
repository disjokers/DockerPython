import mysql.connector

connection = mysql.connector.connect(
user='root',
password='docker1',
host='172.17.0.2',
database='CochesDB'
)

cursor = connection.cursor()
cursor.execute("select * from coches")

res = cursor.fetchall()
for coche in res:
    print(coche)