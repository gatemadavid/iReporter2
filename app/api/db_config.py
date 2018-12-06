import psycopg2
import psycopg2.extras


url = "dbname='ireporter' host='localhost' port='5432' user='david' password='davie123'"


def connection(url):
    conn = psycopg2.connect(url)
    return conn


def init_db():
    con = connection(url)
    return con


def create_tables():
    conn = connection(url)
    curr = conn.cursor()
    queries = tables()
    for query in queries:
        curr.execute(query)
    conn.commit()


def tables():
    table1 = '''CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY,
        firstname char(20) NOT NULL,
        lastname char(20) NOT NULL,
        email char(50) NOT NULL,
        username char(20) NOT NULL,
        phone char(14) NOT NULL,
        isAdmin BOOLEAN NOT NULL,
        password char(100) NOT NULL,
        registered DATE NOT NULL DEFAULT CURRENT_DATE)
    '''
    table2 = '''CREATE TABLE IF NOT EXISTS incidents(
        id serial PRIMARY KEY,
        title char(100) NOT NULL,
        incident char(50) NOT NULL,
        location char(100) NOT NULL,
        status char(50) NOT NULL,
        description char(200) NOT NULL,
        createdBy char(100) NOT NULL,
        createdOn DATE NOT NULL DEFAULT CURRENT_DATE)
    '''

    queries = [table1, table2]
    return queries


def destroy_tables():
    db1 = ''' DROP TABLE IF EXISTS users CASCADE'''
    db2 = ''' DROP TABLE IF EXISTS incidents CASCADE'''
    queries = [db1, db2]
    return queries
