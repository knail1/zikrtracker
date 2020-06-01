import psycopg2
import os
from connect import *



def delete_table():
    connect()
    cur.execute("DELETE FROM testdb")
    commit_close()


    
def create_table():

    connect()
    cur.execute('CREATE TABLE IF NOT EXISTS testdb (id BIGSERIAL PRIMARY KEY, date DATE NOT NULL, name VARCHAR(150) NOT NULL, comment VARCHAR(150) NOT NULL)')
    commit_close()


def create_post(date, name, comment):
    connect()
    cur.execute("INSERT INTO testdb (date, name, comment) VALUES (%s, %s, %s)", ('NOW()', name, comment)) 
    commit_close()

def get_posts():
    connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM testdb")
    
    posts = cur.fetchall()
    return posts