import os
import psycopg2


def connect():
    try:
        conn = psycopg2.connect(
            host = os.environ['DB_HOST'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USER_NAME'],
            password = os.environ['PASSWORD'],
            port = os.environ['DB_PORT']
            )
        cur = conn.cursor()
    except:
        print('Unable to connect to Database')


def commit_close():
    connect()
    conn.commit()
    conn.close()