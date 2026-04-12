from tkinter import Tk, ttk
from ui.ui import UI

if __name__ == "__main__":
    app_window = Tk()
    app_window.attributes('-zoomed', True)
    app_window.title("Muistikorttisovellus")

    ui = UI(app_window)
    ui.start()

    app_window.mainloop()