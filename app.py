from base64 import decode
from encodings import utf_8
from enum import unique
from turtle import color
from flask import Flask, render_template, redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import IntegerField, EmailField, SubmitField , StringField
from wtforms.validators import DataRequired
from flask_mail import Mail, Message
import smtplib
from flask_mysqldb import MySQL 


app = Flask(__name__)   
app.debug = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'tops'

mysql = MySQL(app)

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

class Register_std(FlaskForm):
    name = StringField("الاسم الثلاثي", validators=[DataRequired()])
    email = StringField("الايميل", validators=[DataRequired()])
    phone = StringField("رقم للتواصل", validators=[DataRequired()])
    number = StringField("الصف", validators=[DataRequired()])
    sub = SubmitField("ارسال")

    def __repr__(self):
        return f'<User : {self.name}>'
# The main page
@app.route('/')

def home ():
    return render_template('main.html')



# The unused blog
@app.route('/blog')
def blog ():
    return render_template('gameswc.html')


# Register
@app.route('/register/', methods = ['POST', 'GET'])
def register ():
        return render_template('choose.html')
        
# register for std
@app.route('/register/s/')
def registers ():
    return render_template('download.html')

# The school leaderboard on the exams
@app.route('/Tops')
def Tops():
    cur  = mysql.connection.cursor()
    cur.execute("SELECT number1 , number2 , number3 FROM leaders")
    data = cur.fetchall()
    cur.close()

    return render_template('Tops.html' , data=data)

# The managers page
@app.route('/sc' , methods =["GET", "POST"])
def sc ():
    if request.method == "POST":
        passm = request.form.get("pass")
        passm = passm.encode('utf-32')
        passm0 = 'manager'.encode('utf-32')
        if passm == passm0:
            return render_template('choose2.html')
    return render_template("privatesc.html")

# it's only true!
@app.route('/true')
def true ():
    return render_template('true.html')

#it's only sure!    
@app.route('/sure')
def sure ():
    return render_template('tables.html')
# Don't matter only for debugging 
@app.route('/private/sc', methods=['POST', 'GET'])
def privatesc ():
   return render_template('privatesc.html')


# 75% I Will delete this route
@app.route('/products')
def products ():
    return render_template('products.html')


# The main page
@app.route('/main')
def main ():
    return render_template('index.html')

# The erorr 404
@app.errorhandler(404)
def erorr404 (e):
    return render_template('404.html'), 404


# The erorr 500
@app.errorhandler(500)
def erorr500 (e):
    return render_template('404.html'), 404


@app.route('/bus')
def bus():
    return render_template('bus.html')

@app.route('/game')
def game():
    return render_template('gameswc.html')
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
    app.run(host='0.0.0.0', debug=True)