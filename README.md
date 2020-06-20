# P5-OpenFoodFact

projet 5 openclassrooms_utiliser_les_données_de_l_openfoodfacts

install brew

brew install python3

pip3 install virtualenv

=> télécharger le dossier github de ce liens: 

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
