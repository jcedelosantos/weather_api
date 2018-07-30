from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import DECIMAL

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clima.db'
db = SQLAlchemy(app)


class Medicion(db.Model):
	"""docstring for Medicion"""
	id =  db.Column(db.Integer(), primary_key= True)
	idHardware = db.Column(db.String(30))
	temperatura = db.Column(db.DECIMAL(10,4))
	humedad = db.Column(db.String(5))
	presionBar= db.Column(db.DECIMAL(10,4))
	altitud=db.Column(db.DECIMAL(10,4))
	fecha = db.Column(db.DateTime())
	# sensors = db.relationship('Sensor', backref='owner')

class Sensor(db.Model):
	"""docstring for Sensor"""
	id =  db.Column(db.Integer(), primary_key= True)
	# owner_id = db.Column(db.Integer, db.ForeignKey('medicion.id'))
	idHardware =db.Column(db.String(30))
	nombre = db.Column(db.String())
	latitud = db.Column(db.DECIMAL(10,18))
	Longitud= db.Column(db.DECIMAL(10,18))
	ubicacion=db.Column(db.String())
	estatus = db.Column(db.Integer())
