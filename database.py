from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.sql.expression import func, select

# var with the method declarative_base()
Base = declarative_base()
# var with name of user of the db
user = 'tom' # 'your_user_name'
# var with password of the db
password = 'root'  # 'your_password'
# var with the name of the host
host = 'localhost'  # 'your_host_name'
# var with the name of the db
database = 'test'  # 'your_database_name'
#var for the connection wit all parameter for to connect to the db
engine = create_engine(
    'postgresql://{}:{}@{}/{}'.format(user, password, host, database), echo=False)

# table category
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    category_name = Column(String)
# table product
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    product_name = Column(String)
    nutri_score = Column(String)
    stores_tags = Column(String)
    url = Column(String)
    category = relationship("Category", back_populates="products")

# table favorite
class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    favorite_id = Column(Integer, ForeignKey('products.id'))
    product_name = Column(String)
    product = relationship("Product", back_populates="favorites")

# method for creat the table in the db
def create_db():
    Category.products = relationship(
        "Product", order_by=Product.id, back_populates="category")
    Product.favorites = relationship(
        "Favorite", order_by=Favorite.id, back_populates="product")
    Base.metadata.create_all(engine)

# method for drop the table in the db
def drop_db():
    Category.products = relationship(
        "Product", order_by=Product.id, back_populates="category")
    Product.favorites = relationship(
        "Favorite", order_by=Favorite.id, back_populates="product")
    Base.metadata.drop_all(engine)

# method for set the datas in the db
def set_data(data):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(data)
    session.commit()

# method for get the datas in the db
def get_data(cat_select):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Product).filter(
        Product.category_id == cat_select).all()
    return result

# method for get the datas in the db => when you choice a product
def get_data_choice(number):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Product).filter_by(id=number)
    return result

# method for get the datas in the db => when you choice a product => return a substitute random
def get_data_random(cat_select):
    Session=sessionmaker(bind = engine)
    session=Session()
    result = session.query(Product).filter(
        Product.nutri_score == "a", Product.category_id == cat_select).order_by(func.random()).first()
    return result

# method for get the datas in the db => when you choice "f" show the favorites
def get_data_favorite():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Favorite).all()
    return result



