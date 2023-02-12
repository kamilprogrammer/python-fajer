from  flask import Flask , session , render_template , flash
import pyrebase
app = Flask(__name__)
#Firebase code:
app.secret_key = 'kamIl044'
config = {
    'apiKey': "AIzaSyB92b3L8ZzB_HUeeWgSEvq1SgpbF-paukc",
    'authDomain': "fajer-school.firebaseapp.com",
    'projectId': "fajer-school",
    'storageBucket': "fajer-school.appspot.com",
    'messagingSenderId': "935840445144",
    'appId': "1:935840445144:web:f48027d09075a7fc7cddad",
    'databaseURL': ""
}


fireabse = pyrebase.initialize_app(config)
auth = fireabse.auth()
email = 'kg0390217@gmail.com'
password = 'kamIl044'

user = auth.sign_in_with_email_and_password(email , password)
print(user)

auth.send_email_verification(user['idToken'])
#to here firebase-end


#The App routes:
@app.route('/')
def index():
    render_template('index.html')
