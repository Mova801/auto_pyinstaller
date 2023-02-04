from typing import Optional
import sys

import webbrowser as wb


sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")
from lib.guipack.gui import GUI


def open_link(link: str) -> None:
    """Opens the given link if valid."""
    if link:
        wb.open(link)


class InvalidGuiError(ValueError):
    """Exception raised when an invalid GUI is received as parameter."""


class AutoPyApp:
    """Class that represents the AutoPyGUI."""

    _app_win_size: str
    _app_title: str
    _gui: GUI

    def __init__(
        self,
        gui: GUI,
        version: Optional[str] = None,
        build: Optional[str] = None,
    ):
        self._gui = gui
        self._version = version
        self._build = build

    @property
    def gui(self, gui: GUI):
        """Set a gui for the App."""
        if not gui:
            raise InvalidGuiError(gui)
        self._gui = gui

    def loop(self):
        """Starts the application."""
        self._gui.loop()

    def on_closing(self, event=0):
        """Destroy the window when closed."""
        self._gui.close()


if __name__ == "__main__":
    app = AutoPyApp("800x600", "GUI")
    app.loop()
