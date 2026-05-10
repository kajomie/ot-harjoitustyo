from tkinter import Tk
from ui.ui import UI

if __name__ == "__main__":
    app_window = Tk()
    app_window.geometry("1200x900")

    app_window.title("Muistikorttisovellus")

    ui = UI(app_window)
    ui.start()

    app_window.mainloop()
