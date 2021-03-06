import tkinter
from tkinter import *
from tkinter.ttk import Combobox, Style
from pathlib import Path
from view.maskedentry import MaskedWidget
from ttkbootstrap import Style
from ttkbootstrap.widgets import Meter


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1280x768")
window.configure(bg="#FFFFFF")
window.resizable(False, False)
window.title("Morais Estacionamento")
window.iconphoto(True, tkinter.PhotoImage(file=relative_to_assets('icon.png')))
style = Style(theme='morais', themes_file=relative_to_assets("ttkbootstrap_themes.json"))
