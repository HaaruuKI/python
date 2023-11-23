import flet as ft
from flet import *
import conexion as c
import time


def main(page: Page):
    
    tbEmailL = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPasswordL = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
    
    tbEmailR = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPasswordR = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
            
    
    page.title = "Routes Example"

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
                        Text(""),
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
            login = c.auth.sign_in_with_email_and_password(tbEmailL.value, tbPasswordL.value)
            registrado = Text("Su registro fue exitoso")
            time.sleep(5)
            page.go("/app")
        except:
            print("Invalid email or password")
            return
    page.update()

    def signup(e):
        try:
            user= c.auth.create_user_with_email_and_password(tbEmailR.value, tbPasswordR.value)
            page.go("/log_in")
        except:
            print("Email already exists")
            return
    page.update()


ft.app(target=main)