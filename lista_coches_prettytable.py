import mysql.connector
import json
from prettytable import PrettyTable;

with open("datosdb.json","r") as archivo:
    config = json.load(archivo)

connection = mysql.connector.connect(
    user=config['user'],
    password=config['password'],
    host=config['host'],
    database=config['database']
)

cursor = connection.cursor()
cursor.execute("select * from coches")

res = cursor.fetchall()

tabla = PrettyTable(["ID", "MARCA", "MODELO", "COLOR", "KILOMETRAJE", "PRECIO"])
for fila in res:
    tabla.add_row(fila)
print(tabla)

cursor.close()
connection.close()