from tkinter import Tk, ttk, constants, StringVar
import tkinter as tk
from tkinter import *
from application.card_service import card_service

class CardView:
    def __init__(self, root, handle_front_page_view, handle_logging_out):
        self._root = root
        self._frame = None
        self._card_service = card_service
        self._user = self._card_service.get_user()
        self._cards = self._card_service.get_cards(self._user.id)
        self._handle_front_page_view = handle_front_page_view
        self._handle_logging_out = handle_logging_out
        self._current_card = None
        self._cardlist = None
        self._question_variable = None
        self._answer_variable = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        self._card_service.logout()
        self._handle_logging_out()

    def _select_card_handler(self):
        selected = self._cardlist.curselection()
        if selected:
            self._current_card = self._cards[selected[0]]
            self._show_selected_card()
        else:
            return

    def _show_selected_card(self):
        self._question_variable.set(self._current_card.question)
        self._answer_variable.set(self._current_card.answer)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header = tk.Frame(master=self._frame, background="#6140c6", height=150)
        footer = tk.Frame(master=self._frame, background="#6140c6", height=150)
        main = tk.Frame(master=self._frame, background="#f4f4fd")

        header.pack(side="top", fill="x")
        footer.pack(side="bottom", fill="x")
        main.pack(side="top", fill="both", expand=True)

        header_title = ttk.Label(master=header, text="Muistikorttisovellus", font=("Helvetica", 22), background="#6140c6")
        header_title.pack(side="left", padx=50, pady=50)

        header_style = ttk.Style()
        header_style.configure("header.TLabel", foreground="white")
        header_title.configure(style="header.TLabel")

        logout_button = ttk.Button(master=header, text="Kirjaudu ulos", command=self._logout_handler)
        logout_button.pack(side="right", padx=50)

        welcome_text_label = ttk.Label(master=header, background="#6140c6", text=f"Olet kirjautunut sisään käyttäjänä {self._user.username}")
        welcome_text_label.pack(side="right", padx=30)
        welcome_text_label.configure(style="header.TLabel")

        left_page_frame = tk.Frame(master=main, width=700, background="#d2d2f7")
        left_page_frame.pack(side="left", fill="y")
        right_page_frame = tk.Frame(master=main, background="#f4f4fd")
        right_page_frame.pack(side="right", fill="both", expand=True)

        browse_card_frame = tk.Frame(master=left_page_frame, background="#d2d2f7")
        browse_card_frame.pack(fill="both", expand=True)

        browse_card_label = ttk.Label(master=browse_card_frame, text="Selaa kortteja", font=("Helvetica", 16), background="#d2d2f7")
        browse_card_label.pack(side="top", pady=20, padx=50)

        lista = Listbox(browse_card_frame)
        lista.pack(side="left", fill="both", pady=20, padx=20)
        scroll = Scrollbar(browse_card_frame)
        scroll.pack(side="left", fill="y")
        lista.config(yscrollcommand=scroll.set)
        scroll.config(command=lista.yview)

        self._cardlist = lista

        for card in self._cards:
            lista.insert(END, card.question)

        select_button = ttk.Button(master=left_page_frame, text="Valitse kortti", command=self._select_card_handler)
        select_button.pack(side="bottom", padx=10, pady=10)

        self._question_variable = StringVar()
        self._question_variable.set("")
        question_label = ttk.Label(master=right_page_frame, textvariable=self._question_variable, background="#f4f4fd")
        question_label.pack(padx=10, pady=15)

        self._answer_variable = StringVar()
        self._answer_variable.set("")
        answer_label = ttk.Label(master=right_page_frame, textvariable=self._answer_variable, background="#f4f4fd")
        answer_label.pack(padx=10, pady=15)

        back_button = ttk.Button(master=footer, text="Takaisin etusivulle", command=self._handle_front_page_view)
        back_button.pack(side="left", padx=50, pady=50)
