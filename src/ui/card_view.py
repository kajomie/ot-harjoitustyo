from tkinter import Tk, ttk, StringVar, messagebox
import tkinter as tk
from tkinter import *
from application.card_service import card_service

class CardView:
    """Korttinäkymän luokka.
    """
    def __init__(self, root, handle_front_page_view, handle_logging_out):
        """CardView-luokan konstruktori.

        Args:
            root: Käyttöliittymän 'juuri', jonka sisään sivu rakentuu.
            handle_front_page_view: Etusivun tapahtumakäsittelijä.
            handle_logging_out: Uloskirjautumisen tapahtumakäsittelijä.
        """
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
        self._decks = self._card_service.get_decks(self._user.id)
        self._deck_options = None
        self._current_deck = None
        self._toggle_answer_button = None
        self._answer_is_showing = False
        self._delete_card_button = None
        self._edit_card_button = None
        self._showing_card_frame = None
        self._editing_frame = None

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

    def _clear_view(self):
        """Korttinäkymän oikean puolen tyhjennys.
        """
        self._question_variable.set("")
        self._answer_variable.set("")
        self._answer_is_showing = False
        self._toggle_answer_button.pack_forget()
        self._delete_card_button.pack_forget()
        self._edit_card_button.pack_forget()

    def _select_card_handler(self, event):
        """Valitun kortin tapahtumakäsittelijä.
        """
        self._clear_view()
        selected = self._cardlist.curselection()
        if selected:
            self._current_card = self._cards[selected[0]]
            self._show_selected_card()
        else:
            return

    def _show_selected_card(self):
        """Valitun kortin näyttäminen.
        """
        self._answer_variable.set("")
        self._answer_is_showing = False
        self._question_variable.set(self._current_card.question)
        self._toggle_answer_button.config(text="Näytä vastaus")
        self._toggle_answer_button.pack(padx=10, pady=10)
        self._delete_card_button.pack(side="bottom", anchor="e", padx=10, pady=10)
        self._edit_card_button.pack(side="bottom", anchor="e", padx=10, pady=10)

    def _toggle_show_answer(self):
        """Vastauksen näyttäminen, kun nappia painetaan.
        """
        if self._current_card is None:
            return

        if self._answer_is_showing:
            self._toggle_answer_button.config(text="Näytä vastaus")
            self._answer_is_showing = False
            self._answer_variable.set("")
        else:
            self._answer_variable.set(self._current_card.answer)
            self._toggle_answer_button.config(text="Piilota vastaus")
            self._answer_is_showing = True

    def _update_cards(self):
        """Korttilistauksen päivittäminen.
        """
        self._cardlist.delete(0, "end")
        for card in self._cards:
            self._cardlist.insert(END, card.question)

    def _filter_by_deck(self, event):
        """Korttien suodatus niiden pakan mukaan.
        """
        selected = self._deck_options.get()

        if selected:
            self._clear_view()
            self._current_card = None

            if selected == "(Näytä kaikki kortit)":
                self._current_deck = None
                self._cards = self._card_service.get_cards(self._user.id)
                self._update_cards()
            else:
                deck_id = None

                for d in self._decks:
                    if selected == d.name:
                        deck_id = d.id
                        self._current_deck = d

                if deck_id is not None:
                    self._cards = self._card_service.get_deck_cards(deck_id)
                    self._update_cards()
        else:
            return

    def _delete_card(self):
        """Kortin poistaminen.
        """
        confirm_delete = messagebox.askokcancel("askokcancel", "Haluatko varmasti poistaa tämän kortin?")

        if confirm_delete:
            self._card_service.delete_card(self._current_card.id)
            self._current_card = None
            self._clear_view()
            if self._current_deck is not None:
                self._cards = self._card_service.get_deck_cards(self._current_deck.id)
            else:
                self._cards = self._card_service.get_cards(self._user.id)
            self._update_cards()
            return
        else:
            return

    def _show_editing_view(self):
        """Muokkausnäkymän näyttäminen.
        """
        self._showing_card_frame.pack_forget()
        self._edit_question_field.delete(0, "end")
        self._edit_question_field.insert(0, self._current_card.question)
        self._edit_answer_field.delete(0, "end")
        self._edit_answer_field.insert(0, self._current_card.answer)
        self._editing_frame.pack()

    def _show_normal_view(self):
        """Muokkausnäkymän vaihtaminen tavalliseen korttinäkymään.
        """
        self._editing_frame.pack_forget()
        self._showing_card_frame.pack(fill="both", expand=True)

    def _edit_card(self):
        """Kortin muokkaus.
        """
        edited_question = self._edit_question_field.get()
        edited_answer = self._edit_answer_field.get()

        if not edited_question or not edited_answer:
            messagebox.showerror("showerror", "Kortin kysymys tai vastaus eivät saa olla tyhjiä!")
            return

        card_id = self._current_card.id
        user_id = self._user.id
        deck_id = self._current_card.deck_id
        self._current_card = self._card_service.edit_card(card_id, edited_question, edited_answer, user_id, deck_id)

        if self._current_deck is not None:
            self._cards = self._card_service.get_deck_cards(self._current_deck.id)
        else:
            self._cards = self._card_service.get_cards(self._user.id)

        self._update_cards()
        self._show_normal_view()
        self._show_selected_card()

    def _initialize(self):
        """Korttinäkymän alustaminen.
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

        filter_deck_label = ttk.Label(master=browse_card_frame, text="Suodata pakan mukaan:", background="#d2d2f7")
        filter_deck_label.pack(padx=5, pady=5)
        decklist = ["(Näytä kaikki kortit)"] + [pakka.name for pakka in self._decks]
        self._deck_options = ttk.Combobox(browse_card_frame, state="readonly")
        self._deck_options.set("(Näytä kaikki kortit)")
        self._deck_options["values"] = decklist
        self._deck_options.pack(padx=5, pady=5)
        self._deck_options.bind('<<ComboboxSelected>>', self._filter_by_deck)

        right_cardlist = Listbox(browse_card_frame)
        right_cardlist.pack(side="left", fill="both", pady=20, padx=20)
        scroll = Scrollbar(browse_card_frame)
        scroll.pack(side="left", fill="y")
        right_cardlist.config(yscrollcommand=scroll.set)
        scroll.config(command=right_cardlist.yview)

        self._cardlist = right_cardlist

        for card in self._cards:
            right_cardlist.insert(END, card.question)

        right_cardlist.bind('<<ListboxSelect>>',self._select_card_handler)

        self._showing_card_frame = tk.Frame(master=right_page_frame, background="#f4f4fd")
        self._showing_card_frame.pack(fill="both", expand=True)

        self._question_variable = StringVar()
        self._question_variable.set("")
        question_label = ttk.Label(master=self._showing_card_frame, textvariable=self._question_variable, background="#f4f4fd")
        question_label.pack(padx=10, pady=15)

        separator = ttk.Separator(self._showing_card_frame, orient='horizontal')
        separator.pack(fill="x", padx=20, pady=10)

        self._answer_variable = StringVar()
        self._answer_variable.set("")
        answer_label = ttk.Label(master=self._showing_card_frame, textvariable=self._answer_variable, background="#f4f4fd")
        answer_label.pack(padx=10, pady=15)

        self._toggle_answer_button = ttk.Button(master=self._showing_card_frame, text="Näytä vastaus", command=self._toggle_show_answer)
        self._toggle_answer_button.pack(padx=10, pady=10)
        self._toggle_answer_button.pack_forget()

        self._delete_card_button = ttk.Button(master=self._showing_card_frame, text="Poista kortti", command=self._delete_card)
        self._delete_card_button.pack(side="bottom", anchor="e", padx=10, pady=10)
        self._delete_card_button.pack_forget()

        self._edit_card_button = ttk.Button(master=self._showing_card_frame, text="Muokkaa korttia", command=self._show_editing_view)
        self._edit_card_button.pack(side="bottom", anchor="e", padx=10, pady=10)
        self._edit_card_button.pack_forget()

        self._editing_frame = tk.Frame(master=right_page_frame, background="#f4f4fd")
        edit_question_label = ttk.Label(master=self._editing_frame, text="Kysymys: ", background="#f4f4fd")
        edit_question_label.pack(padx=10, pady=15)
        self._edit_question_field = ttk.Entry(master=self._editing_frame)
        self._edit_question_field.pack(padx=5, pady=5)
        edit_answer_label = ttk.Label(master=self._editing_frame, text="Vastaus: ", background="#f4f4fd")
        edit_answer_label.pack(padx=10, pady=15)
        self._edit_answer_field = ttk.Entry(master=self._editing_frame)
        self._edit_answer_field.pack(padx=5, pady=5)
        save_edit_button = ttk.Button(master=self._editing_frame, text="Tallenna muutokset", command=self._edit_card)
        save_edit_button.pack(padx=10, pady=10)
        back_to_card_view_button = ttk.Button(master=self._editing_frame, text="Takaisin", command=self._show_normal_view)
        back_to_card_view_button.pack(padx=10, pady=10)
        self._editing_frame.pack_forget()

        back_button = ttk.Button(master=footer, text="Takaisin etusivulle", command=self._handle_front_page_view)
        back_button.pack(side="left", padx=50, pady=50)
