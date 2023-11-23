import pyrebase
# configuracion de firebase y apis
config = {   
  "apiKey": "AIzaSyCzc2iy_OesOvqJEu1QbXcatf1dJu-zm0o",
  "authDomain": "login-ef924.firebaseapp.com",
  "databaseURL": "https://login-ef924-default-rtdb.firebaseio.com",
  "projectId": "login-ef924",
  "storageBucket": "login-ef924.appspot.com",
  "messagingSenderId": "143538818303",
  "appId": "1:143538818303:web:0a8f539d624bd5936c90ca"
}

# Inicializa firebase
app = pyrebase.initialize_app(config)

auth = app.auth()

def login():
  print("log in...")
  email = input("Enter email: ")
  password = input("Enter password: ")
  try:
    login = auth.sign_in_with_email_and_password(email, password)
    print("Successfully logged in!")
  except:
    print("Invalid email or password")
  return

def signup():
  print("sign up...")
  email = input("Enter email: ")
  password = input("Enter password: ")
  try:
    user= auth.create_user_with_email_and_password(email, password)
  except:
    print("Email already exists")
    return
ans = input("are you new user? [y/n]")

if ans == 'n':
  login()
  
elif ans == 'y':
  signup()

