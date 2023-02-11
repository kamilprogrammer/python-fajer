from flask import *
import pyrebase4

config = {
    'apiKey': "AIzaSyB92b3L8ZzB_HUeeWgSEvq1SgpbF-paukc",
    'authDomain': "fajer-school.firebaseapp.com",
    'projectId': "fajer-school",
    'storageBucket': "fajer-school.appspot.com",
    'messagingSenderId': "935840445144",
    'appId': "1:935840445144:web:f48027d09075a7fc7cddad"
}

fireabse = pyrebase4.initialize_app(config)
auth = fireabse.auth()