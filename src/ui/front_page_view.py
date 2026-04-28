from tkinter import Tk, ttk, constants
import tkinter as tk
from application.card_service import card_service

class FrontPageView:
    """Etusivun näkymän luokka.
    """
    def __init__(self, root, handle_logging_out, handle_card_view):
        """FrontPageView-luokan konstruktori.

        Args:
            root: Näkymän 'juuri', jonka sisään näkymä rakentuu.
            handle_logging_out: Uloskirjautumisen tapahtumakäsittelijä.
            handle_card_view: Korttinäkymän tapahtumakäsittelijä.
        """
        self._root = root
        self._frame = None
        self._card_service = card_service
        self._user = self._card_service.get_user()
        self._handle_logging_out = handle_logging_out
        self._handle_card_view = handle_card_view
        self._question_field = None
        self._answer_field = None
        self._deck_name_field = None
        self._decks = self._card_service.get_decks(self._user.id)
        self._deck_options = None

        self._initialize()

    def pack(self):
        """Näkymän näyttö.
        """
        self._frame.pack(fill="both", expand=True)

    def destroy(self):
        """Näkymän poisto.
        """
        self._frame.destroy()

    def _logout_handler(self):
        """Uloskirjautumisen tapahtumakäsittelijä.
        """
        self._card_service.logout()
        self._handle_logging_out()

    def _create_card_handler(self):
        """Uuden kortin luomisesta vastaava tapahtumakäsittelijä.
        """
        question = self._question_field.get()
        answer = self._answer_field.get()
        current_deck = self._deck_options.get()
        deck_id = None
        for d in self._decks:
            if current_deck == d.name:
                deck_id = d.id
        self._card_service.create_new_card(question, answer, deck_id)

    def _create_deck_handler(self):
        """Uuden pakan luomisesta vastaava tapahtumakäsittelijä.
        """
        deck_name = self._deck_name_field.get()
        self._card_service.create_new_deck(deck_name)

    def _initialize(self):
        """Etusivun näkymän alustus.
        """
        self._frame = ttk.Frame(master=self._root)
        header = tk.Frame(master=self._frame, background="#6140c6", height=150)
        footer = tk.Frame(master=self._frame, background="#6140c6", height=100)
        main = tk.Frame(master=self._frame, background="#f4f4fd")

        header.pack(side="top", fill="x")
        footer.pack(side="bottom", fill="x")
        main.pack(side="top", fill="both", expand=True)

        header_title = ttk.Label(master=header, text="Muistikorttisovellus", font=("Helvetica", 22), background="#6140c6")
        header_title.pack(side="left", padx=50, pady=50)

        header_style = ttk.Style()
        header_style.configure("header.TLabel", foreground="white")
        header_title.configure(style="header.TLabel")

        left_page_frame = tk.Frame(master=main, width=500, background="#d2d2f7")
        left_page_frame.pack(side="left", fill="y")
        right_page_frame = tk.Frame(master=main, background="#f4f4fd")
        right_page_frame.pack(side="right", fill="both", expand=True)

        logout_button = ttk.Button(master=header, text="Kirjaudu ulos", command=self._logout_handler)
        logout_button.pack(side="right", padx=50)

        welcome_text_label = ttk.Label(master=header, background="#6140c6", text=f"Olet kirjautunut sisään käyttäjänä {self._user.username}")
        welcome_text_label.pack(side="right", padx=30)
        welcome_text_label.configure(style="header.TLabel")

        create_card_frame = tk.Frame(master=left_page_frame, width=400, height=400, background="#6e6ee6")
        create_card_frame.pack(padx=20, pady=20)
        create_card_label = ttk.Label(master=create_card_frame, text="Luo uusi muistikortti", font=("Helvetica", 16), background="#6e6ee6", style="header.TLabel")
        create_card_label.pack(side="top", pady=20)

        question_label = ttk.Label(master=create_card_frame, text="Kysymys:", background="#6e6ee6", style="header.TLabel")
        self._question_field = ttk.Entry(master=create_card_frame)
        question_label.pack(padx=5, pady=5)
        self._question_field.pack(padx=5, pady=5)
        answer_label = ttk.Label(master=create_card_frame, text="Vastaus:", background="#6e6ee6", style="header.TLabel")
        self._answer_field = ttk.Entry(master=create_card_frame)
        answer_label.pack(padx=5, pady=5)
        self._answer_field.pack(padx=5, pady=5)
        choose_deck_label = ttk.Label(master=create_card_frame, text="Kortin pakka:", background="#6e6ee6", style="header.TLabel")
        choose_deck_label.pack(padx=5, pady=10)
        decklist = [pakka.name for pakka in self._decks]
        self._deck_options = ttk.Combobox(create_card_frame, state="readonly")
        self._deck_options.set("Valitse pakka")
        self._deck_options["values"] = decklist
        self._deck_options.pack(padx=5, pady=5)

        create_card_button = ttk.Button(master=create_card_frame, text="Luo uusi muistikortti", command=self._create_card_handler)
        create_card_button.pack(padx=50, pady=50)

        card_view_button = ttk.Button(master=right_page_frame, text="Selaa kortteja", command=self._handle_card_view)
        card_view_button.pack(padx=50, pady=50)

        create_deck_frame = tk.Frame(master=left_page_frame, width=400, height=400, background="#9999ed")
        create_deck_frame.pack(padx=20, pady=20)
        create_deck_label = ttk.Label(master=create_deck_frame, text="Luo uusi pakka", font=("Helvetica", 16), background="#9999ed", style="header.TLabel")
        create_deck_label.pack(side="top", padx=20, pady=20)
        deck_label = ttk.Label(master=create_deck_frame, text="Pakan nimi:", background="#9999ed", style="header.TLabel")
        self._deck_name_field = ttk.Entry(master=create_deck_frame)
        deck_label.pack(padx=5, pady=5)
        self._deck_name_field.pack(padx=40, pady=10)

        create_deck_button = ttk.Button(master=create_deck_frame, text="Luo uusi pakka", command=self._create_deck_handler)
        create_deck_button.pack(padx=5, pady=20)
