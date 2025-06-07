from flask_sqlalchemy import SQLAlchemy

# --- INITIALISATION SQLALCHEMY ---
db = SQLAlchemy()

# --- MODELES ---
class Publication(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    categorie = db.Column(db.String(255), nullable=False)
    prix = db.Column(db.Numeric(10, 2), nullable=False)
    unite = db.Column(db.String(50), nullable=False)
    image = db.Column(db.Text)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    roles = db.Column(db.String(20))  

    db.create_all()