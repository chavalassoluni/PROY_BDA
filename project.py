from flask import Flask
from flask_mysqldb import MySQL
from query import obtenerEmpleados, validarLogin, validacionUsuarioSucursal, obtener_info_cliente, listadoLibrosBarranquilla, listadoLibrosMedellin, listadoLibrosSantaMarta, listadoLibrosCartagena, listadoLibrosRiohacha, listadoLibrosBogota, listadoLibrosPasto, listadoLibrosCali, listadoEmpMedellin, chequeoCredencialEmpleado, agregarEmpleado, listadoSucursales, listacargo, agregarClientes, ciudades, chequeoCredencialCliente
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

@app.route('/buscarEmpleado', methods=['GET', 'POST'])
def buscarEmpleado():
    error = None
    if request.method == 'POST':
        # Obtén el término de búsqueda del formulario
        identificacion = request.form['identificacion']
        print(identificacion)
        data = chequeoCredencialEmpleado(identificacion)
        print(data, "este")
        if data:            
            print('¡Empleado encontrado!.')
            return render_template('buscarEmpleado.html', resultados=data)
        else:
            print('No se encontraron empleados con esa identificación.')
    return render_template('buscarEmpleado.html')

@app.route('/index')
def index():
    identificacion_usuario = request.cookies.get('identificacion')
    empleadosSucursal=validacionUsuarioSucursal(identificacion_usuario)
    return render_template('index.html', datosEmpleado=empleadosSucursal)

@app.route('/cliente')
def cliente():
     identificacionCliente = request.cookies.get('identificacion')
     clienteSucursal=validacionUsuarioSucursal(identificacionCliente)
     return render_template('./cliente.html', clientes=clienteSucursal)

@app.route('/perfilCliente')
def clientePerfil():
     clientePerfil=obtener_info_cliente()
     return render_template('./cliente.html', perfilCliente=clientePerfil)



@app.route('/Barranquilla')
def comprarLibroCliente():
     librosBarranquilla = listadoLibrosBarranquilla()
     return render_template('./barranquilla.html', librosB=librosBarranquilla)

@app.route('/medellin')
def comprarLibroClienteMedellin():
     librosMedellin = listadoLibrosMedellin()
     return render_template('./medellin.html', librosM=librosMedellin)

@app.route('/santaMarta')
def comprarLibroClienteSantaMartha():
     librosSnMarta = listadoLibrosSantaMarta()
     return render_template('./santaMarta.html', librosS=librosSnMarta)

@app.route('/cartagena')
def comprarLibroClienteCartagena():
     librosCartagena = listadoLibrosCartagena()
     return render_template('./cartagena.html', librosC=librosCartagena)

@app.route('/riohacha')
def comprarLibroClienteRiohacha():
     librosRiohacha = listadoLibrosRiohacha()
     return render_template('./riohacha.html', librosR=librosRiohacha)

@app.route('/bogota')
def comprarLibroClienteBogota():
     librosBogota = listadoLibrosBogota()
     return render_template('./bogota.html', librosBg=librosBogota)

@app.route('/pasto')
def comprarLibroClientePasto():
     librosPasto = listadoLibrosPasto()
     return render_template('./pasto.html', librosP=librosPasto)

@app.route('/cali')
def comprarLibroClienteCali():
     librosCali = listadoLibrosCali()
     return render_template('./cali.html', librosCali=librosCali)


#OBTENER INFO DE EMPLEADOS POR SUCURSAL
@app.route('/empMedellin')
def infoEmpMedellin():
     infoEmpMedellin = listadoEmpMedellin()
     return render_template('./empMedellin.html', infoEmple=infoEmpMedellin)

@app.route('/comprarLibroC')
def comprarLibroC():
     return render_template('./comprarLibroC.html')

@app.route('/consolidado')
def conoslidado():
     return render_template('./consolidado.html')

@app.route('/reportes')
def reportes():
     return render_template('./reportes.html')

@app.route('/gerente')
def gerente():
     return render_template('./gerente.html')

@app.route('/sucursalesCompra')
def sucursalesCompra():
     return render_template('./sucursalesCompra.html')

@app.route('/agregarEmple', methods=['POST', 'GET'])
def agregarEmple():
     if request.method == 'POST':
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        fecha_ento = request.form['fecha_ento']
        fecha_ingreso = request.form['fecha_ingreso']
        salario = request.form['salario']
        contrasena = request.form['contrasena']
        tel_fijo = request.form['tel_fijo']
        celular = request.form['celular']
        cargo = request.form['cargo']
        sucursal = request.form['sucursal']
        print(nombre, cedula, fecha_ento, fecha_ingreso, salario, contrasena, celular,  tel_fijo, cargo, sucursal)
        # Llamamos a la función de validación del login
        agregarEmpleado(nombre, cedula, fecha_ento, fecha_ingreso, salario, contrasena, celular,  tel_fijo, cargo, sucursal)
     
     sucursalList=listadoSucursales()
     cargosList=listacargo()

     return render_template('./agregarEmpleado.html',sucursales=sucursalList, listaCargos=cargosList)

@app.route('/agregarCliente', methods=['POST', 'GET'])
def agregarCliente():
     if request.method == 'POST':
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        celular = request.form['celular']
        tel_fijo = request.form['tel_fijo']
        ciudadR = request.form['ciudadR']
        contrasena = request.form['contrasena']
        FechaRegistro = request.form['FechaRegistro']

        print(nombre, cedula, celular, tel_fijo, ciudadR, contrasena, FechaRegistro)
        # Llamamos a la función de validación del login
        agregarClientes(nombre, cedula, celular, tel_fijo, ciudadR, contrasena, FechaRegistro)
     
     listaCiudades=ciudades()
     sucursalList=listadoSucursales()


     return render_template('./agregarCliente.html',sucursales=sucursalList, listaCiudades=listaCiudades)

@app.route('/buscarCliente', methods=['GET', 'POST'])
def buscarCliente():
    error = None
    if request.method == 'POST':
        # Obtén el término de búsqueda del formulario
        identificacion = request.form['identificacion']
        print(identificacion)
        data = chequeoCredencialCliente(identificacion)
        print(data, "este")
        if data:            
            print('¡Cliente encontrado!.')
            return render_template('buscarCliente.html', resultados=data)
        else:
            print('No se encontraron clientes con esa identificación.')
    return render_template('buscarCliente.html')

if __name__ =='__main__':
    app.run(port =3000, debug =True)