import psycopg2
from app import app


def create_post(name, date, comment):
    conn = psycopg2.connect(    
            host = 'ec2-18-209-187-54.compute-1.amazonaws.com',
            database = 'd8hto9mvtubuln',
            user = 'kmdvxvuvocjhha',
            password = 'ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3',
            port = 5432
    )
    cur = conn.cursor()
    cur.execute('INSERT INTO testdb (date, name, commment) VALUES (now(), ?, ?)', (name, comment))

    conn.commit()

    conn.close()

def get_posts():
    conn = psycopg2.connect(
        host = 'ec2-18-209-187-54.compute-1.amazonaws.com',
        database = 'd8hto9mvtubuln',
        user = 'kmdvxvuvocjhha',
        password = 'ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3',
        port = 5432
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM testdb")
    posts = cur.fetchall()
    return posts