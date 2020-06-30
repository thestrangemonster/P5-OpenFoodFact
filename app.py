import database
import random


class App:
    # method __init__() class
    def __init__(self):
        # init instance database
        self.db = database
        # init var for loop while
        self.run_app = True

    # methode's posting the products
    def display_choice_of_products(self, result, beging, end, size):
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
        for row in self.result:
            comparison_one = row.Product.id >= self.beging
            comparison_two = row.Product.id <= self.beging + 10
            if comparison_one and comparison_two:
                print(row.Product.id, row.Product.product_name)

        # loop while
        while self.run_app:

            # MENU
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
            sign = "r -> , <- l or "
            question = "What food do you want to replace?"
            order = " enter a number: "
            self.push = input("{}{}{}".format(sign, question, order))
            # bloc with keys words try except
            try:
                # it's a condition if self push is a integer,
                # so try excecut that
                self.push = int(self.push)

                if self.push > end or self.push < beging:
                    print('enter the number in the list, thanks')

                else:
                    # show the product,
                    # when your choice is a number in the list
                    self.show_choice = self.db.get_data_choice(self.push)
                    for row in self.show_choice:
                        print(row.id, row.product_name)
                    # show substitute
                    self.show_random = self.db.get_data_random(result)
                    print("the substitue is {} {}".format(
                        self.show_random.Product.id,
                        self.show_random.Product.product_name))
                    print("the nutri-score is {}".format(
                        self.show_random.Product.nutri_score))
                    print("available from {}".format(
                        self.show_random.Product.stores_tags.replace(
                            "{", "").replace("}", "")))
                    print("fore more information {}".format(
                        self.show_random.Product.url))
                    # if you want add favorite or not
                    # if you want add favorite or not
                    stc_choice = "[Y/N] "
                    stc = "Do you want add this product to your favorites? : "
                    self.add_favorite = input("{}{}".format(stc_choice, stc))

                    # Yes => the datas is set in the table favorites
                    if self.add_favorite == 'Y':
                        data = self.db.Favorite(
                            product_name=self.show_random.Product.product_name)
                        self.db.set_data(data)
                        print(self.show_random.Product.id,
                              self.show_random.Product.product_name)

                    else:
                        pass
            # if self.push is a string
            except ValueError:

                self.push = str(self.push)

                if self.push in ("l", "r", "q", "f"):
                    pass
                else:
                    print("sorry press l,r,f or q")

                if self.push == 'f':
                    self.show_favorite = self.db.get_data_favorite()
                    for row in self.show_favorite:
                        print(row.id, row.product_name)

                # R = RIGHT go to the next page
                if self.push == 'r':

                    if self.page >= self.nb_of_page:
                        self.beging = end - (self.residual - 1)
                        self.page = self.nb_of_page + 1
                        for row in self.result:
                            if row.Product.id >= self.beging and row.Product.id <= self.end:
                                print(row.Product.id, row.Product.product_name)
                        print(self.page)
                    else:
                        self.beging += 10
                        self.page += 1
                        for row in self.result:
                            if row.Product.id >= self.beging and row.Product.id <= self.beging + 10:
                                print(row.Product.id, row.Product.product_name)
                        print(self.page)
               
                # L = LEFT go to the previous page
                if self.push == 'l':

                    if self.page == 1:
                        self.page = 1
                        self.beging = beging
                        for row in self.result:
                            if row.Product.id >= self.beging and row.Product.id <= self.beging + 9:
                                print(row.Product.id, row.Product.product_name)
                        print(self.page)

                    else:
                        self.beging -= 10
                        self.page -= 1
                        for row in self.result:
                            if row.Product.id >= self.beging and row.Product.id <= self.beging + 9:
                                print(row.Product.id, row.Product.product_name)
                        print(self.page)

                # Q = QUIT for quit the app
                if self.push == 'q':
                    self.run_app = False


    # méthode for re init the methode __init__ of the class App
    def re_init(self):
        self.db = database
        self.run_app = True
