from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
from models import *
import psycopg2



app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://kmdvxvuvocjhha:ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3@ec2-18-209-187-54.compute-1.amazonaws.com:5432/d8hto9mvtubuln'




@app.route('/', methods = ['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        comment = request.form.get('comment')
        create_post(date, name, comment)
    posts = get_posts()

    return render_template('index.html', posts=posts)



if __name__ == "__main__":
    app.run(debug=True)
