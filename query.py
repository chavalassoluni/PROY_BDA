from flask_mysqldb import MySQL
import pymysql
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session
app = Flask(__name__, static_folder='static', template_folder='template')
# Configura la conexión a la base de datos MySQL
connection = pymysql.connect(host="localhost", user="root", passwd="", database="leerencanta")
cursor = connection.cursor()

def obtenerEmpleados():
    cursor.execute("SELECT * FROM leerencanta.empleado")
    rows = cursor.fetchall()    
    return rows

def validarLogin(identificacion, contrasena):
    print('prueba1')
    error = None
        # Verificar las credenciales en la base de datos
    if check_credentials(identificacion, contrasena):
            # Credenciales válidas, redirigir a la página de inicio
        print('prueba2')
        return redirect(url_for('index'))
    else:
        print('prueba3')
        error = 'Credenciales incorrectas. Por favor, inténtalo de nuevo.'

    return render_template('login.html', error=error)

# Función para verificar las credenciales en la base de datos
def check_credentials(identificacion, contrasena):
    # Ejemplo de consulta para verificar las credenciales
    cursor.execute("SELECT idEmpleado, NombreEmpleado, DocumentoEmpleado FROM leerencanta.empleado WHERE DocumentoEmpleado = %s AND Contrasena =%s", (identificacion, contrasena))
    info_empleado = cursor.fetchone()
    print(info_empleado)
    return info_empleado is not None

    # Si hay un resultado, las credenciales son válidas
