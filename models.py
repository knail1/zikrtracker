import psycopg2
import os

# hello


def delete_table():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB'],
            user=os.environ['USER_NAME'],
            password=os.environ['PASSWORD'],
            port=os.environ['DB_PORT']
        )
    except:
        print('Could not connect')
    cur = conn.cursor()
    cur.execute("DELETE FROM zikr")
    conn.commit()
    conn.close()


def create_table():

    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB'],
            user=os.environ['USER_NAME'],
            password=os.environ['PASSWORD'],
            port=os.environ['DB_PORT']
        )
    except:
        print('Could not connect')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS zikr (date DATE NOT NULL PRIMARY KEY, complete BOOLEAN NOT NULL, comment VARCHAR(150))")
    conn.commit()
    conn.close()


def create_post(date, complete, comment):
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB'],
            user=os.environ['USER_NAME'],
            password=os.environ['PASSWORD'],
            port=os.environ['DB_PORT']
        )
    except:
        print('Could not connect')
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO zikr (date, complete, comment) VALUES (%s, %s, %s)", (date, '1', comment))

    conn.commit()

    conn.close()


def get_posts():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB'],
            user=os.environ['USER_NAME'],
            password=os.environ['PASSWORD'],
            port=os.environ['DB_PORT']
        )
    except:
        print('Could not connect')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM zikr ORDER BY date DESC LIMIT 3")
        posts = cur.fetchall()
        return posts
    except:
        create_table()


def show_status(date):
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB'],
            user=os.environ['USER_NAME'],
            password=os.environ['PASSWORD'],
            port=os.environ['DB_PORT']
        )
    except:
        conn = psycopg2.connect(
            host='ec2-18-209-187-54.compute-1.amazonaws.com',
            database='d8hto9mvtubuln',
            user='kmdvxvuvocjhha',
            password='ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3',
            port=5432
        )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM zikr WHERE complete='1' ORDER BY date DESC LIMIT 1")
    results = cur.fetchall()
    return results
    conn.commit()
    conn.close()


def update_zikr(date):
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB'],
            user=os.environ['USER_NAME'],
            password=os.environ['PASSWORD'],
            port=os.environ['DB_PORT']
        )
    except:
        print('Could not connect')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM zikr WHERE date = '{date}'")
    row = cur.fetchall()
    completed = row[0][1]
    # if completed == True:
    #cur.execute(f"UPDATE zikr set complete = '0' where date = '{date}'")
    if completed == False:
        cur.execute(f"UPDATE zikr SET complete = '1' where date = '{date}'")
    elif completed == True:
        cur.execute(f"UPDATE zikr SET complete = '0' where date = '{date}'")

    conn.commit()
    conn.close()
