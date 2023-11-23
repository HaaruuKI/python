from flet import *
import flet as ft
import conexion as c



def main(page: ft.Page):   
    def login():
        email = tbEmail
        password = tbPassword
        try:
            login = c.auth.sign_in_with_email_and_password(email, password)
            print("Successfully logged in!")
        except:
            print("Invalid email or password")
        return
    page.update()


    def signup():
        email = tbEmail
        password = tbPassword
        try:
            user= c.auth.create_user_with_email_and_password(email, password)
        except:
            print("Email already exists")
            return
        ans = input("are you new user? [y/n]")

        if ans == 'n':
            login()
        
        elif ans == 'y':
            signup()
    page.update()

    t = ft.Text()
    title1 = ft.Text("\nIniciar sesion", style=ft.TextThemeStyle.DISPLAY_MEDIUM)
    tbEmail = ft.TextField(label="Correo", hint_text="Porfavor ingrese su correo")
    tbPassword = ft.TextField(label="Contraseña", hint_text="Porfavor ingrese su contraseña")
    btnSing_up = ft.ElevatedButton(text="Sign up")
    btnLog_in = ft.ElevatedButton(text="Log in")
    page.add(title1,tbEmail, tbPassword, btnSing_up,btnLog_in, t )
            

ft.app(target=main)
