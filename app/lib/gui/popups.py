import tkinter as tk
from typing import Optional
from enum import Enum


class Images(Enum):
    LOGO = r"C:\Users\marco\OneDrive\Documenti\GitHub\auto_pyinstaller\app\src\icons\aupy.ico"

class Colors(Enum):
    DARK_BLUE = "#181b2c"
    MISTIC_BLUE = "#22274b"
    SILVER = "silver"
    GLOW_AZURE = "#2336d2"
    YELLOW = "yellow"
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    WHITE = "white"
    BLACK = "black"


class Fonts(Enum):
    SEGOE_UI = "SegoeUI"
    HELVETICA = "Helvetica"
    ROBOTO = "Roboto"


def poperror(title, error: str) -> None:
    popup(
        title,
        "Something has gone wrong.\n Please try again :(",
        error,
        size="920x300"
    )


def popup(title: str, msg_title: str, msg: str, size: Optional[str] = "400x300") -> None:
    """Create a popup window"""
    pop = tk.Tk()
    pop.title(title)
    pop.geometry(size)
    pop.iconbitmap(Images.LOGO.value)
    pop.resizable(True, False)
    pop.config(bg=Colors.DARK_BLUE.value)

    pop_label1 = tk.Label(
        pop,
        text=msg_title,
        bg=Colors.DARK_BLUE.value,
        fg=Colors.WHITE.value,
        font=Fonts.ROBOTO.value + " 16",
    )
    pop_label1.grid(row=1, column=1, padx=30, pady=35)

    pop_label2 = tk.Label(
        pop,
        text=msg,
        bg=Colors.DARK_BLUE.value,
        fg=Colors.YELLOW.value,
        font=Fonts.ROBOTO.value + " 12",
    )
    pop_label2.grid(row=2, column=1, padx=30, pady=5)

    pop_btn = tk.Button(
        pop,
        text="EXIT",
        bg=Colors.GLOW_AZURE.value,
        fg=Colors.WHITE.value,
        font=Fonts.ROBOTO.value,
        command=pop.destroy,
        activebackground=Colors.WHITE.value,
        activeforeground=Colors.GLOW_AZURE.value,
        border=False
    )
    pop_btn.grid(row=3, column=1, pady=30)

    pop.mainloop()


if __name__ == "__main__":
    poperror()
