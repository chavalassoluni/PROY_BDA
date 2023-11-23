# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    gerente_id = db.Column(db.Integer, db.ForeignKey('empleado.id'))
    empleados = db.relationship('Empleado', backref='sucursal', lazy=True)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), nullable=False, unique=True)
    documento_id = db.Column(db.String(20), nullable=False, unique=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)
    salario = db.Column(db.Float, nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), nullable=False, unique=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    editorial = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(20), nullable=False, unique=True)
    num_paginas = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    documento_id = db.Column(db.String(20), nullable=False, unique=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    ciudad_residencia = db.Column(db.String(50), nullable=False)
    compras = db.relationship('Compra', backref='cliente', lazy=True)

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    libro_id = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    fecha_compra = db.Column(db.Date, nullable=False)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
