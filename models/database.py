#separated because a custom setup can be required
import postgresqlite
from flask_sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlite.get_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False