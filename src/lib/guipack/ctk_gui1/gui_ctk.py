from lib.guipack.ctk_gui1.modules.input_types import InputTypes
from lib.guipack.ctk_gui1.modules.left_frame import left_frame
from lib.guipack.ctk_gui1.modules.right_frame import right_frame
from lib.configpack.config import Gui, App
from dataclasses import dataclass
from typing import Optional
import sys

import customtkinter as ct

sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")


CLOCK: int = 1000


@dataclass
class CtkGui:
    """Represents a GUI. This class can be used to add GUI components."""

    _input_types_registry = {
        InputTypes.MAIN: {"entry": None, "data": None},
        InputTypes.DATA: {"entry": None, "data": None},
        InputTypes.IMPORTS: {"entry": None, "data": None},
        InputTypes.ICON: {"entry": None, "data": None},
    }

    def __init__(
        self,
        win_size: str,
        title: str,
        gui_info: Optional[Gui] = None,
        app_info: Optional[App] = None,
        appearance_mode: Optional[str] = None,
        color_theme: Optional[str] = None,
    ):
        # initializing gui info
        self.gui = ct.CTk()
        self.gui.title(title)  # CTk Title
        self._app_title = title
        self.gui.geometry(win_size)
        self.gui.iconbitmap(gui_info.images.logo)
        self.gui.resizable(
            gui_info.window.resizable_width, gui_info.window.resizable_height
        )
        self.gui.protocol(
            "WM_DELETE_WINDOW", self.close
        )  # call self.close() when app gets closed
        # setting app theme and appearance
        if gui_info is not None:
            self.gui_info = gui_info
        if not appearance_mode:
            appearance_mode = gui_info.window.appearance_mode
        if not color_theme:
            color_theme = gui_info.window.color_theme
        self.change_appearance_mode(appearance_mode)
        self.change_color_theme(color_theme)
        self.app = app_info
        self.clock = max(
            CLOCK, gui_info.params.clock
        )  # min 1000 ticks / 1s

    def change_appearance_mode(self, apprearance_mode: str) -> None:
        # Modes: "System" (standard), "Dark", "Light"
        if not apprearance_mode:
            apprearance_mode = "Dark"
        ct.set_appearance_mode(apprearance_mode)

    def change_color_theme(self, color_theme: str) -> None:
        # Themes: "blue" (standard), "green", "dark-blue"
        if not color_theme:
            color_theme = "blue"
        ct.set_default_color_theme(color_theme)

    def build(self):
        # self._load_gui_images()
        # ============ create two frames ============
        # gui_infoigure grid layout (2x1)
        self.gui.grid_columnconfigure(1, weight=1)
        self.gui.grid_rowconfigure(0, weight=1)

        left_frame._build_left_frame(self)
        right_frame._build_right_frame_spec(self)

        return self

    def loop(self):
        """Starts the application loop."""
        if self:
            self.gui.mainloop()

    def close(self, event=0):
        """Destroy the window when closed."""
        self.gui.destroy()

    def spec_button_event(self):
        print("Spec button pressed")

    def exe_button_event(self):
        print("Exe button pressed")

    def config_button_event(self):
        print("Config button pressed")

    def button_event(self):
        print("Button pressed")
