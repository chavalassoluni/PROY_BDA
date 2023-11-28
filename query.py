from flask_mysqldb import MySQL
import pymysql
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session, make_response
app = Flask(__name__, static_folder='static', template_folder='template')
# Configura la conexión a la base de datos MySQL
connection = pymysql.connect(host="localhost", user="root", passwd="", database="leerencanta")
cursor = connection.cursor()

def obtenerEmpleados():
    cursor.execute("SELECT * FROM leerencanta.empleado")
    rows = cursor.fetchall()    
    return rows

def validarLogin(identificacion, contrasena):
    error = None
        # Verificar las credenciales en la base de datos
    if check_credentials(identificacion, contrasena):
        #GUARDAR COKKIE
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('identificacion', identificacion)
        return resp
    
    else:
        if check_credentials_cliente(identificacion, contrasena):
            resp = make_response(redirect(url_for('cliente')))
            resp.set_cookie('identificacion', identificacion)
            return resp
        else:
            error = 'Credenciales incorrectas. Por favor, inténtalo de nuevo.'

    return render_template('login.html', error=error)

# Función para verificar las credenciales en la base de datos
def check_credentials(identificacion, contrasena):
    # Ejemplo de consulta para verificar las credenciales
    cursor.execute("SELECT idEmpleado, NombreEmpleado, DocumentoEmpleado FROM leerencanta.empleado WHERE DocumentoEmpleado = %s AND Contrasena =%s", (identificacion, contrasena))
    info_empleado = cursor.fetchone()
    return info_empleado is not None


def validacionUsuarioSucursal(identificacion):
    cursor.execute("SELECT * FROM empleado e INNER JOIN sucursal s ON e.NombreSucursal = s.NombreSucursal WHERE e.DocumentoEmpleado = %s", (identificacion))
    info_empleadoSucursalLogueo = cursor.fetchone()
    return info_empleadoSucursalLogueo


def check_credentials_cliente(identificacion, contrasena):
    # Ejemplo de consulta para verificar las credenciales
    cursor.execute("SELECT idCliente, NombreCliente, DocumentoCliente FROM leerencanta.cliente WHERE DocumentoCliente = %s AND Contrasena =%s", (identificacion, contrasena))
    info_cliente = cursor.fetchone()
    return info_cliente is not None
