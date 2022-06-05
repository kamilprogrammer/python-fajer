from flask import Flask, render_template, redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from data import Posts
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///privatesc.db'
db = SQLAlchemy(app)
posts = Posts()



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self) :
        return '<Task %r>' % self.id
@app.route('/')
def home ():
    return render_template('main.html')



@app.route('/blog')

def blog ():
    return render_template('blog.html', posts = Posts)


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

def erorr404 (e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)