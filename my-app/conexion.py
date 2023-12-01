import pyrebase
# configuracion de firebase y apis
config = {   
"apiKey": "AIzaSyCzc2iy_OesOvqJEu1QbXcatf1dJu-zm0o",
  "authDomain": "login-ef924.firebaseapp.com",
  "databaseURL": "https://login-ef924-default-rtdb.firebaseio.com",
  "projectId": "login-ef924",
  "storageBucket": "login-ef924.appspot.com",
  "messagingSenderId": "143538818303",
  "appId": "1:143538818303:web:0a8f539d624bd5936c90ca",
  "measurementId": "G-PMD8DPPENH"
}

# Inicializa firebase
app = pyrebase.initialize_app(config)

auth = app.auth()

firebase = pyrebase.initialize_app(config)

db = firebase.database()