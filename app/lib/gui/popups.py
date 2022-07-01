import tkinter as tk
import customtkinter as ck
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
        title, "Something has gone wrong.\n Please try again :(", error, size="420x300"
    )


def popup(
    title: str, msg_title: str, msg: str, size: Optional[str] = "400x300"
) -> None:
    """Create a popup window"""
    win_width, _ = size.split("x")
    ck.set_appearance_mode("dark")
    ck.set_default_color_theme("blue")
    pop = ck.CTk()
    pop.title(title)
    pop.geometry(size)
    pop.iconbitmap(Images.LOGO.value)
    pop.resizable(True, False)

    # ============ frame ================
    frame = ck.CTkFrame(master=pop, width=int(win_width))
    frame.grid(row=0, column=0, sticky="ns")

    # ============ title ================

    title_label = ck.CTkLabel(
        master=frame,
        text=msg_title,
        text_font=(Fonts.ROBOTO.value, 20),
        width=int(win_width),
    )
    title_label.grid(row=0, column=0, sticky="ns", pady=30)

    # ============= msg =================

    msg_label = ck.CTkLabel(
        master=frame,
        text=msg,
        background=None,
        width=int(win_width)
    )
    msg_label.grid(row=1, column=0, sticky=tk.NSEW)

    # =========== button ================

    button = ck.CTkButton(
        master=frame,
        text="EXIT",
        text_font=(Fonts.ROBOTO.value, 20),
        text_color=Colors.WHITE.value,
        command=pop.destroy,
    )
    button.grid(row=2, column=0, pady=30)

    pop.mainloop()


if __name__ == "__main__":
    poperror(
        "POPUP ERROR",
        "ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR",
    )
