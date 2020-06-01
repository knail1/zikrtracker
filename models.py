import psycopg2
import os






def delete_table():
    conn = psycopg2.connect(    
            host = os.environ['DB_HOST'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USER_NAME'],
            password = os.environ['PASSWORD'],
            port = os.environ['DB_PORT']
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM testdb")
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
    cur.execute('CREATE TABLE IF NOT EXISTS testdb (id BIGSERIAL PRIMARY KEY, date DATE NOT NULL, name VARCHAR(150) NOT NULL, comment VARCHAR(150) NOT NULL)')
    conn.commit()
    conn.close()




def create_post(date, name, comment):
    conn = psycopg2.connect(    
            host = os.environ['DB_HOST'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USER_NAME'],
            password = os.environ['PASSWORD'],
            port = os.environ['DB_PORT']
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO testdb (date, name, comment) VALUES (%s, %s, %s)", ('NOW()', name, comment)) 
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
    cur.execute("SELECT * FROM testdb")
    posts = cur.fetchall()
    return posts