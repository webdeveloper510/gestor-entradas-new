from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import secrets
from models import db


app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = secrets.token_hex(16)




app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfghjkl'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/myapp'
db.init_app(app)
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()



#Admin#123


