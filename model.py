from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Faly@localhost/agriculture'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Définition du modèle Publication
class Publication(db.Model):
    __tablename__ = 'publication'  # Assure-toi que ta table s'appelle bien 'publication'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    categorie = db.Column(db.String(255), nullable=False)
    prix = db.Column(db.Numeric(10, 2), nullable=False)
    unite = db.Column(db.String(50), nullable=False)
    image = db.Column(db.Text)