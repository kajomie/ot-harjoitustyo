from tkinter import Tk, ttk, constants
import tkinter as tk
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.front_page_view import FrontPageView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_register_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = RegisterView(self._root, self._handle_show_login, self._show_login_view)

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(self._root, self._handle_show_register, self._handle_show_front_page_view)

        self._current_view.pack()

    def _show_front_page_view(self):
        self._hide_current_view()

        self._current_view = FrontPageView(self._root, self._handle_show_login)

        self._current_view.pack()

    def _handle_show_front_page_view(self):
        self._show_front_page_view()

    def _handle_show_login(self):
        self._show_login_view()

    def _handle_show_register(self):
        self._show_register_view()
