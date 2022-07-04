from dataclasses import dataclass
from typing import Optional
import tkinter as tk
import sys
from enum import Enum

import customtkinter as ct

sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")
from lib.configpack.config import Gui, App
from lib.guipack.ctk_gui1.support_functions import (
    get_cpu_usage,
    get_mem_usage,
    open_file_dialog,
    open_files_dialog,
    open_image,
    show_image,
)


class InputTypes(Enum):
    MAIN = "main"
    DATA = "data"
    IMPORTS = "imports"
    ICON = "icon"


@dataclass
class CtkGui:
    """Represents a GUI. This class can be used to add GUI components."""

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
        self.update_time_ticks = max(
            1000, gui_info.params.update_time_ticks
        )  # min 1000 ticks / 1s

        self.main_path = self.data_path = self.imports_path = self.icon_path = None

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

    def _set_entry_text(self, entry: ct.CTkEntry, text: str) -> None:
        entry.delete(0, tk.END)
        entry.insert(0, text)

    def _save_input(self, input_type: InputTypes, value: str) -> None:
        if input_type == InputTypes.MAIN:
            self.main_path = value
            self._set_entry_text(self.main_entry, value)

        if input_type == InputTypes.DATA:
            self.data_path = value
            self._set_entry_text(self.data_entry, value)

        if input_type == InputTypes.IMPORTS:
            self.imports_path = value
            self._set_entry_text(self.imports_entry, value)

        if input_type == InputTypes.ICON:
            self.icon_path = value
            self._set_entry_text(self.icon_entry, value)

    def _open_dialog(
        self,
        types: list[list[str, str]],
        input_type: InputTypes,
        multifiles: bool = False,
    ) -> str:
        if multifiles:
            path = open_files_dialog("Select files", types)
        else:
            path = open_file_dialog("Select a file", types)
        self._save_input(input_type, path)

    def _cpu_usage(self):
        cpu = get_cpu_usage()
        self.label_cpu.config(text=f"CPU: {cpu:2d}%")
        self.cpu_bar.set(cpu / 100)
        self.cpu_bar.after(self.update_time_ticks, self._cpu_usage)

    def _mem_usage(self):
        mem = get_mem_usage()
        self.label_mem.config(text=f"MEM: {mem:2d}%")
        self.mem_bar.set(mem / 100)
        self.mem_bar.after(self.update_time_ticks, self._mem_usage)

    def _build_left_frame_buttons(self) -> None:
        button_pady: int = self.gui_info.left_frame.button_pady
        icon_size_scale: int = 1
        img_size: int = int(self.gui_info.sizes.img_button * icon_size_scale)

        SPEC_ICON = open_image(self.gui_info.images.spec, img_size)
        self.button_1 = ct.CTkButton(
            master=self.frame_left,
            text="Spec",
            image=SPEC_ICON,
            compound="right",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=self.spec_button_event,
        )
        self.button_1.grid(row=2, column=0, pady=button_pady, padx=20)

        EXE_ICON = open_image(self.gui_info.images.exe, img_size)
        self.button_2 = ct.CTkButton(
            master=self.frame_left,
            text="Exe",
            image=EXE_ICON,
            compound="right",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=self.exe_button_event,
        )
        self.button_2.grid(row=3, column=0, pady=button_pady, padx=20)

        SETTINGS_ICON = open_image(self.gui_info.images.settings, img_size)
        self.button_3 = ct.CTkButton(
            master=self.frame_left,
            text="Settings",
            image=SETTINGS_ICON,
            compound="right",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=self.config_button_event,
        )
        self.button_3.grid(row=4, column=0, pady=button_pady, padx=20)

    def _build_resource_usage_interface(self) -> None:
        # ============ frame_left: cpu usage ============

        self.label_cpu = ct.CTkLabel(
            master=self.frame_left,
            text=f"CPU: {0:2d}%",
            text_font=(self.gui_info.fonts.roboto, 8),
        )  # font name and size in px
        self.label_cpu.grid(row=6, column=0, sticky="we")

        self.cpu_bar = ct.CTkProgressBar(
            master=self.frame_left, width=self.gui_info.sizes.bar
        )
        self.cpu_bar.set(0.0)
        self.cpu_bar.grid(row=7, column=0, sticky="we", padx=15)

        self._cpu_usage()

        # ============ frame_left: mem usage ============

        self.label_mem = ct.CTkLabel(
            master=self.frame_left,
            text=f"MEM: {0:2d}%",
            text_font=(self.gui_info.fonts.roboto, 8),
        )  # font name and size in px
        self.label_mem.grid(row=8, column=0, sticky="we")

        self.mem_bar = ct.CTkProgressBar(
            master=self.frame_left, width=self.gui_info.sizes.bar
        )
        self.mem_bar.set(0.0)
        self.mem_bar.grid(row=9, column=0, sticky="we", padx=15)

        self._mem_usage()

        # ============ frame_left: build info ============

        self.label_build = ct.CTkLabel(
            master=self.frame_left,
            text=f"build {self.app.build} v{self.app.version}",
            text_font=(self.gui_info.fonts.roboto, 7),
        )
        self.label_build.grid(row=10, column=0, sticky="we", padx=20, pady=0)

    def _build_right_frame_main_row(self):
        entry_pad: int = self.gui_info.right_frame.entry_pad
        entry_width: int = self.gui_info.right_frame.entry_width

        # ============ frame_right: main entry ============
        main_row: int = 0
        btn_info: int = int(self.gui_info.sizes.info_button)
        self.main_entry = ct.CTkEntry(
            master=self.frame_info,
            width=entry_width,
            placeholder_text="Select main file...",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
        )
        self.main_entry.grid(
            row=main_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
        )
        # ============ frame_right: main browse button ============
        self.button_browse_main = ct.CTkButton(
            master=self.frame_info,
            text="Browse",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=lambda: self._open_dialog(
                (("python files", "*.py"),), InputTypes.MAIN
            ),
            width=self.gui_info.sizes.buttonw,
        )
        self.button_browse_main.grid(row=main_row, column=1, sticky="e")

        # ============ frame_right: main info button ============

        HELP_IMG = open_image(
            self.gui_info.images.help, self.gui_info.sizes.info_button
        )

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            corner_radius=50,
            bg_color=None,
            width=btn_info + 25,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=main_row,
            column=2,
            pady=entry_pad,
            padx=entry_pad,
        )  # , sticky="n")

    def _build_right_frame_data_row(self):
        entry_pad: int = self.gui_info.right_frame.entry_pad
        entry_width: int = self.gui_info.right_frame.entry_width

        # ============ frame_right: data entry ============
        data_row: int = 1
        btn_info: int = int(self.gui_info.sizes.info_button)
        self.data_entry = ct.CTkEntry(
            master=self.frame_info,
            width=entry_width,
            placeholder_text="Select data files...",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
        )
        self.data_entry.grid(
            row=data_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
        )
        # ============ frame_right: data browse button ============
        types = (
            ("json files", "*.json"),
            ("text files", "*.txt"),
            ("ini files", "*.ini"),
            ("yaml files", "*.yaml"),
        )
        self.button_browse_main = ct.CTkButton(
            master=self.frame_info,
            text="Browse",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=lambda: self._open_dialog(types, InputTypes.DATA),
            width=self.gui_info.sizes.buttonw,
        )
        self.button_browse_main.grid(row=data_row, column=1, sticky="e")

        # ============ frame_right: data info button ============

        HELP_IMG = open_image(
            self.gui_info.images.help, self.gui_info.sizes.info_button
        )

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            corner_radius=50,
            bg_color=None,
            width=btn_info + 25,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=data_row,
            column=2,
            pady=entry_pad,
            padx=entry_pad,
        )  # , sticky="n")

    def _build_right_frame_imports_row(self):
        entry_pad: int = self.gui_info.right_frame.entry_pad
        entry_width: int = self.gui_info.right_frame.entry_width

        # ============ frame_right: hidden imports entry ============
        imports_row: int = 2
        btn_info: int = int(self.gui_info.sizes.info_button)
        self.imports_entry = ct.CTkEntry(
            master=self.frame_info,
            width=entry_width,
            placeholder_text="Select imports files...",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
        )
        self.imports_entry.grid(
            row=imports_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
        )
        # ============ frame_right: imports browse button ============
        self.button_browse_main = ct.CTkButton(
            master=self.frame_info,
            text="Browse",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=lambda: self._open_dialog(
                (("python files", "*.py"),), InputTypes.IMPORTS, multifiles=True
            ),
            width=self.gui_info.sizes.buttonw,
        )
        self.button_browse_main.grid(row=imports_row, column=1, sticky="e")

        # ============ frame_right: imports info button ============

        HELP_IMG = open_image(
            self.gui_info.images.help, self.gui_info.sizes.info_button
        )

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            corner_radius=50,
            bg_color=None,
            width=btn_info + 25,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=imports_row,
            column=2,
            pady=entry_pad,
            padx=entry_pad,
        )  # , sticky="n")

    def _build_right_frame_icon_row(self):
        entry_pad: int = self.gui_info.right_frame.entry_pad
        entry_width: int = self.gui_info.right_frame.entry_width

        # ============ frame_right: icon entry ============
        icon_row: int = 3
        btn_info: int = int(self.gui_info.sizes.info_button)
        self.icon_entry = ct.CTkEntry(
            master=self.frame_info,
            width=entry_width,
            placeholder_text="Select icon...",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
        )
        self.icon_entry.grid(
            row=icon_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
        )
        # ============ frame_right: imports browse button ============
        self.button_browse_main = ct.CTkButton(
            master=self.frame_info,
            text="Browse",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=lambda: self._open_dialog(
                (("ico files", "*.ico"),), InputTypes.ICON
            ),
            width=self.gui_info.sizes.buttonw,
        )
        self.button_browse_main.grid(row=icon_row, column=1, sticky="e")

        # ============ frame_right: imports info button ============

        HELP_IMG = open_image(
            self.gui_info.images.help, self.gui_info.sizes.info_button
        )

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            corner_radius=50,
            bg_color=None,
            width=btn_info + 25,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=icon_row,
            column=2,
            pady=entry_pad,
            padx=entry_pad,
        )  # , sticky="n")

        IMAGE = open_image(self.gui_info.images.image, self.gui_info.sizes.img_button)

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=IMAGE,
            command=lambda: show_image(self.icon_path),
            text="",
            bg_color=None,
            width=btn_info + 25,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=icon_row,
            column=3,
        )  # , sticky="n")

    def _build_left_frame(self):
        # ============ frame_left ============

        # gui_infoigure grid layout (1x2)
        self.frame_right.grid_columnconfigure(
            (0, 1),
            weight=1,
        )

        # gui_infoigure grid layout (1x11)
        self.frame_left.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            5, minsize=20, weight=1
        )  # empty row as spacing
        self.frame_left.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            9, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            10, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing

        self.label_1 = ct.CTkLabel(
            master=self.frame_left,
            text=self._app_title,
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.title_small),
        )  # font name and size in px
        self.label_1.grid(row=1, column=0)

        self._build_left_frame_buttons()

        if self.gui_info.left_frame.show_resource_usage:
            self._build_resource_usage_interface()

    def _build_right_frame_spec(self):
        # ============ frame_right ============

        # gui_infoigure grid layout (3x7)
        self.frame_right.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        self.frame_right.grid_columnconfigure(0, weight=1)
        # self.frame_right.grid_columnconfigure(2, weight=1)

        self.label_title_spec = ct.CTkLabel(
            master=self.frame_right,
            text="Spec File Generation",
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font + 8),
        )
        self.label_title_spec.grid(row=0, column=0, padx=15, sticky="w")

        self.frame_info = ct.CTkFrame(master=self.frame_right)
        self.frame_info.grid(
            row=1, column=0, columnspan=2, rowspan=4, padx=20, sticky="nsew"
        )

        # ============ frame_info ============

        # gui_infoigure grid layout (1x1)
        self.frame_info.grid_rowconfigure((1, 2, 3, 4), weight=0)
        self.frame_info.grid_columnconfigure((0, 1), weight=0)

        self._build_right_frame_main_row()
        self._build_right_frame_data_row()
        self._build_right_frame_imports_row()
        self._build_right_frame_icon_row()

        # IMAGE = open_image(self.gui_info.images.image, self.gui_info.sizes.img_button)
        # btn_size = self.gui_info.sizes.img_button
        # self.button_help_main = ct.CTkButton(
        #     master=self.frame_info,
        #     image=IMAGE,
        #     command= self.button_event,
        #     text="",
        #     bg_color=None,
        #     width=btn_size,
        #     height=btn_size,
        # )
        # self.button_help_main.grid(
        #     row=10,
        #     column=0,
        # )  # , sticky="n")


    def build(self):
        # self._load_gui_images()
        # ============ create two frames ============
        # gui_infoigure grid layout (2x1)
        self.gui.grid_columnconfigure(1, weight=1)
        self.gui.grid_rowconfigure(0, weight=1)

        self.frame_left = ct.CTkFrame(master=self.gui, width=180, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = ct.CTkFrame(master=self.gui)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self._build_left_frame()
        self._build_right_frame_spec()

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
