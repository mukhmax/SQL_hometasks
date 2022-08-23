import psycopg2
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
database_name = os.getenv('DATABASE_NAME')
username = os.getenv('SQL_USER')
password = os.getenv('SQL_PASS')


def create_tables():
    conn = psycopg2.connect(database=database_name, user=username, password=password)
    with conn.cursor() as cur:
        cur.execute("""
                    DROP TABLE IF EXISTS phones;
                    DROP TABLE IF EXISTS clients;
                    """)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS clients(
                    client_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(60) NOT NULL,
                    last_name VARCHAR(60) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL
                    );
                    """)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS phones(
                    phone_id SERIAL PRIMARY KEY,
                    phone_number VARCHAR(15) UNIQUE NOT NULL,
                    client_id INT REFERENCES clients(client_id) NOT NULL
                    );
                    """)
        conn.commit()
    conn.close()


def client_search(**kwargs):
    conn = psycopg2.connect(database=database_name, user=username, password=password)
    with conn.cursor() as cur:
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
    conn.close()
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
        conn = psycopg2.connect(database=database_name, user=username, password=password)
        with conn.cursor() as cur:
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
            with conn.cursor() as cur:
                cur.execute("""
                INSERT INTO clients(first_name, last_name, email)
                VALUES(%(first_name)s, %(last_name)s, %(email)s);""", values)
                conn.commit()
        conn.close()
        print('Запись о клиенте успешно внесена.')

    def add_phone(self, phone_number):
        conn = psycopg2.connect(database=database_name, user=username, password=password)
        with conn.cursor() as cur_find:
            values = ({'first_name': self.first_name,
                       'last_name': self.last_name,
                       'email': self.email})
            cur_find.execute("""
            SELECT client_id FROM clients
            WHERE first_name = %(first_name)s AND last_name = %(last_name)s AND email = %(email)s;""", values)
            check = cur_find.fetchone()
            if check:
                client_id = check[0]
            else:
                print('Такого клиента нет в базе данных.')
                return
        with conn.cursor() as cur_find:
            cur_find.execute("SELECT phone_number FROM phones;")
            check = cur_find.fetchall()
            for number_tuple in check:
                if phone_number in number_tuple:
                    print('Такой номер уже есть в базе данных.')
                    return
        with conn.cursor() as cur:
            values = ({'phone_number': phone_number, 'client_id': client_id})
            cur.execute("""
                        INSERT INTO phones(phone_number, client_id)
                        VALUES(%(phone_number)s, %(client_id)s)""", values)
            conn.commit()
        conn.close()
        print('Телефон успешно записан.')

    def client_change(self, client_id):
        conn = psycopg2.connect(database=database_name, user=username, password=password)
        with conn.cursor() as cur_find:
            cur_find.execute("SELECT client_id FROM clients;")
            check = cur_find.fetchall()
            if not (client_id,) in check:
                print('Клиента с таким ID нет в базе данных.')
                return
        with conn.cursor() as cur:
            cur.execute("SELECT email FROM clients;")
            check = cur.fetchall()
            for email_tuple in check:
                if self.email in email_tuple:
                    print('Такой адрес электронной почты уже есть в базе данных.')
                    return
        with conn.cursor() as cur:
            values = ({'client_id': client_id,
                       'first_name': self.first_name,
                       'last_name': self.last_name,
                       'email': self.email})
            cur.execute("""
            UPDATE clients
            SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
            WHERE client_id = %(client_id)s""", values)
            conn.commit()
        conn.close()
        print('Запись успешно обновлена.')

    def phone_delete(self):
        conn = psycopg2.connect(database=database_name, user=username, password=password)
        with conn.cursor() as cur_find:
            values = ({'first_name': self.first_name,
                       'last_name': self.last_name,
                       'email': self.email})
            cur_find.execute("""
            SELECT client_id FROM clients
            WHERE first_name = %(first_name)s AND last_name = %(last_name)s AND email = %(email)s;""", values)
            check = cur_find.fetchone()
            if check:
                client_id = check[0]
            else:
                print('Такого клиента нет в базе данных.')
                return
        with conn.cursor() as cur_list:
            values = ({'client_id': client_id})
            cur_list.execute("""
            SELECT phone_id, phone_number from phones p
            JOIN clients c on p.client_id = c.client_id
            WHERE c.client_id = %(client_id)s;""", values)
            phones_list = cur_list.fetchall()
            if phones_list:
                print('Список номеров клиента:')
                pprint(phones_list)
            else:
                print('В базе данных отсутствует информация о телефонных номерах клиента.')
                return
        delete_id = int(input('Какой номер Вы хотите удалить (введите ID номера)?)  '))
        with conn.cursor() as cur:
            cur.execute("""
            SELECT phone_id FROM phones;""", values)
            phones_id_list = cur.fetchall()
            phones_id = []
            for phone_id_tuple in phones_id_list:
                phones_id.append(phone_id_tuple[0])
            if delete_id not in phones_id:
                print('В базе данных нет телефона с таким ID')
                self.phone_delete()
        with conn.cursor() as cur_delete:
            values = ({'delete_id': delete_id})
            cur_delete.execute("""
            DELETE FROM phones WHERE phone_id=%(delete_id)s;""", values)
            conn.commit()
        conn.close()
        print('Номер успешно удален.')

    def client_delete(self):
        conn = psycopg2.connect(database=database_name, user=username, password=password)
        with conn.cursor() as cur_find:
            values = ({'first_name': self.first_name,
                       'last_name': self.last_name,
                       'email': self.email})
            cur_find.execute("""
            SELECT client_id FROM clients
            WHERE first_name = %(first_name)s AND last_name = %(last_name)s AND email = %(email)s;""", values)
            check = cur_find.fetchone()
            if check:
                client_id = check[0]
            else:
                print('Такого клиента нет в базе данных.')
                return
        with conn.cursor() as cur_phones_delete:
            values = ({'client_id': client_id})
            cur_phones_delete.execute("""
            DELETE FROM phones WHERE client_id=%(client_id)s;
            DELETE FROM clients WHERE client_id=%(client_id)s""", values)
            conn.commit()
        conn.close()
        print('Информация о клиенте успешно удалена.')


if __name__ == '__main__':
    # create_tables()
    # new_client = Client(first_name='Alexander', last_name='Alekseev', email='aleks@mail.ru')
    # new_client.add_()
    # new_client.add_phone('+79319563811')
    # client_update = Client(first_name='Maxim', last_name='Mukhin', email='mqwe@gmail.com')
    # client_update.phone_delete()
    # client_update.client_change(10)
    # client_update.client_delete()
    client_search(first_name='Maksim', last_name='Ivanov')
