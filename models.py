from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(500))
    lastname = db.Column(db.String(500))
    email = db.Column(db.String(500))
    password = db.Column(db.String(500))
    role = db.Column(db.String(500))
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow)
    

    
    


class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(500))
    apellidos = db.Column(db.String(500))
    correo = db.Column(db.String(500))
    fecha_nacimiento = db.Column(db.DateTime)
  
    
    
    
class Discoteca(db.Model):
    __tablename__ = 'discoteca'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(500))
    lugar = db.Column(db.String(500))
    aforo = db.Column(db.Integer)
    descripcion = db.Column(db.Text)    
  
 
class Evento(db.Model):
    __tablename__ = 'evento'
    id = db.Column(db.Integer, primary_key = True)
    id_disco = db.Column(db.Integer, ForeignKey('discoteca.id'))  
    nombre = db.Column(db.String(500))
    descripcion = db.Column(db.Text)
    aforo = db.Column(db.Integer)
    fecha = db.Column(db.DateTime,default=datetime.utcnow)
    hora = db.Column(db.DateTime,default=datetime.utcnow)
    aforo = db.Column(db.Integer,default=18)
    
    
class Mapa(db.Model):
    __tablename__ = 'mapa'
    id = db.Column(db.Integer, primary_key = True)
    queryString = db.Column(db.Text)
    place_id = db.Column(db.Text)
    cid = db.Column(db.Text)
        
    
    
    
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    
    
    
    