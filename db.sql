CREATE DATABASE agriculture;

CREATE TABLE legume (
    id SERIAL PRIMARY KEY,                  -- Identifiant unique
    nom VARCHAR(100) NOT NULL,              -- Nom du produit
    prix NUMERIC(5,2) NOT NULL,             -- Prix du produit
    unite VARCHAR(20) DEFAULT 'kg',         -- Unité de mesure (kg, pièce, etc.)
    image VARCHAR(255),                     -- Nom du fichier image (ex: image1.jpg)
    categorie VARCHAR(50),                  -- Catégorie du produit (ex: top_selling, new_arrival)
    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Date d'ajout du produit
);


INSERT INTO legume(nom, prix, unite, image, categorie)VALUES 
('Chou_de_bruxelles', 0.75, 'kg', 'chou_de_bruxelles-removebg-preview.png', 'top_selling'),
('Tomate', 1.00, 'kg', 'tomate-removebg-preview.png', 'top_selling'),
('Petit_pois', 0.50, 'kg', 'petit_pois-removebg-preview.png', 'top_selling'),
('Piment', 0.50, 'kg', 'piment-removebg-preview.png', 'top_selling'),
('Gingembre', 10.00, 'kg', 'gingembre-removebg-preview.png', 'new_products'),
('Cornichon', 10.00, 'kg', 'cornichon-removebg-preview.png', 'new_products'),
('Oignon', 10.00, 'kg', 'oignon-removebg-preview.png', 'new_products'),
('Batavia', 0.50, 'kg', 'batavia-removebg-preview.png', 'publication'),
('Carotte', 10.00, 'kg', 'carotte-removebg-preview.png', 'publication'),
('Ciboulette', 10.00, 'kg', 'ciboulette-removebg-preview.png', 'publication'),
('Brocoli', 10.00, 'kg', 'brocoli-removebg-preview.png', 'publication'),
('Betterave', 10.00, 'kg', 'betterave-removebg-preview.png', 'publication'),
('Oignon_rouge', 10.00, 'kg', 'oignon_rouge-removebg-preview.png', 'publication'),
('Fenouil', 10.00, 'kg', 'fenouil-removebg-preview.png', 'publication'),
('Flageolet', 10.00, 'kg', 'flageolet-removebg-preview.png', 'publication');



CREATE TABLE graines (
    id SERIAL PRIMARY KEY,                       -- Identifiant unique auto-incrémenté
    nom VARCHAR(100) NOT NULL, 
    categorie VARCHAR(50),                   -- Nom du produit (obligatoire)
    prix NUMERIC(5,2) NOT NULL,                  -- Prix du produit (ex: 12.50)
    unite VARCHAR(20) DEFAULT 'kg',              -- Unité de mesure (par défaut 'kg')
    image VARCHAR(255),                          -- Nom du fichier image (ex: image1.jpg)                      -- Catégorie du produit (ex: top_selling, new_arrival)
    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Date d'ajout automatique
);


INSERT INTO graines (nom, categorie ,prix, unite, image) VALUES
('mais', 'top_selling', 1.20, 'kg', 'gettyimages.png'),
('mais', 'top_selling', 1.50, 'kg', 'gettyimages-2184106170.png'),
('riz', 'top_selling', 1.10, 'kg', 'rice-removebg-preview.png'),
('riz Blance','new_arrival', 2.00, 'kg', 'rizBlance-removebg-preview.png'),
('Riz','new_arrival', 2.50, 'kg', 'rizpreview.png'),
('graine','new_arrival', 1.80, 'kg', 'graine.JPG'),
('manioc','new_arrival', 3.00, 'kg', 'manioc-removebg-preview.png'),
('mais', 'top_selling', 2.20, 'kg', '71YLh8Gj8TL._AC_-removebg-preview.png'),
('rice', 'top_selling', 1.00, 'kg', 'rice.jpg'),
('oignon','new_arrival', 4.00, 'kg', 'oignon-removebg-preview.png'),
('echalotte', 'top_selling', 1.00, 'kg', 'echalotte-removebg-preview.png'),
('gingembre','new_arrival', 4.00, 'kg', 'gingembre-removebg-preview.png');




CREATE TABLE fruits (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    categorie VARCHAR(50),       -- "new arrival", "best product", "publication"
    description TEXT,
    prix DECIMAL(10, 2) NOT NULL,
    unite VARCHAR(20) DEFAULT 'kg', -- ou autre unité
    image VARCHAR(255),          -- chemin ou nom fichier image
    date_ajout TIMESTAMP DEFAULT NOW()
);


INSERT INTO fruits (nom, categorie, description, prix, unite, image) VALUES
('Orange', 'new arrival', 'Fruits and Vegetable', 0.75, 'kg', 'pexels-pixabay-161559-removebg-preview.png'),
('Pomme de terre', 'new arrival', 'Fruits and Vegetable', 1.00, 'kg', 'pomme de terre.png'),
('Mango', 'new arrival', 'Fruits and Vegetable', 0.50, 'kg', 'mango.png'),
('Orange Bricavile', 'new arrival', 'Fruits and Vegetable', 0.50, 'kg', 'mae-mu-U1iYwZ8Dx7k-unsplash-removebg-preview.png'),

('Ananas', 'best product', 'Best product', 10.00, 'kg', 'fernando-andrade-nAOZCYcLND8-unsplash-removebg-preview.png'),
('Fraise', 'best product', 'Best product', 10.00, 'kg', 'allec-gomes-xnRg3xDcNnE-unsplash-removebg-preview.png'),

('Coldenne', 'publication', 'Publication product', 0.50, 'kg', 'chris-dez-t2ZIt-WNXrk-unsplash-removebg-preview.png'),
('Banana', 'publication', 'Publication product', 2.00, 'kg', 'charlesdeluvio-0v_1TPz1uXw-unsplash-removebg-preview.png'),
('peche', 'publication', 'Publication product', 2.00, 'kg', 'peche.jpg'),
('Tomate', 'publication', 'Publication product', 1.00, 'kg', 'tomate-removebg-preview.png'),
('avocado', 'publication', 'Publication product', 1.20, 'kg', 'thought-catalog-9aOswReDKPo-unsplash.jpg'),
('Mais', 'publication', 'Publication product', 1.50, 'kg', 'mais-removebg-preview.png');


