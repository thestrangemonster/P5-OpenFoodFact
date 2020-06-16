import database
import random

class App:
    # method __init__() class
    def __init__(self):
        # init instance database
        self.db = database
        # init var for loop while
        self.run_app = True

    # methode's posting  the products 
    def display_choice_of_products(self,result,beging,end,size):
        # var beging for limit 
        self.beging = beging
        # var beging for limit
        self.end = end 
        # var for nb of pages
        self.nb_of_page = size // 10
        # var for residual of the last page
        self.residual = size % 10
        # var init of the first page
        self.page = 1
        # var get the data on the DB
        self.result = self.db.get_data(result)
        print('\n')
        print('**********************************************')
        # loop for post the products
        for row in self.result.products:
            if row.id >= self.beging and row.id <= self.beging + 9:
                print(row.id,row.product_name)

        #print('page {} sur {}'.format(self.page, self.a+1))
        # loop while 
        while self.run_app:
            print('\n')
            print('*************************INFO*************************')
            print('for to go to the next page push r')
            print('for to go to the previous page push l')
            print('for to select a choice enter the number of the product')
            print('for to show your favorite press f')
            print('for to quit the app press q')
            print('******************************************************')
            print('\n')
            # var with input for enter a number or navigate 
            self.push = input(
                "R ->, <- L or enter a number: ")
            # bloc with keys words try except
            try:
                # it's a condition if self push is a integer, so try excecut that 
                self.push = int(self.push)

                if self.push > end or self.push < beging:
                    print('enter the number in the list, thanks')

                else:
                    self.show_choice = self.db.get_data_choice(self.push)
                    for row in self.show_choice:
                        print(row.id,row.product_name)

                    self.show_substitute = self.db.get_data_choice(self.set_random_substitute())
                    for row in self.show_substitute:

                        print("the substitue is {} {}".format(
                            row.id, row.product_name))
                        print("available from {}".format(
                            row.stores_tags.replace("{", "").replace("}", "")))
                        print("fore more information {}".format(row.url))
                        
                        self.add_favorite = input(
                        "[Y/N] You want add this product to your favorites? : ")
                        if self.add_favorite == 'Y':

                            data = self.db.Favorite(product_name=row.product_name)
                            self.db.set_data(data)
                            print(row.id, row.product_name)

                        else:
                            pass                                        

            except ValueError:

                self.push = str(self.push)

                if self.push in ("l", "r", "q", "f"):
                    pass
                else:
                    print("sorry")

                if self.push == 'f':
                    self.show_favorite = self.db.get_data_favorite()
                    for row in self.show_favorite:
                        print(row.id,row.product_name)

                # R = RIGHT go to the next page
                if self.push == 'r':

                    if self.page >= self.nb_of_page:
                        self.beging = end - (self.residual - 1)
                        self.page = self.nb_of_page + 1
                        #print('\n')
                        #print(
                            #'***********************  {}  ***********************'.format(self.category.upper()))
                        for row in self.result.products:
                            if row.id >= self.beging and row.id <= self.end:
                                print(row.id, row.product_name)
                        print(self.page)
                        #print('page {} sur {}'.format())
                    else:
                        self.beging += 10
                        self.page += 1
                        #print('\n')
                        #print(
                            #'***********************  {}  ***********************'.format(self.category.upper()))
                        for row in self.result.products:
                            if row.id >= self.beging and row.id <= self.beging + 9:
                                print(row.id, row.product_name)
                        print(self.page)
                        #print('page {} sur {}'.format(page, nb_of_page))
               
                # L = LEFT go to the previous page
                if self.push == 'l':

                    if self.page == 1:
                        self.page = 1
                        self.beging = beging
                        #print('\n')
                        #print(
                            #'***********************  {}  ***********************'.format(self.category.upper()))
                        for row in self.result.products:
                            if row.id >= self.beging and row.id <= self.beging + 9:
                                print(row.id, row.product_name)
                        print(self.page)

                    else:
                        self.beging -= 10
                        self.page -= 1
                        #print('\n')
                        #print(
                            #'***********************  {}  ***********************'.format(self.category.upper()))
                        for row in self.result.products:
                            if row.id >= self.beging and row.id <= self.beging + 9:
                                print(row.id, row.product_name)
                        print(self.page)

                # Q = QUIT for quit the app
                if self.push == 'q':
                    #self.dbc.drop_table()
                    self.run_app = False

    # methode for random a number 
    def set_random_substitute(self):
        #random.randint(a, b)
        #Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
        self.substitute = random.randint(self.beging, self.end)
        return self.substitute


    # méthode for re init the methode __init__ of the class App
    def re_init(self):
        self.db = database
        self.run_app = True

