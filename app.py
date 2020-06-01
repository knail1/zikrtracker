from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy 
import os
from models import *
import psycopg2
from connect import *




app = Flask(__name__)
SQLACHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']



@app.route('/clear')
def clear():
    delete_table()
    return redirect(url_for('index'))



@app.route('/', methods = ['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        comment = request.form.get('comment')
        create_table()
        create_post(date, name, comment)
    posts = get_posts()

    return render_template('index.html', posts=posts)



if __name__ == "__main__":
    app.run(debug=True)
