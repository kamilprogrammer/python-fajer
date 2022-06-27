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
from flask_mail import Mail, Message
import os
import smtplib


app = Flask(__name__)
app.config['MAIL_SERVER '] = 'smtp.gmail.com'
app.config['MAIL_PORT '] = '456'
app.config['MAIL_USERNAME'] = 'kg0390217@gmail.com'
app.config['MAIL_PASSWORD'] = '123'
app.config['MAIL_USE_TLS '] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
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
        return render_template('choose.html')

@app.route('/register/s' , methods=['POST', 'GET'])
def registers ():
    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("number")
        email = request.form.get("email")
        phone = request.form.get("phonenumber")
        msg = 'kamil is here because my package is just here!'
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("kg0390217@gmail.com", "shisfemgekjynvwk")
        server.sendmail ("kg0390217@gmail.com", email, msg)

        if name  == '':
            return render_template('register.html')
        elif number  == '' :
            return render_template('register.html')
        elif email  == '':
            return render_template('register.html')
        elif phone  == '':
            return render_template('register.html')         
        else:
            return render_template('tables.html', number=number, phone=phone, name=name, email=email)
    return render_template('register.html')

@app.route('/sc' , methods =["GET", "POST"])
def sc ():
    if request.method == "POST":
       passm = request.form.get("pass")
       if passm == 'manager':
        return render_template('manager.html') 
    return render_template("privatesc.html")

@app.route('/true')
def true ():
    return render_template('true.html')
@app.route('/sure')
def sure ():
    return render_template('tables.html')

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




if __name__ == '__main__':
    app.run(debug=True)