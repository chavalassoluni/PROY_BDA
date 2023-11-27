from flask_mysqldb import MySQL
import pymysql

# Configura la conexión a la base de datos MySQL
connection = pymysql.connect(host="localhost", user="root", passwd="", database="leerencanta")
cursor = connection.cursor()

def obtenerEmpleados():
    cursor.execute("SELECT * FROM leerencanta.empleado")
    rows = cursor.fetchall()    
    return rows
