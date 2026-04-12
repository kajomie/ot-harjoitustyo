from tkinter import Tk, ttk, constants
import tkinter as tk
from application.card_service import card_service
from repositories.user_repository import UserRepository

class RegisterView:
    def __init__(self, root, handle_show_login, handle_create_new_user):
        self._root = root
        self._handle_show_login = handle_show_login
        self._handle_create_new_user = handle_create_new_user
        self._frame = None
        self._username_field = None
        self._password_field = None
        self._card_service = card_service

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _create_new_user_handler(self):
        username = self._username_field.get()
        password = self._password_field.get()

        self._card_service.create_new_user(username, password)
        self._handle_create_new_user()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header = tk.Frame(master=self._frame, background="#32567a", height=150)
        footer = tk.Frame(master=self._frame, background="#32567a", height=150)
        main = tk.Frame(master=self._frame, background="#e7eef5")

        header.pack(side="top", fill="x")
        footer.pack(side="bottom", fill="x")
        main.pack(side="top", fill="both", expand=True)

        header_title = ttk.Label(master=header, text="Rekisteröidy", font=("Helvetica", 20), background="#32567a")
        header_title.pack(padx=50, pady=50)

        header_style = ttk.Style()
        header_style.configure("header.TLabel", foreground="white")
        header_title.configure(style="header.TLabel")
        
        register_frame = tk.Frame(master=main, width=500, height=500, background="#e7eef5")
        register_frame.pack(padx=50, pady=50)

        username_text = ttk.Label(master=register_frame, text="Käyttäjänimi", background="#e7eef5")
        self._username_field = ttk.Entry(master=register_frame)

        password_text = ttk.Label(master=register_frame, text="Salasana", background="#e7eef5")
        self._password_field = ttk.Entry(master=register_frame, show="*")

        confirm_password_text = ttk.Label(master=register_frame, text="Salasana uudestaan", background="#e7eef5")
        confirm_password_field = ttk.Entry(master=register_frame, show="*")

        register_new_user_button = ttk.Button(master=register_frame, text="Luo tunnus", command=self._create_new_user_handler)

        username_text.pack(padx=5, pady=5)
        self._username_field.pack(padx=5, pady=5)
        password_text.pack(padx=5, pady=5)
        self._password_field.pack(padx=5, pady=5)
        confirm_password_text.pack(padx=5, pady=5)
        confirm_password_field.pack(padx=5, pady=5)
        register_new_user_button.pack(padx=5, pady=5)

        login_label = ttk.Label(master=self._frame, text="Kirjaudu sisään käyttäjänä")
        
        login_user_button = ttk.Button(master=self._frame, text="Kirjaudu sisään", command=self._handle_show_login)

        login_user_button.pack()
        login_label.pack()