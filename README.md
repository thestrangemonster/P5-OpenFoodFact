# P5-OpenFoodFact

L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants:
1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.
L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses:
Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
    Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
    L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.


projet 5 openclassrooms_utiliser_les_données_de_l_openfoodfacts

install brew

brew install python3

pip3 install virtualenv

=> télécharger le dossier github de ce liens: https://github.com/thestrangemonster/P5-OpenFoodFact

=> se rendre dans le dossier github téléchargé dans le terminal avec la commande cd

$ virtualenv -p python3 P5-OpenFoodFact

$ source P5-OpenFoodFact/bin/activate

$ pip3 install -r requirements.txt

$ deactivate => for exit

=============== postgresql ===============

$ psql postgres -U name_of_user 

$ CREATE DATABASE name_of_db;

$ GRANT ALL PRIVILEGES ON DATABASE name_of_db TO name_of_user ; 

=============== file database.py ===============

=> fill with your data

var with name of user of the db
###### user = 'your username'
var with password of the db
###### password = 'your password'
var with the name of the host
###### host = 'your host'
var with the name of the db
###### database = 'your database' 

=============== file main.py ===============

for run => python3 main.py