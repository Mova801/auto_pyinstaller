from lib.guipack.ctk_gui1.modules.input_types import InputTypes
from lib.guipack.gui import GUI
import tkinter as tk
import sys
from tkinter import filedialog
from typing import Optional


sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")


def open_file_dialog(
    title: Optional[str] = "Select A File",
    filetypes: list[str] = (),
    initialdir: Optional[str] = "/",
) -> str:
    return filedialog.askopenfilename(
        initialdir=initialdir, title=title, filetypes=filetypes
    )


def open_files_dialog(
    title: Optional[str] = "Select Files",
    filetypes: list[str] = (),
    initialdir: Optional[str] = "/",
) -> str:
    return filedialog.askopenfilenames(
        initialdir=initialdir, title=title, filetypes=filetypes
    )


def _set_entry_text(entry: GUI, text: str) -> None:
    entry.delete(0, tk.END)
    entry.insert(0, text)


def _save_input(gui: GUI, input_type: InputTypes, value: str) -> None:
    if not value:
        path = gui._input_types_registry[input_type]["entry"].get()
        gui._input_types_registry[input_type]["data"] = path
    else:
        gui._input_types_registry[input_type]["data"] = value
        entry = gui._input_types_registry[input_type]["entry"]
        _set_entry_text(entry, value)


def _open_dialog(
    gui: GUI,
    types: list[list[str, str]],
    input_type: InputTypes,
    multifiles: bool = False,
) -> str:
    if multifiles:
        path = open_files_dialog("Select files", types)
    else:
        path = open_file_dialog("Select a file", types)
    _save_input(gui, input_type, path)
