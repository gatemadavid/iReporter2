import psycopg2
import psycopg2.extras
import os

url = os.getenv('DATABASE_TEST_URL')
DATABASE_URL = os.getenv('DATABASE_URL', url)


def connection(url):
    conn = psycopg2.connect(DATABASE_URL)
    return conn


def init_db():
    con = connection(DATABASE_URL)
    return con


def create_tables():
    conn = connection(DATABASE_URL)
    curr = conn.cursor()
    queries = tables()
    for query in queries:
        curr.execute(query)
    conn.commit()


def tables():
    users_table = '''CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY,
        firstname char(20) NOT NULL,
        lastname char(20) NOT NULL,
        email char(50) NOT NULL,
        username char(20) NOT NULL,
        phone char(14) NOT NULL,
        isAdmin BOOLEAN DEFAULT False,
        password char(100) NOT NULL,
        registered DATE NOT NULL DEFAULT CURRENT_DATE)
    '''
    incidents_table = '''CREATE TABLE IF NOT EXISTS incidents(
        id serial PRIMARY KEY,
        title char(100) NOT NULL,
        incident char(50) NOT NULL,
        location char(100) NOT NULL,
        status char(30) DEFAULT 'Draft',
        description char(200) NOT NULL,
        images char(100) NOT NULL,
        createdBy char(100) NOT NULL,
        createdOn DATE NOT NULL DEFAULT CURRENT_DATE)    '''

    queries = [users_table, incidents_table]
    return queries


def destroy_tables():
    conn = connection(url)
    curr = conn.cursor()
    users_table = ''' DROP TABLE IF EXISTS users CASCADE'''
    incidents_table = ''' DROP TABLE IF EXISTS incidents CASCADE'''
    queries = [users_table, incidents_table]
    for query in queries:
        curr.execute(query)
    conn.commit()
