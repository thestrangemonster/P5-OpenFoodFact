import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import database.database


class Api:

    def __init__(self, category):
        # variable with parameter category
        self.categories = category
        # variable with URL for to search in the API of apenfoodfacts
        self.url = 'https://world.openfoodfacts.org/cgi/search.pl'
        # dictionnary with all parameter for to search
        self.parameters = {
            'page_size': 55,
            'search_terms': self.categories,
            'search_simple': 1,
            'sort_by': 'unique_scans_n',
            'action': 'process',
            'json': 1
        }
        # self.r is a variable with method requests.get for wrap the data
        self.r = requests.get(self.url, self.parameters)
        # the datas are json files
        self.r = self.r.json()
        # in the json files selected the products 
        self.r = self.r['products']
        # calcul the number of products in each category 
        self.size_of_category = 0
        # instance of the files database 
        self.db = database.database
        # used the method Category for to 
        # configure the db with the right parameter
        self.data = self.db.Category(category_name=self.categories)
        # a list for to stock all product
        self.data.products = []


    # method for get data api and set in the db
    def get_data_api(self):
        # loop 
        for product in self.r:
            # try except
            try:
                self.product_name = product['product_name']
                self.nutri_score = product['nutrition_grades']
                self.store = product['stores_tags']
                self.url = product['url']
                # var data with data 
                data = self.db.Product(
                                        product_name=self.product_name,
                                        nutri_score=self.nutri_score,
                                        stores_tags=self.store,
                                        url=self.url
                                    )
                # the datas are now in the list
                self.data.products.append(data)
                # the nb of products for each categories
                self.size_of_category += 1
            except KeyError:
                pass
            except UnicodeEncodeError:
                pass
        # push the datas in the db
        self.db.set_data(self.data)
        # return the nb of each categories
        return self.size_of_category