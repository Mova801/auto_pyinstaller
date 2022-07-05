from lib.guipack.ctk_gui1.modules.right_frame import file_dialog
from lib.guipack.ctk_gui1.modules.support_functions import open_image, show_image, save_spec_file
from lib.guipack.ctk_gui1.modules.input_types import InputTypes
from lib.guipack.gui import GUI
import customtkinter as ct
import sys

sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")

INFO_BTN_W_PLUS = 10


def _build_right_frame_main_row(gui: GUI):
    entry_pad: int = gui.gui_info.right_frame.entry_pad
    entry_width: int = gui.gui_info.right_frame.entry_width
    btn_i_padx: int = gui.gui_info.right_frame.btn_i_padx
    btn_i_pady: int = gui.gui_info.right_frame.btn_i_pady

    # ============ frame_right: main entry ============
    main_row: int = 0
    btn_info: int = int(gui.gui_info.sizes.info_button)
    gui.main_entry = ct.CTkEntry(
        master=gui.frame_info,
        width=entry_width,
        placeholder_text="Select main file...",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
    )
    gui.main_entry.grid(
        row=main_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
    )
    gui._input_types_registry[InputTypes.MAIN]["entry"] = gui.main_entry
    # ============ frame_right: main browse button ============
    gui.button_browse_main = ct.CTkButton(
        master=gui.frame_info,
        text="Browse",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
        command=lambda: file_dialog._open_dialog(
            gui, (("python files", "*.py"),), InputTypes.MAIN
        ),
    )
    gui.button_browse_main.grid(row=main_row, column=1, sticky="e")

    # ============ frame_right: main info button ============

    HELP_IMG = open_image(gui.gui_info.images.help, gui.gui_info.sizes.info_button)

    gui.button_help_main = ct.CTkButton(
        master=gui.frame_info,
        image=HELP_IMG,
        command=gui.button_event,
        text="",
        width=btn_info + INFO_BTN_W_PLUS,
        height=btn_info,
    )
    gui.button_help_main.grid(
        row=main_row, column=2, pady=btn_i_pady, padx=btn_i_padx, sticky="wn"
    )  # , sticky="n")


def _build_right_frame_data_row(gui: GUI):
    entry_pad: int = gui.gui_info.right_frame.entry_pad
    entry_width: int = gui.gui_info.right_frame.entry_width
    btn_i_padx: int = gui.gui_info.right_frame.btn_i_padx
    btn_i_pady: int = gui.gui_info.right_frame.btn_i_pady

    # ============ frame_right: data entry ============
    data_row: int = 1
    btn_info: int = int(gui.gui_info.sizes.info_button)
    gui.data_entry = ct.CTkEntry(
        master=gui.frame_info,
        width=entry_width,
        placeholder_text="Select data files...",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
    )
    gui.data_entry.grid(
        row=data_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
    )
    gui._input_types_registry[InputTypes.DATA]["entry"] = gui.data_entry
    # ============ frame_right: data browse button ============
    types = (
        ("json files", "*.json"),
        ("text files", "*.txt"),
        ("ini files", "*.ini"),
        ("yaml files", "*.yaml"),
    )
    gui.button_browse_main = ct.CTkButton(
        master=gui.frame_info,
        text="Browse",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
        command=lambda: file_dialog._open_dialog(gui, types, InputTypes.DATA),
    )
    gui.button_browse_main.grid(row=data_row, column=1, sticky="e")

    # ============ frame_right: data info button ============

    HELP_IMG = open_image(gui.gui_info.images.help, gui.gui_info.sizes.info_button)

    gui.button_help_main = ct.CTkButton(
        master=gui.frame_info,
        image=HELP_IMG,
        command=gui.button_event,
        text="",
        width=btn_info + INFO_BTN_W_PLUS,
        height=btn_info,
    )
    gui.button_help_main.grid(
        row=data_row, column=2, pady=btn_i_pady, padx=btn_i_padx, sticky="wn"
    )  # , sticky="n")


def _build_right_frame_imports_row(gui: GUI):
    entry_pad: int = gui.gui_info.right_frame.entry_pad
    entry_width: int = gui.gui_info.right_frame.entry_width
    btn_i_padx: int = gui.gui_info.right_frame.btn_i_padx
    btn_i_pady: int = gui.gui_info.right_frame.btn_i_pady

    # ============ frame_right: hidden imports entry ============
    imports_row: int = 2
    btn_info: int = int(gui.gui_info.sizes.info_button)
    gui.imports_entry = ct.CTkEntry(
        master=gui.frame_info,
        width=entry_width,
        placeholder_text="Select imports files...",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
    )
    gui.imports_entry.grid(
        row=imports_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
    )
    # ============ frame_right: imports browse button ============
    gui.button_browse_main = ct.CTkButton(
        master=gui.frame_info,
        text="Browse",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
        command=lambda: file_dialog._open_dialog(
            gui, (("python files", "*.py"),), InputTypes.IMPORTS, multifiles=True
        ),
    )
    gui.button_browse_main.grid(row=imports_row, column=1, sticky="e")

    gui._input_types_registry[InputTypes.IMPORTS]["entry"] = gui.imports_entry
    # ============ frame_right: imports info button ============

    HELP_IMG = open_image(gui.gui_info.images.help, gui.gui_info.sizes.info_button)

    gui.button_help_main = ct.CTkButton(
        master=gui.frame_info,
        image=HELP_IMG,
        command=gui.button_event,
        text="",
        width=btn_info + INFO_BTN_W_PLUS,
        height=btn_info,
    )
    gui.button_help_main.grid(
        row=imports_row, column=2, pady=btn_i_pady, padx=btn_i_padx, sticky="wn"
    )  # , sticky="n")


