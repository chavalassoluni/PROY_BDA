from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
app = Flask(__name__, static_folder='static', template_folder='template')

# Configura la conexión a la base de datos MySQL
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "leerEncanta"
mysql = MySQL(app)

# Inicializar sesion
app.secret_key = 'mysecretkey'


@app.route('/')
def login():
     return render_template('login.html')


if __name__ =='__main__':
    app.run(port =3000, debug =True)