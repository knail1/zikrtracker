import psycopg2






def delete_table():
    conn = psycopg2.connect(    
            host = os.environ['HOST_NAME'],
            user = os.environ['USERNAME'],
            password = os.environ['PASSWORD']
            port = os.environ['PORT']
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM testdb")
    conn.commit()
    conn.close()



    
def create_table():

    conn = psycopg2.connect(    
            host = os.environ['HOST_NAME'],
            database = 'd8hto9mvtubuln',
            user = os.environ['USERNAME'],
            password = os.environ['PASSWORD']
            port = os.environ['PORT']
    )
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS testdb (id BIGSERIAL PRIMARY KEY, date DATE NOT NULL, name VARCHAR(150) NOT NULL, comment VARCHAR(150) NOT NULL)')
    conn.commit()
    conn.close()




def create_post(date, name, comment):
    conn = psycopg2.connect(    
            host = os.environ['HOST_NAME'],
            database = os.environ['DB'],
            user = os.environ['USERNAME'],
            password = os.environ['PASSWORD']
            port = os.environ['PORT']
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO testdb (date, name, comment) VALUES (%s, %s, %s)", ('NOW()', name, comment)) 
    conn.commit()

    conn.close()

def get_posts():
    conn = psycopg2.connect(
        host = os.environ['HOST_NAME'],
        database = 'd8hto9mvtubuln',
        user = os.environ['USERNAME'],
        password = os.environ['PASSWORD']
        port = os.environ['PORT']
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM testdb")
    posts = cur.fetchall()
    return posts