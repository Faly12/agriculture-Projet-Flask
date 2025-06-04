from flask import Flask, render_template, session, request, redirect, url_for, flash
from collections import namedtuple
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from psycopg2.extras import RealDictCursor
import psycopg2
import os

# --- CONFIGURATION DE L'APPLICATION ---
app = Flask(__name__)
app.secret_key = "une_cle_secrete_longue_et_complexe"
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Faly@localhost/agriculture'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- INITIALISATION SQLALCHEMY ---
db = SQLAlchemy(app)

# --- CRÉATION DOSSIER UPLOAD ---
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

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


# --- CREATION DES TABLES ---
with app.app_context():
    db.create_all()

# --- CONNEXION DB ---
def get_db_connection():
    return psycopg2.connect(
        dbname='agriculture',
        user='postgres',
        password='Faly',
        host='localhost',
        port='5432'
    )

# --- ROUTES ---
@app.route('/')
def accueil():
    produits = get_all_products()
    return render_template('accueil.html', produits=produits)

def get_all_products():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM produits")
        produits = cur.fetchall()
        cur.close()
        conn.close()
        return produits
    except Exception as e:
        print("Erreur de connexion ou de requête :", e)
        return []

@app.route('/index')
def index():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, nom, prix, unite, image, categorie, date_ajout FROM legume")
        legumes = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return render_template('index.html', legumes=legumes)

@app.route('/fruits')
def fruits():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, nom, prix, unite, image, categorie, description, date_ajout FROM fruits")
        fruits = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return render_template('fruits.html', fruits=fruits)

@app.route('/graines')
def graines():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, nom, prix, unite, image FROM graines")
        graines_data = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    Graine = namedtuple('Graine', ['id', 'nom', 'prix', 'unite', 'image'])
    graines = [Graine(*row) for row in graines_data]
    return render_template('graine.html', graines=graines)

@app.route('/ajouter_panier', methods=['POST'])
def ajouter_panier():
    try:
        produit_id = request.form.get('produit_id')
        nom = request.form.get('nom')
        prix_unitaire = float(request.form.get('prix_unitaire'))
        quantite = int(request.form.get('quantite'))
        email = request.form.get('email')
        montant_total = prix_unitaire * quantite
    except (TypeError, ValueError):
        return "Erreur : données invalides", 400

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO panier (produit_id, nom, prix_unitaire, quantite, email, montant_total)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (produit_id, nom, prix_unitaire, quantite, email, montant_total))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

    session['cart_count'] = session.get('cart_count', 0) + 1
    flash("Produit ajouté avec succès")
    session['panier_ajoute'] = True
    return redirect(url_for('accueil'))

@app.route('/produits')
def produits():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM panier")
        produits = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return render_template('produits.html', produits=produits)

@app.route('/addPublication', methods=['POST'])
def addPublication():
    nom = request.form['nomDeProduit']
    categorie = request.form['categorie']
    prix = request.form['prix']
    unite = request.form['unite']

    file = request.files.get('file')
    image_url = None

    if file and file.filename != '':
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        image_url = f"/{app.config['UPLOAD_FOLDER']}/{filename}"

    new_pub = Publication(
        nom=nom,
        categorie=categorie,
        prix=prix,
        unite=unite,
        image=image_url
    )
    db.session.add(new_pub)
    db.session.commit()
    return redirect(url_for('showPublications'))

@app.route('/publication')
def showPublications():
    publications = Publication.query.order_by(Publication.id.desc()).all()
    return render_template('publication.html', publications=publications)

@app.route('/searchContainer/<string:query>')
def searchContainer(query):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nom, prix, 'legume' AS categorie FROM legume WHERE LOWER(nom) LIKE LOWER(%s)
            UNION ALL
            SELECT id, nom, prix, 'fruits' AS categorie FROM fruits WHERE LOWER(nom) LIKE LOWER(%s)
            UNION ALL
            SELECT id, nom, prix, 'graines' AS categorie FROM graines WHERE LOWER(nom) LIKE LOWER(%s)
            ORDER BY id
        """, (f'%{query}%', f'%{query}%', f'%{query}%'))
        users = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return render_template("index.html", users=users)

@app.route('/galerie')
def galerie():
    return render_template('galerie.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Traitez le formulaire
        nom = request.form["nom"]
        email = request.form["email"]
        sujet = request.form["sujet"]
        message = request.form["message"]
        
        # Vous pouvez ajouter ici un enregistrement en base, envoi d'email, etc.
        flash("Message envoyé avec succès", "success")
        return redirect(url_for("contact"))

    # Affichez la page de contact si méthode GET
    return render_template("contact.html")

@app.route('/admin')
def admin():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT SUM(prix) FROM legume")
        result = cur.fetchone()
        total = result[0] if result[0] is not None else 0
    finally:
        cur.close()
        conn.close()
    return render_template('admin.html', total=total)

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    if User.query.filter_by(email=email).first():
        flash("Un compte existe déjà avec cet email. Veuillez vous connecter.", "warning")
        return redirect(url_for('index'))

    hashed_password = generate_password_hash(password)
    user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    session['user_id'] = user.id
    session['user_name'] = f"{user.first_name} {user.last_name}"
    flash("Inscription réussie. Vous êtes maintenant connecté.", "success")
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['user_name'] = f"{user.first_name} {user.last_name}"
        flash('Connexion réussie !', 'success')
        return redirect(url_for('admin'))
    flash('Email ou mot de passe incorrect.', 'danger')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Déconnexion réussie.', 'info')
    return redirect(url_for('index'))

@app.route('/supprimer_produit', methods=['POST'])
def supprimer_produit():
    id = request.form.get('id')
    if not id:
        return "Erreur : id manquant", 400

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM panier WHERE id = %s", (id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for('produits'))

@app.route('/clear_panier_flag')
def clear_panier_flag():
    session.pop('panier_ajoute', None)
    return '', 204

@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form.get('id')
    if not user_id:
        flash("ID utilisateur manquant.", "danger")
        return redirect(url_for('user_list'))

    try:
        conn = get_db_connection()  # ouvrir connexion (à adapter)
        cur = conn.cursor()
        # Suppression dans la table users (adapter le nom de table/colonne si besoin)
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        cur.close()
        conn.close()
        flash("Utilisateur supprimé avec succès.", "success")
    except Exception as e:
        flash(f"Erreur lors de la suppression : {e}", "danger")

    return redirect(url_for('user_list')
)

# Exemple de route pour afficher la liste des utilisateurs
import psycopg2.extras

@app.route('/users')
def user_list():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT id, first_name, last_name, email FROM "users" ORDER BY id')
    users = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('users.html', users=users)


    # Rendre le template, en passant la liste des utilisateurs
    return render_template('users.html', users=users)

# --- LANCEMENT DE L'APPLICATION ---
if __name__ == '__main__':
    app.config.update(SESSION_COOKIE_SAMESITE="Lax")
    app.run(debug=True)
