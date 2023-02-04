from tkinter import messagebox
from typing import Optional
from enum import Enum
from pathlib import Path


class Images(Enum):
    LOGO = Path.cwd().joinpath('rsc/icons/aupy.ico')


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
