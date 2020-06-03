import psycopg2
import os

#hello




def delete_table():
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

    conn = psycopg2.connect(    
            host = os.environ['DB_HOST'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USER_NAME'],
            password = os.environ['PASSWORD'],
            port = os.environ['DB_PORT']
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS zikr (id BIGSERIAL PRIMARY KEY NOT NULL, date DATE NOT NULL, complete VARCHAR(100) NOT NULL, comment VARCHAR(150) NOT NULL)")
    conn.commit()
    conn.close()




def create_post(date, complete, comment):
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