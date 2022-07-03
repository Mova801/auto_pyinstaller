import tkinter as tk
from tkinter import messagebox
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
    """Create a popup error window"""
    messagebox.showerror(title=title, message=error)


def popup(
    title: str, msg_title: str, msg: str, size: Optional[str] = "400x300"
) -> None:
    """Create a popup window"""
    messagebox.showerror(title=title, message=msg_title)


if __name__ == "__main__":
    poperror()
