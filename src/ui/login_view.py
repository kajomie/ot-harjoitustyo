from tkinter import StringVar, Tk, ttk, constants
import tkinter as tk
from application.card_service import card_service, WrongUsernameOrPassword
from repositories.user_repository import UserRepository

class LoginView:
    def __init__(self, root, handle_register, handle_logging_in):
        self._root = root
        self._handle_register = handle_register
        self._handle_logging_in = handle_logging_in
        self._frame = None
        self._username_field = None
        self._password_field = None
        self._card_service = card_service
        self._error_label = None
        self._myvar = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_field.get()
        password = self._password_field.get()

        try:
            self._card_service.login(username, password)
            self._handle_logging_in()
        except WrongUsernameOrPassword:
            self._show_error_message()

    def _show_error_message(self):
        self._myvar.set("Väärä käyttäjätunnus tai salasana!")

    def _hide_error_message(self):
        self._myvar.set("")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header = tk.Frame(master=self._frame, background="#6140c6", height=150)
        footer = tk.Frame(master=self._frame, background="#6140c6", height=150)
        main = tk.Frame(master=self._frame, background="#f4f4fd")

        header.pack(side="top", fill="x")
        footer.pack(side="bottom", fill="x")
        main.pack(side="top", fill="both", expand=True)

        header_title = ttk.Label(master=header, text="Kirjaudu sisään", font=("Helvetica", 22), background="#6140c6")
        header_title.pack(side="left", padx=50, pady=50)

        header_style = ttk.Style()
        header_style.configure("header.TLabel", foreground="white")
        header_title.configure(style="header.TLabel")
        
        login_frame = tk.Frame(master=main, width=500, height=500, background="#f4f4fd")
        login_frame.pack(padx=50, pady=50)

        self._myvar = StringVar()
        self._myvar.set("")
        self._error_label = ttk.Label(master=login_frame, textvariable=self._myvar, foreground="red", background="#f4f4fd")
        self._error_label.pack(padx=10, pady=15)

        username_text = ttk.Label(master=login_frame, text="Käyttäjänimi", background="#f4f4fd")
        self._username_field = ttk.Entry(master=login_frame)

        password_text = ttk.Label(master=login_frame, text="Salasana", background="#f4f4fd")
        self._password_field = ttk.Entry(master=login_frame, show="*")

        login_button = ttk.Button(master=login_frame, text="Kirjaudu sisään", command=self._login_handler)

        username_text.pack(padx=5, pady=5)
        self._username_field.pack(padx=5, pady=5)
        password_text.pack(padx=5, pady=5)
        self._password_field.pack(padx=5, pady=5)
        login_button.pack(padx=5, pady=5)
        
        register_button = ttk.Button(master=header, text="Rekisteröidy", command=self._handle_register)
        register_button.pack(side="right", padx=50)

        self._hide_error_message()
    