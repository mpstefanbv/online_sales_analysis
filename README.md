# Online Sales Analysis

Acest proiect reprezinta un sistem simplificat de analiza si gestionare a produselor si a cosului de cumparaturi, realizat in Python folosind programare orientata pe obiecte (OOP).  
Proiectul include si un flux Git complet: ramuri, imbinari, rezolvarea conflictelor si utilizarea fisierului `.gitignore` pentru securizarea datelor sensibile.

##  Functionalitati principale

### Gestionarea produselor
Implementata prin clasele `Product` și `ProductManager`:
- Adaugarea produselor
- Afisarea produselor
- Actualizarea cantitatii
- Calcularea valorii totale a inventarului
- Eliminarea produselor dupa nume

###  Gestionarea cosului de cumparaturi
Implementata prin clasa `Cart`:
- Adaugarea produselor in cos
- Afisarea continutului cosului
- Calcularea valorii totale de plata

## Structura proiectului
online_sales_analysis/ 
│
├── product.py
├── product_manager.py 
├── cart.py 
├── main.py 
├── .gitignore 
└── README.md

##  Clasele proiectului

### `Product`
Reprezinta un produs din magazin.
- **Atribute:** `name`, `price`, `quantity`
- **Metode:** afisare informatii, actualizare cantitate

### `ProductManager`
Gestioneaza lista de produse.
- **Atribute:** lista de produse
- **Metode:** adaugare, afisare, eliminare, valoare totala

### `Cart`
Gestioneaza cosul clientului.
- **Atribute:** `cart_items`
- **Metode:** adaugare in cos, afisare cos, valoare totala

##  Rulare proiect

In fisierul `main.py` sunt create instantele claselor si sunt demonstrate functionalitatile:

- Se creeaza produse
- Se adauga in manager
- Se selecteaza produse aleatoriu pentru cos
- Se afiseaza totalul de plata

Rulare: python main.py

## Securitate si .gitignore

Proiectul include un fisier `config.json` cu date sensibile (ex: chei API).  
Acesta este ignorat prin `.gitignore`, impreuna cu capturile de ecran: config.json *.png *.jpg *.jpeg *.gif

## Flux Git folosit

- Initializare proiect
- Creare ramuri pentru functionalitati:
  - `add-product-removal`
  - `add-cart-functionality`
- Imbinari si rezolvari de conflicte
- Commit-uri semnificative
- Push final pe GitHub

## Concluzie

Acest proiect demonstreaza:
- utilizarea OOP în Python,
- gestionarea inventarului si a cosului,
- lucrul profesionist cu Git si GitHub,
- utilizarea `.gitignore` pentru protectia datelor.

Proiectul poate fi extins cu:
- salvarea datelor în fisiere,
- interfata grafica,
- conectare la baze de date,
- API pentru gestionarea produselor.