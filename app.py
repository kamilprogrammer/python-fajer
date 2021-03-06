from email.policy import default
from pydoc import render_doc
from tkinter import *
from tkinter import ON
from turtle import onclick
from types import NoneType
from flask import Flask, render_template, redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import INTEGER, Integer
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import IntegerField, EmailField, SubmitField , StringField
from wtforms.validators import DataRequired
from flask_mail import Mail, Message
import os
import smtplib


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "kamil's key"

class Topsm(FlaskForm):
    name71 = StringField("الدرجة الاولى", validators=[DataRequired()])
    name72 = StringField("الدرجة الثانية", validators=[DataRequired()])
    name73 = StringField("الدرجة الثالثة", validators=[DataRequired()])
    name81 = StringField("الدرجة الاولى", validators=[DataRequired()])
    name82 = StringField("الدرجة الثانية", validators=[DataRequired()])
    name83 = StringField("الدرجة الثالثة", validators=[DataRequired()])
    name91 = StringField("الدرجة الاولى", validators=[DataRequired()])
    name92 = StringField("الدرجة الثانية", validators=[DataRequired()])
    name93 = StringField("الدرجة الثالثة", validators=[DataRequired()])
    Submit = SubmitField("ارسال")
#create a model 
class Students (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.Text(), nullable = False)
    name71 =  db.Column(db.Text(), nullable = False)
    name72 =  db.Column(db.Text(), nullable = False)
    name73 =  db.Column(db.Text(), nullable = False)
    name81 =  db.Column(db.Text(), nullable = False)
    name82 =  db.Column(db.Text(), nullable = False)
    name83 =  db.Column(db.Text(), nullable = False)
    name91 =  db.Column(db.Text(), nullable = False)
    name92 =  db.Column(db.Text(), nullable = False)
    name93 =  db.Column(db.Text(), nullable = False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)    



    #create a Text !
    def __repr__ (self):
        return '<Name %r>' % self.name


#the main page
@app.route('/')
def home ():
    return render_template('main.html')


# the unused blog
@app.route('/blog')

def blog ():
    return render_template('blog.html')

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
        server2 = smtplib.SMTP("smtp.gmail.com", 587)
        mmsg = 'new email signed in from the website the name is '+name+'  '+number+' '+email+'  '+phone
        server2.starttls()
        server2.login("kg0390217@gmail.com", "shisfemgekjynvwk")
        server2.sendmail ("kg0390217@gmail.com", "kg0390217@gmail.com",mmsg)


        msg1 = 'kamil is here because my package is just here!'
        server1 = smtplib.SMTP("smtp.gmail.com", 587)
        server1.starttls()
        server1.login("kg0390217@gmail.com", "shisfemgekjynvwk")
        server1.sendmail ("kg0390217@gmail.com", email, msg1)

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
@app.route('/Tops')
def Tops():
    return render_template('Tops.html')


@app.route('/sc' , methods =["GET", "POST"])
def sc ():
    if request.method == "POST":
       passm = request.form.get("pass")
       if passm == 'manager':
        form = Topsm()
        name71 = None
        if form.validate_on_submit():
            name71 = form.name71.data
            form.name71.data = ''

        return render_template('choose2.html', form=form, name71=name71)

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

@app.route('/bus')
def bus():
    return render_template('bus.html')


@app.route('/exam')
def exam():
    if request.method == 'POST':
        msg1 = 'kamil is here because my package is just here!'
        server1 = smtplib.SMTP("smtp.gmail.com", 587)
        server1.starttls()
        server1.login("kg0390217@gmail.com", "shisfemgekjynvwk")
        to = ['rjdata.sy@gmail.com' , 'al-fajer@gmail.com']
        server1.sendmail ("kg0390217@gmail.com", to, msg1)
        
    return render_template('exam.html')


@app.route('/noto')
def noto():
    return render_template('noto.html')

if __name__ == '__main__':
    app.run(debug=True)