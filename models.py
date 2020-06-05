import psycopg2
import os

#hello




def delete_table():
    try:
        conn = psycopg2.connect(
            host = 'ec2-18-209-187-54.compute-1.amazonaws.com',
            database = 'd8hto9mvtubuln',
            user = 'kmdvxvuvocjhha',
            password = 'ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3',
            port = 5432
        )
    except:
        conn = psycopg2.connect(    
            host = os.environ['DB_HOST'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USER_NAME'],
            password = os.environ['PASSWORD'],
            port = os.environ['DB_PORT']
        )
    cur = conn.cursor()
    cur.execute("DELETE FROM zikr")
    conn.commit()
    conn.close()



    
def create_table():

    try:
        conn = psycopg2.connect(
            host = 'ec2-18-209-187-54.compute-1.amazonaws.com',
            database = 'd8hto9mvtubuln',
            user = 'kmdvxvuvocjhha',
            password = 'ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3',
            port = 5432
        )
    except:
        conn = psycopg2.connect(    
            host = os.environ['DB_HOST'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USER_NAME'],
            password = os.environ['PASSWORD'],
            port = os.environ['DB_PORT']
        )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS zikr (date DATE NOT NULL PRIMARY KEY, complete BOOLEAN NOT NULL, comment VARCHAR(150))")
    conn.commit()
    conn.close()




def create_post(date, complete, comment):
    try:
        conn = psycopg2.connect(
            host = 'ec2-18-209-187-54.compute-1.amazonaws.com',
            database = 'd8hto9mvtubuln',
            user = 'kmdvxvuvocjhha',
            password = 'ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3',
            port = 5432
        )
    except:
        conn = psycopg2.connect(    
            host = os.environ['DB_HOST'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USER_NAME'],
            password = os.environ['PASSWORD'],
            port = os.environ['DB_PORT']
        )
    cur = conn.cursor()
    cur.execute("INSERT INTO zikr (date, complete, comment) VALUES (%s, %s, %s)", ('NOW()', '1', comment)) 
    conn.commit()

    conn.close()

def get_posts():
    try:
        conn = psycopg2.connect(
            host = 'ec2-18-209-187-54.compute-1.amazonaws.com',
            database = 'd8hto9mvtubuln',
            user = 'kmdvxvuvocjhha',
            password = 'ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3',
            port = 5432
        )
    except:
        conn = psycopg2.connect(    
            host = os.environ['DB_HOST'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USER_NAME'],
            password = os.environ['PASSWORD'],
            port = os.environ['DB_PORT']
        )
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM zikr")
        posts = cur.fetchall()
        return posts
    except:
        create_table()