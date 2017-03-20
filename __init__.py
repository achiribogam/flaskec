from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flaskext.markdown import Markdown
app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


#Migrations
migrate = Migrate(app, db)

#Markdown
Markdown(app)


from blog import views 
from author import views


