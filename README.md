# SdfTown-sql

Ce projet vise à apporter de l'aide aux sans-abris en fournissant une plateforme en ligne où ils peuvent trouver des informations sur les produits disponibles, se connecter et s'inscrire pour accéder à des fonctionnalités supplémentaires. Le projet est mis en œuvre à l'aide de Python et Flask pour le backend, et il utilise une base de données SQL pour stocker les informations des utilisateurs et des produits.

## Comment lancer le projet

Pour exécuter ce projet sur votre propre machine, suivez ces étapes :

1. Clonez le référentiel depuis GitHub en utilisant la commande suivante :

   git clone https://github.com/Razner/SdfTown-sql.git

2. Accédez au répertoire BDD à l'aide de la commande `cd` :

   cd BDD/

3. Exécutez l'application en utilisant Python avec le fichier handler.py :

   python handler.py

L'application sera maintenant accessible localement à l'adresse http://127.0.0.1:5000/.

## Fonctionnalités du site

Le site offre les fonctionnalités suivantes :

- **Connexion** : Les utilisateurs peuvent se connecter à leurs comptes existants en fournissant leur email et leur mot de passe.

- **Inscription** : Les nouveaux utilisateurs peuvent créer un compte en fournissant leur prénom, nom, mot de passe, email et numéro de téléphone. Les données des utilisateurs sont stockées dans la base de données.

- **Produits** : Les utilisateurs connectés peuvent parcourir la liste des produits disponibles. Les informations sur les produits sont récupérées depuis la base de données.

- **Enregistrement des données** : Lorsqu'un nouvel utilisateur s'inscrit, ses informations sont enregistrées dans la base de données pour une utilisation ultérieure.

---