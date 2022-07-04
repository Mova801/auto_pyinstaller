import tkinter as tk
import sys

import customtkinter as ct

sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")
from lib.guipack.gui import GUI
from lib.guipack.ctk_gui1.modules.input_types import InputTypes
from lib.guipack.ctk_gui1.modules.support_functions import (
    open_file_dialog,
    open_files_dialog,
)


def _set_entry_text(entry: GUI, text: str) -> None:
    entry.delete(0, tk.END)
    entry.insert(0, text)


def _save_input(gui: GUI, input_type: InputTypes, value: str) -> None:
    if input_type == InputTypes.MAIN:
        gui.main_path = value
        _set_entry_text(gui.main_entry, value)

    if input_type == InputTypes.DATA:
        gui.data_path = value
        _set_entry_text(gui.data_entry, value)

    if input_type == InputTypes.IMPORTS:
        gui.imports_path = value
        _set_entry_text(gui.imports_entry, value)

    if input_type == InputTypes.ICON:
        gui.icon_path = value
        _set_entry_text(gui.icon_entry, value)


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
