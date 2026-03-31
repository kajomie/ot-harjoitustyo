from tkinter import Tk, ttk, constants
import tkinter as tk

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        header = tk.Frame(self._root, background="#32567a", height=150)
        footer = tk.Frame(self._root, background="#32567a", height=150)
        main = tk.Frame(self._root, background="#e7eef5")

        header.pack(side="top", fill="x")
        footer.pack(side="bottom", fill="x")
        main.pack(side="top", fill="both", expand=True)
        
        register_frame = tk.Frame(master=main, width=500, height=500, background="#e7eef5")
        register_frame.pack(padx=50, pady=50)

        username_text = ttk.Label(master=register_frame, text="Käyttäjänimi", background="#e7eef5")
        username_field = ttk.Entry(master=register_frame)

        password_text = ttk.Label(master=register_frame, text="Salasana", background="#e7eef5")
        password_field = ttk.Entry(master=register_frame)

        confirm_password_text = ttk.Label(master=register_frame, text="Salasana uudestaan", background="#e7eef5")
        confirm_password_field = ttk.Entry(master=register_frame)

        register_button = ttk.Button(master=register_frame, text="Luo tunnus")

        username_text.pack(padx=5, pady=5)
        username_field.pack(padx=5, pady=5)
        password_text.pack(padx=5, pady=5)
        password_field.pack(padx=5, pady=5)
        confirm_password_text.pack(padx=5, pady=5)
        confirm_password_field.pack(padx=5, pady=5)
        register_button.pack(padx=5, pady=5)

