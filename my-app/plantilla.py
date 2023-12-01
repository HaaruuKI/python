import flet as ft
from flet import *
import pyrebase
import time
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


def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text("Iniciar Sesion\n", style=ft.TextThemeStyle.DISPLAY_MEDIUM)
    page.add(title)

    page.add(
       ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Iniciar Sesion"),
            padding=20,
            width=800,
            col={"sm": 6, "md": 4, "xl": 2},
        ),
        
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Registrarse"),
            padding=20,
            width=800,
            col={"sm": 6, "md": 4, "xl": 2},
        ),
    )
    #login y register
    tbEmailL = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPasswordL = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
    
    tbEmailR = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPasswordR = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
    
    #App
    def celsius(e):
        users = db.child("/temp/-NkCvGQtoIeXJknZDeBl/temperatura/0").get()
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
    farenheitt = ElevatedButton(text="Actualizar F°", on_click=farenheit)
    



    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                   AppBar(title=Text("Inciar Sesion")),
                ],
            )
        )
        if page.route == "/log_in" or page.route == "/log_in":
            page.views.append(
                View(
                    "/log_in",
                    [
                        AppBar(title=Text("Inciar Sesion")),
                       
                    ],
                )
            )
        if page.route == "/sign_up" or page.route == "/sign_up":
            page.views.append(
                View(
                    "/sign_up",
                    [
                        AppBar(title=Text("Registrarse")),
                       
                    ],
                )
            )
        if page.route == "/app":
            page.views.append(
                View(
                    "/app",
                    [
                        AppBar(title=Text("Sensor de temperatura"), bgcolor=colors.SURFACE_VARIANT),
                        
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
ft.app(main)