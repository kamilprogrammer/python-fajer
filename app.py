from operator import methodcaller
from types import NoneType
from flask import Flask, render_template, redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import INTEGER, Integer
from data import Posts
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///privatesc.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "kamil's key"
# create a form class

class NameForm (FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    P1 = IntegerField("tHE fathers phone number", validators=[DataRequired()])
    age = IntegerField('THe age')
    sub = SubmitField("Submit")
#create a model 
class Students (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name=  db.Column(db.String(50), nullable = False)

    #create a string !
    def __repr__ (self):
        return '<Name %r>' % self.name


#the main page
@app.route('/')
def home ():
    return render_template('main.html')


# the unused blog
@app.route('/blog')

def blog ():
    return render_template('blog.html', posts = Posts)

# register
@app.route('/register', methods = ['POST', 'GET'])

def register ():
        return render_template('register.html')

@app.route('/register/2' , methods=['POST', 'GET'])

def register2 ():
    return render_template('register2.html')

@app.route('/private/sc', methods=['POST', 'GET'])

def privatesc ():
   return render_template('privatesc.html')

@app.route('/products')

def products ():
    return render_template('products.html')


@app.route('/main')

def main ():
    return render_template('index.html')


@app.errorhandler(404)

def erorr404 (e):
    return render_template('404.html'), 404

@app.errorhandler(500)

def erorr500 (e):
    return render_template('404.html'), 404

@app.route('/sc', methods=['POST', 'GET'])
def sc ():
    name = None
    form  = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('privatesc.html', name=name, form = form)    



if __name__ == '__main__':
    app.run(debug=True)