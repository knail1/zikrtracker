from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
import psycopg2



app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://kmdvxvuvocjhha:ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3@ec2-18-209-187-54.compute-1.amazonaws.com:5432/d8hto9mvtubuln'
db = SQLAlchemy(app)

try:
    conn = psycopg2.connect(
            host = 'ec2-18-209-187-54.compute-1.amazonaws.com',
            database = 'd8hto9mvtubuln',
            user = 'kmdvxvuvocjhha',
            password = 'ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3',
            port = 5432
    )
    cur = conn.cursor()

    print("database connected")
    query = "INSERT INTO testdb (id, date, name, comment) VALUES (2, NOW(), 'zakir', 'second test yo')"

    cur.execute(query)
    print('query successful')

    conn.commit()
    cur.close()
    conn.close()

    print("committed and closed")
except:
    print("something went WRONG")




def home():

    return render_template('index.html', data=data)
    









if __name__ == "__main__":
    app.run(debug=True)
