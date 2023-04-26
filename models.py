from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(500))
    lastname = db.Column(db.String(500))
    email = db.Column(db.String(500))
    password = db.Column(db.String(500))
    role = db.Column(db.String(500))
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    

    
    


class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(500))
    apellidos = db.Column(db.String(500))
    correo = db.Column(db.String(500))
    fecha_nacimiento = db.Column(db.DateTime)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    
    
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# db.create_all()
    
    
    
    