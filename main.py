
"""
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants:
1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.
L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses:
Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
    Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
    L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.
"""

# us import the files API, DATABASE and APP with every method specific to the files
import database
from api import Api
from app import App
# dictionnary for stoked the categories
categories = {1: "pizza",
              2: "fish",
              3: "meat",
              4: "cheese",
              5: "vegetables",
              6: "fruits"
              }

# var for stocked the limit of each categories              
length=[0]
# var for stoked the number of products of each categories
size=[]
# methode/fonction main()
def main():
    # var for the loop while
    run=True
    # instance database "import file database.py"
    db = database
    # methode drop_db() => drop of the database
    db.drop_db()
    # methode create_db() => creation of the database 
    db.create_db()
    # var for stoked the number of the limite and size of the products per categories 
    nb = 0
    # loop for each categories used for iterating over a sequence "dictionnary"
    for row in categories:
        x = Api(categories[row]).get_data_api()
        nb += x
        size.append(x)
        length.append(nb)
    app = App()
    while run == True:
        #a loop, hes creats a list with all categories
        for row in categories:
            print(row, categories[row])
        # a loop, if choice is not between 1 and 6
        nb_not_allowed = True
        while nb_not_allowed:

            try:
                choice_caterogie = int(
                    input("Enter a number between 1 and 6: "))
                choice_categories = categories[choice_caterogie]
                nb_not_allowed = False

            except KeyError:
                print("please enter a between 1 and 6, you introduced a wrong number ")

                pass
            except ValueError:
                print(
                    "please enter a number between 1 and 6")

        # condiction for enter in the category pizza
        if choice_categories == "pizza":
            print((1, length[0], length[1], size[0]))
            app.display_choice_of_products(1,length[0],length[1],size[0])
            
            #nb_not_allowed = False
        # condiction for enter in the category fish
        if choice_categories == "fish":
            app.display_choice_of_products(2, length[1], length[2], size[1])
            
            #nb_not_allowed = False
        # condiction for enter in the category meat
        if choice_categories == "meat":
            app.display_choice_of_products(3, length[2], length[3], size[2])
            
            #nb_not_allowed = False
        # condiction for enter in the category cheese
        if choice_categories == "cheese":
            app.display_choice_of_products(4, length[3], length[4], size[3])
            
            #nb_not_allowed = False
        # condiction for enter in the category vegetables
        if choice_categories == "vegetables":
            app.display_choice_of_products(5, length[4], length[5], size[4])
            
            #nb_not_allowed = False
        # condiction for enter in the category fruits
        if choice_categories == "fruits":
            app.display_choice_of_products(6, length[5], length[6], size[5])
            
            #nb_not_allowed = False
        # condition for exit or continue
        if app.run_app == False:

            choice_for_exit_or_continue = input("[Y/N] You want choice another category? ")
            if choice_for_exit_or_continue == "N":
                run = False

            if choice_for_exit_or_continue == "Y":
                app.re_init()



# when python execut this script he's using one special variable __name__
# so, if python execut this script... my function main() can be executed
if __name__ == "__main__":

    main()
