from flask import Flask
from flask_mysqldb import MySQL
from query import obtenerEmpleados, validarLogin, validacionUsuarioSucursal
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session
app = Flask(__name__, static_folder='static', template_folder='template')


# Ruta para el formulario de login
@app.route('/login', methods=['POST', 'GET'])
def login():
     error = None
     if request.method == 'POST':
        identificacion = request.form['identificacion']
        contrasena = request.form['contrasena']
        print(identificacion, contrasena)
        # Llamamos a la función de validación del login
        return validarLogin(identificacion, contrasena)
     

     return render_template('login.html', error=error, )

@app.route('/index')
def index():
    identificacion_usuario = request.cookies.get('identificacion')
    empleadosSucursal=validacionUsuarioSucursal(identificacion_usuario)
    return render_template('index.html', datosEmpleado=empleadosSucursal)

@app.route('/cliente')
def cliente():
     identificacionCliente = request.cookies.get('identificacion')
     clienteSucursal=validacionUsuarioSucursal(identificacionCliente)
     return render_template('./cliente.html', cliente=clienteSucursal)

@app.route('/consolidado')
def conoslidado():
     return render_template('./consolidado.html')


@app.route('/barranquilla')
def barranquilla():
     return render_template('./barranquilla.html')

@app.route('/bogota')
def bogota():
     return render_template('./bogota.html')

@app.route('/cali')
def cali():
     return render_template('./cali.html')

@app.route('/cartagena')
def cartagena():
     return render_template('./cartagena.html')

@app.route('/medellin')
def medellin():
     return render_template('./medellin.html')

@app.route('/pasto')
def pasto():
     return render_template('./pasto.html')

@app.route('/riohacha')
def riohacha():
     return render_template('./riohacha.html')

@app.route('/santaMarta')
def santaMarta():
     return render_template('./santaMarta.html')


@app.route('/gerente')
def gerente():
     return render_template('./gerente.html')




if __name__ =='__main__':
    app.run(port =3000, debug =True)