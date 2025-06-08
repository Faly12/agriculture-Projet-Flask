CREATE DATABASE agriculture;

CREATE TABLE legume (
    id SERIAL PRIMARY KEY,                 
    nom VARCHAR(100) NOT NULL,              
    prix NUMERIC(5,2) NOT NULL,            
    unite VARCHAR(20) DEFAULT 'kg',         
    image VARCHAR(255),                     
    categorie VARCHAR(50),                 
    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);

CREATE TABLE graines (
    id SERIAL PRIMARY KEY,                      
    nom VARCHAR(100) NOT NULL, 
    categorie VARCHAR(50),                  
    prix NUMERIC(5,2) NOT NULL,                 
    unite VARCHAR(20) DEFAULT 'kg',              
    image VARCHAR(255),                                
    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);


CREATE TABLE fruits (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    categorie VARCHAR(50),       
    description TEXT,
    prix DECIMAL(10, 2) NOT NULL,
    unite VARCHAR(20) DEFAULT 'kg',
    image VARCHAR(255),          
    date_ajout TIMESTAMP DEFAULT NOW()
);