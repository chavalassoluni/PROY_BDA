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

    print(check_credentials(identificacion, contrasena), "este!!")
    if check_credentials(identificacion, contrasena):
        #GUARDAR COKKIE
        resp = make_response(redirect(url_for('gerente')))
        resp.set_cookie('identificacion', identificacion)
        print(resp, "validacion")
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
    cursor.execute("SELECT idEmpleado, NombreEmpleado, DocumentoEmpleado, idCargo FROM leerencanta.empleado WHERE DocumentoEmpleado = %s AND Contrasena =%s AND idCargo = 1", (identificacion, contrasena))
    info_empleado = cursor.fetchone()
    print(info_empleado,"prueba")
    return info_empleado is not None


def validacionUsuarioSucursal(identificacion):
    cursor.execute("SELECT * FROM empleado e INNER JOIN sucursal s ON e.NombreSucursal = s.NombreSucursal WHERE e.DocumentoEmpleado = %s", (identificacion))
    info_empleadoSucursalLogueo = cursor.fetchall()
    return info_empleadoSucursalLogueo


def check_credentials_cliente(identificacion, contrasena):
    # Ejemplo de consulta para verificar las credenciales
    cursor.execute("SELECT idCliente, NombreCliente, DocumentoCliente FROM leerencanta.cliente WHERE DocumentoCliente = %s AND Contrasena =%s", (identificacion, contrasena))
    info_cliente = cursor.fetchone()
    return info_cliente is not None


def obtener_info_cliente():
    cursor.execute("SELECT DocumentoCliente, NombreCliente, CiudadResidencia, Contrasena, LIbrosComprados FROM leerencanta.cliente")
    info_miembro = cursor.fetchall()
    return info_miembro

#CONSULTA LIBROS DISPONIBLES EN BARRANQUILLA
def listadoLibrosBarranquilla():
    cursor.execute("SELECT libro.Titulo, sucursal.NombreSucursal FROM inventario JOIN libro ON inventario.idLibro = libro.idLibro JOIN sucursal ON inventario.NombreSucursal = sucursal.NombreSucursal WHERE sucursal.NombreSucursal='Arena de ideas'")
    listadoBarranquilla = cursor.fetchall()
    return listadoBarranquilla

#CONSULTA LIBROS DISPONIBLES EN MEDELLIN
def listadoLibrosMedellin():
    cursor.execute("SELECT libro.Titulo, sucursal.NombreSucursal FROM inventario JOIN libro ON inventario.idLibro = libro.idLibro JOIN sucursal ON inventario.NombreSucursal = sucursal.NombreSucursal WHERE sucursal.NombreSucursal='Librero del valle'")
    listadoLibrosMedellin = cursor.fetchall()
    return listadoLibrosMedellin

#CONSULTA LIBROS DISPONIBLES EN SANTA MARTA
def listadoLibrosSantaMarta():
    cursor.execute("SELECT libro.Titulo, sucursal.NombreSucursal FROM inventario JOIN libro ON inventario.idLibro = libro.idLibro JOIN sucursal ON inventario.NombreSucursal = sucursal.NombreSucursal WHERE sucursal.NombreSucursal='Mar de libros'")
    listadoLibrosSantaMarta = cursor.fetchall()
    return listadoLibrosSantaMarta

#CONSULTA LIBROS DISPONIBLES EN CARTAGENA
def listadoLibrosCartagena():
    cursor.execute("SELECT libro.Titulo, sucursal.NombreSucursal FROM inventario JOIN libro ON inventario.idLibro = libro.idLibro JOIN sucursal ON inventario.NombreSucursal = sucursal.NombreSucursal WHERE sucursal.NombreSucursal='Murallas del saber'")
    listadoLibrosCartagena = cursor.fetchall()
    return listadoLibrosCartagena

