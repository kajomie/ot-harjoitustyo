from tkinter import Tk, ttk, constants
import tkinter as tk
from application.card_service import card_service
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

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_field.get()
        password = self._password_field.get()
        self._card_service.login(username, password)
        self._handle_logging_in()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header = tk.Frame(master=self._frame, background="#32567a", height=150)
        footer = tk.Frame(master=self._frame, background="#32567a", height=150)
        main = tk.Frame(master=self._frame, background="#e7eef5")

        header.pack(side="top", fill="x")
        footer.pack(side="bottom", fill="x")
        main.pack(side="top", fill="both", expand=True)

        header_title = ttk.Label(master=header, text="Kirjaudu sisään", font=("Helvetica", 20), background="#32567a")
        header_title.pack(padx=50, pady=50)

        header_style = ttk.Style()
        header_style.configure("header.TLabel", foreground="white")
        header_title.configure(style="header.TLabel")
        
        login_frame = tk.Frame(master=main, width=500, height=500, background="#e7eef5")
        login_frame.pack(padx=50, pady=50)

        username_text = ttk.Label(master=login_frame, text="Käyttäjänimi", background="#e7eef5")
        self._username_field = ttk.Entry(master=login_frame)

        password_text = ttk.Label(master=login_frame, text="Salasana", background="#e7eef5")
        self._password_field = ttk.Entry(master=login_frame, show="*")

        login_button = ttk.Button(master=login_frame, text="Kirjaudu sisään", command=self._login_handler)

        username_text.pack(padx=5, pady=5)
        self._username_field.pack(padx=5, pady=5)
        password_text.pack(padx=5, pady=5)
        self._password_field.pack(padx=5, pady=5)
        login_button.pack(padx=5, pady=5)

        register_label = ttk.Label(master=self._frame, text="Rekisteröi uusi käyttäjä")
        
        register_button = ttk.Button(master=self._frame, text="Rekisteröidy", command=self._handle_register)

        register_button.pack()
        register_label.pack()
    