import flet as ft
from flet import *
import pyrebase
import time
import glob
# configuracion de firebase y apis
config = {   
"apiKey": "AIzaSyAuGyz4j365eCfXWWzroEI0boQEijRPKYM",
  "authDomain": "login-a34a4.firebaseapp.com",
  "databaseURL": "https://login-a34a4-default-rtdb.firebaseio.com",
  "projectId": "login-a34a4",
  "storageBucket": "login-a34a4.appspot.com",
  "messagingSenderId": "679574054351",
  "appId": "1:679574054351:web:440078f45043951bfc5eba",
  "measurementId": "G-L6CW5JFWRY"
}

# Inicializa firebase
app = pyrebase.initialize_app(config)

auth = app.auth()

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def main(page: ft.Page):  
    def button_clicked(e):
        users = db.child("/temp/-NkGzBxN3mq2OJ2TluXJ/temp").get()
        resultado = Text(users.val())
        print(resultado)
        t.value = f"Textboxes values are:  '{resultado.value}'."
        page.update()
        time.sleep(1)
        
    t = ft.Text() 
    btn = ElevatedButton(text="Actualizar", on_click=button_clicked)
    page.add(btn, t)
    

  
    
    
       
ft.app(target=main)