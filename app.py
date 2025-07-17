from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from controllers.database import db
from flask import url_for,render_template , redirect , request , session,flash

app = Flask(__name__)
app.secret_key = "orewamadhamadhathsyuyokunaru"
# this line below is used for databse configursation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)


from controllers.models import *
from controllers.generalroutes import *




if __name__ == "__main__":  
    with app.app_context():
        db.create_all()  
    app.run(debug=True)

