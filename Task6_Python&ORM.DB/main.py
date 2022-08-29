import sqlalchemy
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker
from models import create_tables, delete_tables, Publisher, Book, Shop, Stock, Sale
import json


def shop_filter(publisher_id):
    for c in session.query(Shop).join(Stock, Shop.id == Stock.id_shop). \
            join(Book, Stock.id_book == Book.id).join(Publisher, Book.id_publisher == Publisher.id). \
            filter(Publisher.id == publisher_id).all():
        print(c)


def tables_input(file):
    with open(file) as t:
        data = json.load(t)

    for raw in data:
        if raw['model'] == 'publisher':
            publisher = Publisher(id=raw['pk'], name=raw['fields']['name'])
            session.add(publisher)
        elif raw['model'] == 'book':
            book = Book(id=raw['pk'], title=raw['fields']['title'], id_publisher=raw['fields']['id_publisher'])
            session.add(book)
        elif raw['model'] == 'shop':
            shop = Shop(id=raw['pk'], name=raw['fields']['name'])
            session.add(shop)
        elif raw['model'] == 'stock':
            stock = Stock(id=raw['pk'], id_book=raw['fields']['id_book'],
                          id_shop=raw['fields']['id_shop'], count=raw['fields']['count'])
            session.add(stock)
        elif raw['model'] == 'sale':
            sale = Sale(id=raw['pk'], price=raw['fields']['price'], date_sale=raw['fields']['date_sale'],
                        id_stock=raw['fields']['id_stock'], count=raw['fields']['count'])
            session.add(sale)
    session.commit()


load_dotenv()
database_name = os.getenv('DATABASE_NAME')
user = os.getenv('SQL_USER')
password = os.getenv('SQL_PASS')
DSN = f'postgresql://{user}:{password}@localhost:5432/{database_name}'
engine = sqlalchemy.create_engine(DSN)

# create_tables(engine)
# delete_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

tables_input('tests_data.json')
shop_filter(publisher_id=2)

session.close()