def _build_right_frame_icon_row(gui: GUI):
    entry_pad: int = gui.gui_info.right_frame.entry_pad
    entry_width: int = gui.gui_info.right_frame.entry_width
    btn_i_padx: int = gui.gui_info.right_frame.btn_i_padx
    btn_i_pady: int = gui.gui_info.right_frame.btn_i_pady

    # ============ frame_right: icon entry ============
    icon_row: int = 3
    btn_info: int = int(gui.gui_info.sizes.info_button)
    gui.icon_entry = ct.CTkEntry(
        master=gui.frame_info,
        width=entry_width,
        placeholder_text="Select icon...",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
    )
    gui.icon_entry.grid(
        row=icon_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
    )
    # ============ frame_right: imports browse button ============
    gui.button_browse_main = ct.CTkButton(
        master=gui.frame_info,
        text="Browse",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
        command=lambda: file_dialog._open_dialog(
            gui, (("ico files", "*.ico"),), InputTypes.ICON
        ),
    )
    gui.button_browse_main.grid(row=icon_row, column=1, sticky="e")

    gui._input_types_registry[InputTypes.ICON]["entry"] = gui.icon_entry
    # ============ frame_right: imports info button ============

    HELP_IMG = open_image(gui.gui_info.images.help, gui.gui_info.sizes.info_button)

    gui.button_help_main = ct.CTkButton(
        master=gui.frame_info,
        image=HELP_IMG,
        command=gui.button_event,
        text="",
        width=btn_info + INFO_BTN_W_PLUS,
        height=btn_info,
    )
    gui.button_help_main.grid(
        row=icon_row, column=2, pady=btn_i_pady, padx=btn_i_padx, sticky="wn"
    )  # , sticky="n")

    # IMAGE = open_image(gui.gui_info.images.image, gui.gui_info.sizes.img_button)

    # gui.button_help_main = ct.CTkButton(
    #     master=gui.frame_info,
    #     image=IMAGE,
    #     command=lambda: show_image(gui.icon_path),
    #     text="",
    #     bg_color=None,
    #     width=int(gui.gui_info.sizes.buttonw - 30),
    # )
    # gui.button_help_main.grid(row=icon_row, column=3, padx=entry_pad)  # , sticky="n")


def _build_right_frame_spec(gui: GUI):
    # ============ frame_right ============

    gui.frame_right = ct.CTkFrame(master=gui.gui)
    gui.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    # gui_infoigure grid layout (2x1)
    gui.frame_right.grid_rowconfigure(
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        weight=1,
    )
    gui.frame_right.grid_columnconfigure(0, weight=1)
    # gui.frame_right.grid_columnconfigure(2, weight=1)

    gui.label_title_spec = ct.CTkLabel(
        master=gui.frame_right,
        text="Spec File Generation",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font + 8),
    )
    gui.label_title_spec.grid(row=1, column=0, pady=20, padx=20, sticky="w")

    gui.frame_info = ct.CTkFrame(master=gui.frame_right)
    gui.frame_info.grid(row=2, column=0, padx=20, sticky="nsew")

    # ============ frame_info ============

    # gui_infoigure grid layout (1x1)
    gui.frame_info.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
    gui.frame_info.grid_columnconfigure((0, 1), weight=0)

    _build_right_frame_main_row(gui)
    _build_right_frame_data_row(gui)
    _build_right_frame_imports_row(gui)
    _build_right_frame_icon_row(gui)

    img_resize = int(gui.gui_info.sizes.img_button * 0.8)

    main = gui._input_types_registry[InputTypes.MAIN]["data"]
    data = gui._input_types_registry[InputTypes.DATA]["data"]
    imports = gui._input_types_registry[InputTypes.IMPORTS]["data"]
    icon = gui._input_types_registry[InputTypes.ICON]["data"]

    SAVE = open_image(gui.gui_info.images.save, img_resize)
    btn_size = gui.gui_info.sizes.img_button
    gui.button_save = ct.CTkButton(
        master=gui.frame_info,
        image=SAVE,
        command=lambda: save_spec_file(main, data, imports, icon),
        compound=gui.gui_info.params.img_pos,
        text="Save",
        text_font=(gui.gui_info.sizes.font, gui.gui_info.sizes.title_small),
        height=btn_size + 10,
    )
    gui.button_save.grid(row=5, column=1, pady=20, sticky="ew")
