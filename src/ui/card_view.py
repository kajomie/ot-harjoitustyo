from tkinter import Tk, ttk, constants
import tkinter as tk
from application.card_service import card_service

class CardView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._card_service = card_service
        self._user = self._card_service.get_user()

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header = tk.Frame(master=self._frame, background="#6140c6", height=150)
        footer = tk.Frame(master=self._frame, background="#6140c6", height=150)
        main = tk.Frame(master=self._frame, background="#f4f4fd")

        header.pack(side="top", fill="x")
        footer.pack(side="bottom", fill="x")
        main.pack(side="top", fill="both", expand=True)

        header_title = ttk.Label(master=header, text="Muistikorttisovellus", font=("Helvetica", 22), background="#6140c6")
        header_title.pack(padx=50, pady=50)

        header_style = ttk.Style()
        header_style.configure("header.TLabel", foreground="white")
        header_title.configure(style="header.TLabel")
        
        page_frame = tk.Frame(master=main, width=500, height=500, background="#f4f4fd")
        page_frame.pack(padx=50, pady=50)
