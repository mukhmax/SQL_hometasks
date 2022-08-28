import psycopg2
from pprint import pprint
from dotenv import load_dotenv
import os
from psycopg2.errors import UniqueViolation, SyntaxError

load_dotenv()
database_name = os.getenv('DATABASE_NAME')
username = os.getenv('SQL_USER')
password = os.getenv('SQL_PASS')
conn = psycopg2.connect(database=database_name, user=username, password=password)


def create_table(table_name, **kwargs):
    query = f'CREATE TABLE IF NOT EXISTS {table_name}('
    counter = 0
    arguments = list(kwargs)
    for arg, limits in kwargs.items():
        counter += 1
        if counter == len(arguments):
            query += arg + ' ' + limits + ');'
        else:
            query += arg + ' ' + limits + ', '
    try:
        cur.execute(query)
        conn.commit()
        print('Таблица успешно создана.')
    except SyntaxError:
        print('Введены неверные данные для создания таблицы.')


def delete_table(table_name):
    query = f"""DROP TABLE IF EXISTS {table_name};"""
    cur.execute(query)
    conn.commit()
    print('Таблица успешно удалена.')


def client_search(**kwargs):
    values = ({'first_name': None, 'last_name': None, 'email': None, 'phone_number': None})
    if 'first_name' in kwargs.keys():
        values['first_name'] = kwargs['first_name']
    if 'last_name' in kwargs.keys():
        values['last_name'] = kwargs['last_name']
    if 'email' in kwargs.keys():
        values['email'] = kwargs['email']
    if 'phone_number' in kwargs.keys():
        values['phone_number'] = kwargs['phone_number']
    cur.execute("""
    SELECT c.client_id, c.first_name, c.last_name, c.email, p.phone_number FROM clients c
    LEFT JOIN phones p ON c.client_id = p.client_id WHERE
    first_name = %(first_name)s OR
    last_name = %(last_name)s OR
    email = %(email)s OR
    phone_number = %(phone_number)s
    """, values)
    search_result = cur.fetchall()
    if search_result:
        pprint(search_result)
    else:
        print('Указанных данных в базе не обнаружено.')


class Client:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def add_(self):
        values = ({'first_name': self.first_name,
                   'last_name': self.last_name,
                   'email': self.email})
        cur.execute("""
        SELECT * FROM clients
        WHERE email = %(email)s""", values)
        check = cur.fetchone()
        if check:
            print('Клиент с таким адресом электронной почты уже есть в базе данных.')
            return
        else:
            cur.execute("""
            INSERT INTO clients(first_name, last_name, email)
            VALUES(%(first_name)s, %(last_name)s, %(email)s);""", values)
        conn.commit()
        print('Запись о клиенте успешно внесена.')

    def add_phone(self, phone_number):
        values = ({'first_name': self.first_name,
                   'last_name': self.last_name,
                   'email': self.email})
        cur.execute("""
        SELECT client_id FROM clients
        WHERE first_name = %(first_name)s AND last_name = %(last_name)s AND email = %(email)s;""", values)
        check = cur.fetchone()
        if check:
            client_id = check[0]
        else:
            print('Такого клиента нет в базе данных.')
            return
        values = ({'phone_number': phone_number, 'client_id': client_id})
        try:
            cur.execute("""
            INSERT INTO phones(phone_number, client_id)
            VALUES(%(phone_number)s, %(client_id)s)""", values)
            conn.commit()
            print('Телефон успешно записан.')
        except UniqueViolation:
            print('Такой номер телефона уже есть в базе данных.')

    def client_change(self, client_id):
        cur.execute("SELECT client_id FROM clients;")
        check = cur.fetchall()
        if not (client_id,) in check:
            print('Клиента с таким ID нет в базе данных.')
            return
        values = ({'client_id': client_id,
                   'first_name': self.first_name,
                   'last_name': self.last_name,
                   'email': self.email})
        try:
            cur.execute("""
            UPDATE clients
            SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
            WHERE client_id = %(client_id)s""", values)
            conn.commit()
            print('Запись успешно обновлена.')
        except UniqueViolation:
            print('Такой адрес электронной почты уже есть в базе данных.')

    def phone_delete(self):
        values = ({'first_name': self.first_name,
                   'last_name': self.last_name,
                   'email': self.email})
        cur.execute("""
        SELECT client_id FROM clients
        WHERE first_name = %(first_name)s AND last_name = %(last_name)s AND email = %(email)s;""", values)
        check = cur.fetchone()
        if check:
            client_id = check[0]
        else:
            print('Такого клиента нет в базе данных.')
            return
        values = ({'client_id': client_id})
        cur.execute("""
        SELECT phone_id, phone_number from phones p
        JOIN clients c on p.client_id = c.client_id
        WHERE c.client_id = %(client_id)s;""", values)
        phones_list = cur.fetchall()
        if phones_list:
            print('Список номеров клиента:')
            pprint(phones_list)
        else:
            print('В базе данных отсутствует информация о телефонных номерах клиента.')
            return
        cur.execute("SELECT COUNT(*) FROM phones;")
        phones_number_old = cur.fetchone()
        delete_id = int(input('Какой номер Вы хотите удалить (введите ID номера)?)  '))
        values = ({'delete_id': delete_id})
        cur.execute("""DELETE FROM phones WHERE phone_id=%(delete_id)s;""", values)
        conn.commit()
        cur.execute("SELECT COUNT(*) FROM phones;")
        phones_number_new = cur.fetchone()
        if phones_number_old > phones_number_new:
            print('Номер успешно удален.')
        else:
            print('В базе данных нет телефона с таким ID')

    def client_delete(self):
        values = ({'first_name': self.first_name,
                   'last_name': self.last_name,
                   'email': self.email})
        cur.execute("""
        SELECT client_id FROM clients
        WHERE first_name = %(first_name)s AND last_name = %(last_name)s AND email = %(email)s;""", values)
        check = cur.fetchone()
        if check:
            client_id = check[0]
        else:
            print('Такого клиента нет в базе данных.')
            return
        values = ({'client_id': client_id})
        cur.execute("""
        DELETE FROM phones WHERE client_id=%(client_id)s;
        DELETE FROM clients WHERE client_id=%(client_id)s""", values)
        conn.commit()
        print('Информация о клиенте успешно удалена.')


if __name__ == '__main__':
    with conn.cursor() as cur:
        # delete_table('clients')
        # delete_table('phones')
        create_table('clients',
                     client_id='SERIAL PRIMARY KEY',
                     first_name='VARCHAR(60) NOT NULL',
                     last_name='VARCHAR(60) NOT NULL',
                     email='VARCHAR(255) UNIQUE NOT NULL')
        create_table('phones',
                     phone_id='SERIAL PRIMARY KEY',
                     phone_number='VARCHAR(15) UNIQUE NOT NULL',
                     client_id='INT REFERENCES clients(client_id) NOT NULL')
        # new_client = Client(first_name='Alexander', last_name='Alekseev', email='aleks@mail.ru')
        # new_client.add_()
        # new_client.add_phone('+79319563815')
        # client_update = Client(first_name='Maxim', last_name='Mukhin', email='mqwe@gmail.com')
        # client_update.add_()
        # client_update.phone_delete()
        # client_update.client_change(1)
        # client_update.client_delete()
        # client_search(first_name='Maxim', last_name='Mukhin')
