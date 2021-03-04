# WebScrapper -- Maison Du Monde

This repository is a scrapper of french decoration site Maison du Monde. The aim is to collect the most popular mirror and carpet


## Installation
The project is currently in a development environment. To install and run the it, you have to create docker container. Here is the step to do it. In your command line, you have to write :

    docker run -itd --name flask_scrapping -w /app -v `pwd`:/app --network my_scrap_net python
 
    docker run -itd --name scrap_sql MYSQL_ROOT_PASSWORD=123 --network my_scrap_net mysql

Now that our containers are running, the last step is to execute it. You have to write those commands line :

    docker exec -it flask_scrapping bash
    docker exec -it -uroot scrap_sql mysql -p123

## Technologies

In this project, we used a lot of different technologies. To name them, there was : 
 - Python							
 - mySQL
 - HTML
 - CSS
 - Jinja
 
 #
 ### Packages

It's the same for python packages, we used :


 1. bs4
 2. requests
 3. Flask
 4. Flask-Cors
 5. Jinja2
 6. mysql-connector-python
 7. Unidecode
 
 You can install them locally or in your python docker container if you write this command line :

    pip install bs4 requests Flask Flask-Cors Jinja2 mysql-connector-python Unidecode

## Files and Organisations

In this project, all the files are interconnected to produce the final result.
There one file that do the scrapping of the website named `my_scrap.py`.
In it, we have two classes, one for carpets articles and another for the mirrors. All the function calls are in the `main.py` that returns, in each function, one list of tupples that includes all the data.

Then, we used those two functions to create and insert the data in a sql database that is located in the `file_db.py`. We have another file that cleans article duplicate and send mails of the new items in the `mail_bdd.py`.

Finally, we used the python package flask to create an API, with different routes and arguments, and a frontend. This files are located in `flask_api.py`, in the folder `templates` you will find an `index.html` and in the folder `static` the `style.css`


## Next step

In the near futur, we will implement a more user friendly frontend with the use of Jinja templating.

 - [ ] Creating a search bar
 - [ ] Implementing a filter system 
 - [ ] Functionnality to send email to user
 - [ ] having a proper test file to make sure that my code is sustainable
 #
 
# French

Ce repositoire Github consiste à scrapper le site Maison du Monde afin de récupérer les miroirs et les tapis les plus populaires. 

## Installation
Le projet est, pour le moment, construit sur un evironnement de developpement, pour pouvoir l'utiliser, il est nécessaire de faire tourner des container docker. Pour ce faire, il vous suffit d'écrire ces lignes de commandes :

    docker run -itd --name flask_scrapping -w /app -v `pwd`:/app --network my_scrap_net python
    
    docker run -itd --name scrap_sql MYSQL_ROOT_PASSWORD=123 --network my_scrap_net mysql
    
Maintenant que les containers sont initiés, la prochaine étape est de les exécuter. Il faut d'écrire ceci dans votre terminal :

    docker run -itd --name flask_scrapping -w /app -v `pwd`:/app --network my_scrap_net python
    
    docker run -itd --name scrap_sql MYSQL_ROOT_PASSWORD=123 --network my_scrap_net mysql

## Technologies
Dans ce projet, nous avons utilisées différentes technologies dont : 
 - Python							
 - mySQL
 - HTML
 - CSS
 - Jinja
 
 #
 ### Package
 
 Le meme organisation s'applique pour les package de python :

 1. bs4
 2. requests
 3. Flask
 4. Flask-Cors
 5. Jinja2
 6. mysql-connector-python
 7. Unidecode
 
Vous pouvez les installer en local ou dans votre conteneur python en écrivant cette ligne de commande :


    pip install bs4 requests Flask Flask-Cors Jinja2 mysql-connector-python Unidecode


## Fichiers et organisation

Dans ce projet, tout les fichiers sont connectés afin de produire le résultat final. Nous avons un fichier `main.py` qui réalise la partie scrapping du site.
Il est structuré avec deux classes, une pour les mirroirs et une pour les tapis. Tout les appels de fonctions sont effectués dans le `main.py`. A l'intérieur de celui-ci, il y a deux fonctions qui retournent pour chacune, un tupple avec toutes les informations collectés.

Après cela, nous avons utilisé ces deux fonction pour créer et insérer les données dans une base sql, situé dans `file_db.py`. Nous avons un autre fichier qui supprime les articles doublons et qui permet d'envoyer des mails pour les nouveaux éléments present dans la base de données situé dans `mail_bdd.py`.

Enfin, nous avons créer une API et un front end avec le package Flask de python contenant plusieurs routes et arguments. Le tout est présent dans le fichier `flask_api.py`, dans le fichiers `templates` nous avons le fichier `index.html` et dans le dossier `static` le ficher `style.css`.

## Prochaine amélioration
Dans un futur proche, nous allons ajouter un frontend puls adaptée pour l'utilisateur avec les templates de Jinja.

 - [ ] Avoir une barre de recherche
 - [ ] Implementer un systeme de filtre
 - [ ] Possibilité d'envoyer des mail à l'utilisateur
 - [ ] Avoir un fichier test pour s'assurer que tout mon code est viable
