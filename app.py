from flask import Flask, render_template, redirect , flash
from flask import request
from flask_mysqldb import MySQL 
import random


app = Flask(__name__)   
app.debug = True

app.config['MYSQL_HOST'] = 'bwanmigpdmkdtpx8yccv-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'uh7mzypr7rklsvtp'
app.config['MYSQL_PASSWORD'] = '1XHjFIqX1nhdNHEFEiC3'
app.config['MYSQL_DB'] = 'bwanmigpdmkdtpx8yccv'
app.secret_key = 'root'

mysql = MySQL(app)

# The main page
@app.route('/')
def home ():
    return render_template('main.html')


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
    cur.execute("SELECT top71 , top72 , top73 , top81 , top82 , top83 , top91 , top92 , top93 FROM tops")
    data = cur.fetchall()
    cur.close()
    print(data)
    return render_template('Tops.html' , data=data)

# The managers page
@app.route('/sc' , methods =["GET", "POST"])
def sc ():
    if request.method == "POST":
        passm = request.form.get("pass")
        passm = passm.encode('utf-32')
        passm0 = 'manager'.encode('utf-32')
        if passm == passm0:
            return render_template('choose2.html' , methods=['POST' , 'GET'])
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

@app.route('/grades/' , methods=['POST' , 'GET'])
def exam():
    if request.method == 'POST':
        name71 = request.form['71']
        name72 = request.form['72']
        name73 = request.form['73']
        name81 = request.form['81']
        name82 = request.form['82']
        name83 = request.form['83']
        name91 = request.form['91']
        name92 = request.form['92']
        name93 = request.form['93']
        print(name93)
        cur  = mysql.connection.cursor()
        cur.execute("""UPDATE `tops` SET `id`='0',`top71`=%s , `top71`=%s """  ,  [name71  , name71])
        cur.execute("""UPDATE `tops` SET `id`='0',`top72`=%s , `top72`=%s """  , [name72 , name72])
        cur.execute("""UPDATE `tops` SET `id`='0',`top73`=%s , `top73`=%s """  , [name73 , name73])
        cur.execute("""UPDATE `tops` SET `id`='0',`top81`=%s , `top81`=%s """  , [name81 , name81])
        cur.execute("""UPDATE `tops` SET `id`='0',`top82`=%s , `top82`=%s """  , [name82 , name82])
        cur.execute("""UPDATE `tops` SET `id`='0',`top83`=%s , `top83`=%s """  , [name83 , name83])
        cur.execute("""UPDATE `tops` SET `id`='0',`top91`=%s , `top91`=%s """  , [name91 , name91])
        cur.execute("""UPDATE `tops` SET `id`='0',`top92`=%s , `top92`=%s """  , [name92 , name92])
        cur.execute("""UPDATE `tops` SET `id`='0',`top93`=%s , `top93`=%s """  , [name93 , name93])
        mysql.connection.commit()
        cur.close()
        flash("تم تغيير الأوائل")
        return redirect('/main')
        
    return render_template('grades.html')


@app.route('/noto/')
def noto():
    return render_template('noto.html')

@app.route("/Complaint/" , methods=['POST' , 'GET'])    
def Complaint():
    if request.method == 'POST':
        Complaint = request.form['Complaint']
        cur  = mysql.connection.cursor()
        cur.execute("""INSERT INTO `complaints`(`Complaint`) VALUES (%s)""" , [Complaint])
        mysql.connection.commit()
        cur.close()
        flash('تم ارسال الشكوى')
        return redirect('/main')


    return render_template('Complaint.html')

@app.route("/t_Complaint/" , )    
def t_Complaint():
        cur  = mysql.connection.cursor()
        cur.execute("""  SELECT `Complaint` FROM `complaints` WHERE 1  """)
        data1 = cur.fetchall()
        cur.close()
        return render_template('t_Complaint.html' , data=data1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)