import flet as ft
from flet import *
import pyrebase
import time
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


def main(page: Page):
    
    tbEmailL = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPasswordL = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
    
    tbEmailR = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPasswordR = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
    def celsius(e):
        users = db.child("/temp/-NkGzBxN3mq2OJ2TluXJ/temp").get()
        resultado = Text(users.val())
        print(resultado)
        c.value = f"{resultado.value}"
        page.update()
        time.sleep(1)
    
    def farenheit(e):
        users = db.child("/temp/-NkCvGQtoIeXJknZDeBl/temperatura/1").get()
        resultado = Text(users.val())
        print(resultado)
        f.value = f"{resultado.value}"
        page.update()
        time.sleep(1)
        
    c = ft.Text() 
    f = ft.Text() 
    celsiuss = ElevatedButton(text="Actualizar C°", on_click=celsius)
    #farenheitt = ElevatedButton(text="Actualizar F°", on_click=farenheit)
    

    
    # page.add(btn, t)
    
    page.title = "Sensor de temperatura"

    print("Initial route:", page.route)

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Inciar Sesion")),
                    ElevatedButton(text="Iniciar Sesion",on_click=log_in),
                    ElevatedButton(text="Registrarse",on_click=sign_up)
                ],
            )
        )
        if page.route == "/log_in" or page.route == "/log_in":
            page.views.append(
                View(
                    "/log_in",
                    [
                        AppBar(title=Text("Inciar Sesion")),
                        tbEmailL,
                        tbPasswordL,
                        ElevatedButton(text="Iniciar Sesion", on_click=login),
                        ElevatedButton(text="Aun no estoy registrado", on_click=sign_up),
                    ],
                )
            )
        if page.route == "/sign_up" or page.route == "/sign_up":
            page.views.append(
                View(
                    "/sign_up",
                    [
                        AppBar(title=Text("Registrarse")),
                        tbEmailR,
                        tbPasswordR,
                        ElevatedButton(text="Registrarse", on_click=signup),
                        ElevatedButton(text="Ya estas registrado.", on_click=log_in),
                    ],
                )
            )
        if page.route == "/app":
            page.views.append(
                View(
                    "/app",
                    [
                        AppBar(title=Text("Sensor de temperatura"), bgcolor=colors.SURFACE_VARIANT),
                        ft.Text(value="Bienvenido"),
                        celsiuss,
                        #farenheitt,
                        c,
                        f,
                    ],
                )
            )
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def sign_up(e):
        page.go("/sign_up")

    def log_in(e):
        page.go("/log_in")
    def app(e):
        page.go("/app")

    page.go(page.route)
    
    def login(e):
        try:
            # login = auth.sign_in_with_email_and_password(tbEmailL.value, tbPasswordL.value)
            registrado = Text("Su registro fue exitoso")
            page.go("/app")
        except:
            print("Invalid email or password")
            return
    page.update()

    def signup(e):
        try:
            user= auth.create_user_with_email_and_password(tbEmailR.value, tbPasswordR.value)
            page.go("/log_in")
        except:
            print("Email already exists")
            return
    page.update()
    
    
ft.app(target=main)