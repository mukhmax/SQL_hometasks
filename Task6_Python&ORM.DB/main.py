import sqlalchemy
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock


def shop_filter(publisher_id):
    for c in session.query(Shop).join(Stock, Shop.id == Stock.id_shop). \
            join(Book, Stock.id_book == Book.id).join(Publisher, Book.id_publisher == Publisher.id). \
            filter(Publisher.id == publisher_id).all():
        print(c)


load_dotenv()
database_name = os.getenv('DATABASE_NAME')
user = os.getenv('SQL_USER')
password = os.getenv('SQL_PASS')
DSN = f'postgresql://{user}:{password}@localhost:5432/{database_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# publisher1 = Publisher(name='Azbuka')
# publisher2 = Publisher(name='Terra')
#
# session.add_all([publisher1, publisher2])
# session.commit()
#
# book1 = Book(title='War and Peace', id_publisher=1)
# book2 = Book(title='Crime and Punishment', id_publisher=1)
# book3 = Book(title='Alice in Wonderland', id_publisher=2)
# book4 = Book(title='Harry Potter and the Chamber of Secrets', id_publisher=2)
#
#
# session.add_all([book1, book2, book3, book4])
# session.commit()
#
# shop1 = Shop(name='Book`s World')
# shop2 = Shop(name='All Books')
# shop3 = Shop(name='Books in City')
# shop4 = Shop(name='Book`s Home')
#
#
# session.add_all([shop1, shop2, shop3, shop4])
# session.commit()
#
# stock1 = Stock(id_book=1, id_shop=1, count=4)
# stock2 = Stock(id_book=1, id_shop=2, count=5)
# stock3 = Stock(id_book=1, id_shop=3, count=10)
# stock4 = Stock(id_book=2, id_shop=2, count=11)
# stock5 = Stock(id_book=3, id_shop=3, count=11)
# stock6 = Stock(id_book=3, id_shop=2, count=11)
# stock7 = Stock(id_book=4, id_shop=2, count=11)
# stock8 = Stock(id_book=4, id_shop=3, count=12)
# stock9 = Stock(id_book=4, id_shop=4, count=13)
#
#
# session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9])
# session.commit()

shop_filter(publisher_id=2)

session.close()