def listadoLibrosRiohacha():
    cursor.execute("SELECT libro.Titulo, sucursal.NombreSucursal FROM inventario JOIN libro ON inventario.idLibro = libro.idLibro JOIN sucursal ON inventario.NombreSucursal = sucursal.NombreSucursal WHERE sucursal.NombreSucursal='Oasis de lectura'")
    listadoLibrosRiohacha = cursor.fetchall()
    return listadoLibrosRiohacha

def listadoLibrosBogota():
    cursor.execute("SELECT libro.Titulo, sucursal.NombreSucursal FROM inventario JOIN libro ON inventario.idLibro = libro.idLibro JOIN sucursal ON inventario.NombreSucursal = sucursal.NombreSucursal WHERE sucursal.NombreSucursal='Paginas capitalinas'")
    listadoLibrosBogota = cursor.fetchall()
    return listadoLibrosBogota

def listadoLibrosPasto():
    cursor.execute("SELECT libro.Titulo, sucursal.NombreSucursal FROM inventario JOIN libro ON inventario.idLibro = libro.idLibro JOIN sucursal ON inventario.NombreSucursal = sucursal.NombreSucursal WHERE sucursal.NombreSucursal='Palabras Andinas'")
    listadoLibrosPasto = cursor.fetchall()
    return listadoLibrosPasto

def listadoLibrosCali():
    cursor.execute("SELECT libro.Titulo, sucursal.NombreSucursal FROM inventario JOIN libro ON inventario.idLibro = libro.idLibro JOIN sucursal ON inventario.NombreSucursal = sucursal.NombreSucursal WHERE sucursal.NombreSucursal='Rincon literario cali'")
    listadoLibrosCali = cursor.fetchall()
    return listadoLibrosCali


#INFORMACION DE EMPLEADOS
def listadoEmpMedellin():
    cursor.execute("SELECT e.NombreEmpleado,e.DocumentoEmpleado, e.FechaNacimiento, e.FechaIngreso, e.Salario, e.Celular, e.Telefono FROM empleado e WHERE e.NombreSucursal = 'Librero del valle'")
    infoEmpleMede = cursor.fetchall()
    return infoEmpleMede

def buscarMiembro():
    data = None
    

def chequeoCredencialEmpleado(identificacion):
    print("prueba:",identificacion)
    cursor.execute("SELECT em.DocumentoEmpleado, em.NombreEmpleado, em.FechaNacimiento, em.FechaIngreso, em.Salario, em.Celular, em.Telefono, em.idCargo, sucursal.NombreSucursal, sucursal.CiudadSucursal FROM empleado em JOIN sucursal ON em.NombreSucursal = sucursal.NombreSucursal WHERE em.DocumentoEmpleado = %s", (identificacion))
    print("confirm")
    busquedaEmple = cursor.fetchall()
    print( busquedaEmple, "busqueda")
    return busquedaEmple

def agregarEmpleado(nombre, cedula, fecha_ento, fecha_ingreso, salario, contrasena,  celular, tel_fijo, cargos, sucursal):

     # Ejecutar la consulta SQL para insertar el empleado
    cursor.execute('INSERT INTO empleado (NombreEmpleado, DocumentoEmpleado, FechaNacimiento, FechaIngreso, Salario, Contrasena, Celular, Telefono, idCargo, NombreSucursal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)',
    (nombre, cedula, fecha_ento, fecha_ingreso, salario, contrasena, celular, tel_fijo, cargos, sucursal))
    # Guardar los cambios en la base de datos
    connection.commit()
    print(nombre, cedula, fecha_ento, fecha_ingreso, salario, contrasena, celular, celular, cargos, sucursal)
    return False  # Retorna False si no se ha procesado el formulario

def listadoSucursales():
    cursor.execute("SELECT * FROM sucursal")
    resultadoSucursales=cursor.fetchall()
    return resultadoSucursales

def listacargo():
    cursor.execute("SELECT * FROM cargo")
    resultadoCargo=cursor.fetchall()
    return resultadoCargo