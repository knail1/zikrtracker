from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
import psycopg2

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:/user1:pass@localhost:5432/zikr'
db = SQLAlchemy(app)




@app.route("/")
def home():
    conn = psycopg2.connect(
            host = 'localhost',
            database = 'zikr',
            user = 'user1',
            password = 'pass'
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM zikr;")
    data = cur.fetchall()
    #for d in data:
    #    print(f"date {d[0]} zikr {d[1]} comment {d[2]}")
    cur.close()
    conn.close()
    return render_template('index.html', data=data)
    









if __name__ == "__main__":
    app.run(debug=True)
