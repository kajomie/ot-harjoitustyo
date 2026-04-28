from tkinter import Tk, ttk, constants
import tkinter as tk
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.front_page_view import FrontPageView
from ui.card_view import CardView

class UI:
    """Käyttöliittymän luokka.
    """
    def __init__(self, root):
        """UI-luokan konstruktori.

        Args:
            root: Käyttöliittymän 'juuri', johon se rakennetaan.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Käyttöliittymän käynnistys.
        """
        self._show_register_view()

    def _hide_current_view(self):
        """Nykyisen näkymän piilotus.
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_register_view(self):
        """Rekisteröintinäkymän näyttäminen.
        """
        self._hide_current_view()

        self._current_view = RegisterView(self._root, self._handle_show_login, self._show_login_view)

        self._current_view.pack()

    def _show_login_view(self):
        """Sisäänkirjautumisnäkymän näyttäminen.
        """
        self._hide_current_view()

        self._current_view = LoginView(self._root, self._handle_show_register, self._handle_show_front_page_view)

        self._current_view.pack()

    def _show_front_page_view(self):
        """Etusivun näyttäminen.
        """
        self._hide_current_view()

        self._current_view = FrontPageView(self._root, self._handle_show_login, self._handle_show_card_view)

        self._current_view.pack()

    def _show_card_view(self):
        """Korttinäkymän näyttäminen.
        """
        self._hide_current_view()

        self._current_view = CardView(self._root, self._handle_show_front_page_view, self._handle_show_login)

        self._current_view.pack()

    def _handle_show_card_view(self):
        """Korttinäkymän tapahtumakäsittelijä.
        """
        self._show_card_view()

    def _handle_show_front_page_view(self):
        """Etusivun tapahtumakäsittelijä.
        """
        self._show_front_page_view()

    def _handle_show_login(self):
        """Sisäänkirjautumisnäkymän tapahtumakäsittelijä.
        """
        self._show_login_view()

    def _handle_show_register(self):
        """Rekisteröintinäkymän tapahtumakäsittelijä.
        """
        self._show_register_view()
