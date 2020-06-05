from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy 
from models import *
import psycopg2



app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://kmdvxvuvocjhha:ac9a4385919971b6c4d5695d7dce03df8a45e3cc9a8f31f78a985593754222f3@ec2-18-209-187-54.compute-1.amazonaws.com:5432/d8hto9mvtubuln'


@app.route('/clear')
def clear():
    delete_table()
    return redirect(url_for('index'))



@app.route('/', methods = ['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        create_table()

    if request.method == 'POST':
        complete = request.form.get('complete')
        date = request.form.get('date')
        comment = request.form.get('comment')
        create_table()
        try:
            create_post(date, complete, comment)
        except:
            print('FUCKING FAILURE')
            update_table(date)
    posts = get_posts()

    return render_template('index.html', posts=posts)



if __name__ == "__main__":
    app.run(debug=True)
