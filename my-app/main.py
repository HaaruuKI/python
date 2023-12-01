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

#Aplicacion
###############################################################################
def main(page: ft.Page):
  

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    title = ft.Text("Iniciar Sesion o Registrarse", style=ft.TextThemeStyle.DISPLAY_MEDIUM)

    #funciones de navegacion de pagina
    def sign_up(e):
        page.go("/sign_up")

    def log_in(e):
        page.go("/log_in")
    def app(e):
        page.go("/app")
    # Botones de inicio de sesion o registrarse
    btns = [
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Iniciar Sesion",width=2000, on_click=log_in),
            alignment=ft.alignment.center,
            padding=10,
            col={"sm": 6, "md": 4, "xl": 2},
        ),
            
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Registrarse",width=2000,on_click=sign_up),
            alignment=ft.alignment.center,
            padding=20,
            col={"sm": 6, "md": 4, "xl": 2},
        ),
    ]
    
    # Cuadro de texto de login y register
    tbEmailL = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPasswordL = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
    
    tbEmailR = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPasswordR = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
    
    #App
    def celsius(e):
        users = db.child("/temp/-NkCvGQtoIeXJknZDeBl/temperatura/0").get()
        resultado = Text(int(users.val()))
        print(resultado)
        c.value = f"{resultado.value} °C"
        page.update()
        time.sleep(1)
    
    def farenheit(e):
        users = db.child("/temp/-NkCvGQtoIeXJknZDeBl/temperatura/1").get()
        resultado = Text(int(users.val()))
        print(resultado)
        f.value = f"{resultado.value} °F"
        page.update()
        time.sleep(1)
        
    c = ft.Text(value="C°",size=50)
    f = ft.Text(value="F°",size=50)
    # celsiuss = ElevatedButton(text="Actualizar C°", on_click=celsius)
    # farenheitt = ElevatedButton(text="Actualizar F°", on_click=farenheit)
    
    titleApp = ft.Text("Preciona en los simbolos de C° o F° para mostrar la temperatura",size=20)
    tempC = [
        ft.Row(
        [
            ft.Container(
                c,
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=250,
                height=250,
                border_radius=10,
                on_click=celsius,
                col={"sm": 6, "md": 4, "xl": 2},
            ),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    ]
    tempF = [ft.Row([
        ft.Container(
                f,
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=250,
                height=250,
                border_radius=10,
                on_click=farenheit,
                col={"sm": 6, "md": 4, "xl": 2},

            ),
    ],alignment=ft.MainAxisAlignment.CENTER,)]
   
   

   

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Sensor de Temperatura")),
                    title,
                    *btns,
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
                        ElevatedButton(text="Iniciar Sesion",width=2000,on_click=login),
                        ElevatedButton(text="Aun no estoy registrado?",width=2000 , on_click=sign_up),
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
                        ElevatedButton(text="Registrarse", width=2000,on_click=signup),
                        ElevatedButton(text="Ya cuento con una cuenta.", width=2000,on_click=log_in),
                        
                    ],
                )
            )
        if page.route == "/app":
            page.views.append(
                View(
                    "/app",
                    [
                        AppBar(title=Text("Sensor de temperatura"), bgcolor=colors.SURFACE_VARIANT),
                        titleApp,
                        *tempC,
                        *tempF,
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

   

    page.go(page.route)
    
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Hello, world!"),
        action="Alright!",
    )
    
    def login(e):
        try:
            login = auth.sign_in_with_email_and_password(tbEmailL.value, tbPasswordL.value)
            page.go("/app")
        except:
            print("Invalid email or password")
            page.snack_bar = ft.SnackBar(ft.Text("El correo o la contraseña son invalidos",color="red",size=20))
            page.snack_bar.open = True
            page.update()
            return
    page.update()

    def signup(e):
        try:
            user= auth.create_user_with_email_and_password(tbEmailR.value, tbPasswordR.value)
            page.snack_bar = ft.SnackBar(ft.Text("El registro fue Exitoso",color="green",size=20))
            page.snack_bar.open = True
            page.update()
            page.go("/log_in")
        except:
            print("Email already exists")
            page.snack_bar = ft.SnackBar(ft.Text("El registro ha fallado",color="red",size=20))
            page.snack_bar.open = True
            page.update()
            return
    page.update()
ft.app(main)