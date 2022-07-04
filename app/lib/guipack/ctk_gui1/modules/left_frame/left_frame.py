import sys

import customtkinter as ct

sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")
from lib.guipack.gui import GUI
from lib.guipack.ctk_gui1.modules.left_frame import resource_usage
from lib.guipack.ctk_gui1.modules.support_functions import open_image


def _build_left_frame_buttons(gui: GUI) -> None:
    button_pady: int = gui.gui_info.left_frame.button_pady
    icon_size_scale: int = 1
    img_size: int = int(gui.gui_info.sizes.img_button * icon_size_scale)

    SPEC_ICON = open_image(gui.gui_info.images.spec, img_size)
    gui.button_1 = ct.CTkButton(
        master=gui.frame_left,
        text="Spec",
        image=SPEC_ICON,
        compound="right",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
        command=gui.spec_button_event,
    )
    gui.button_1.grid(row=2, column=0, pady=button_pady, padx=20)

    EXE_ICON = open_image(gui.gui_info.images.exe, img_size)
    gui.button_2 = ct.CTkButton(
        master=gui.frame_left,
        text="Exe",
        image=EXE_ICON,
        compound="right",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
        command=gui.exe_button_event,
    )
    gui.button_2.grid(row=3, column=0, pady=button_pady, padx=20)

    SETTINGS_ICON = open_image(gui.gui_info.images.settings, img_size)
    gui.button_3 = ct.CTkButton(
        master=gui.frame_left,
        text="Settings",
        image=SETTINGS_ICON,
        compound="right",
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.font),
        command=gui.config_button_event,
    )
    gui.button_3.grid(row=4, column=0, pady=button_pady, padx=20)


def _build_resource_usage_interface(gui: GUI) -> None:
    # ============ frame_left: cpu usage ============

    gui.label_cpu = ct.CTkLabel(
        master=gui.frame_left,
        text=f"CPU: {0:2d}%",
        text_font=(gui.gui_info.fonts.roboto, 8),
    )  # font name and size in px
    gui.label_cpu.grid(row=6, column=0, sticky="we")

    gui.cpu_bar = ct.CTkProgressBar(master=gui.frame_left, width=gui.gui_info.sizes.bar)
    gui.cpu_bar.set(0.0)
    gui.cpu_bar.grid(row=7, column=0, sticky="we", padx=15)

    resource_usage._cpu_usage(gui)

    # ============ frame_left: mem usage ============

    gui.label_mem = ct.CTkLabel(
        master=gui.frame_left,
        text=f"MEM: {0:2d}%",
        text_font=(gui.gui_info.fonts.roboto, 8),
    )  # font name and size in px
    gui.label_mem.grid(row=8, column=0, sticky="we")

    gui.mem_bar = ct.CTkProgressBar(master=gui.frame_left, width=gui.gui_info.sizes.bar)
    gui.mem_bar.set(0.0)
    gui.mem_bar.grid(row=9, column=0, sticky="we", padx=15)

    resource_usage._mem_usage(gui)

    # ============ frame_left: build info ============

    gui.label_build = ct.CTkLabel(
        master=gui.frame_left,
        text=f"build {gui.app.build} v{gui.app.version}",
        text_font=(gui.gui_info.fonts.roboto, 7),
    )
    gui.label_build.grid(row=10, column=0, sticky="we", padx=20, pady=0)


def _build_left_frame(gui: GUI):
    # ============ frame_left ============
    gui.frame_left = ct.CTkFrame(master=gui.gui, width=180, corner_radius=0)
    gui.frame_left.grid(row=0, column=0, sticky="nswe")

    # gui_infoigure grid layout (1x11)
    gui.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
    gui.frame_left.grid_rowconfigure(5, minsize=20, weight=1)  # empty row as spacing
    gui.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
    gui.frame_left.grid_rowconfigure(9, minsize=20)  # empty row with minsize as spacing
    gui.frame_left.grid_rowconfigure(
        10, minsize=20
    )  # empty row with minsize as spacing
    gui.frame_left.grid_rowconfigure(
        11, minsize=10
    )  # empty row with minsize as spacing

    gui.label_1 = ct.CTkLabel(
        master=gui.frame_left,
        text=gui._app_title,
        text_font=(gui.gui_info.fonts.roboto, gui.gui_info.sizes.title_small),
    )  # font name and size in px
    gui.label_1.grid(row=1, column=0)

    _build_left_frame_buttons(gui)

    if gui.gui_info.left_frame.show_resource_usage:
        _build_resource_usage_interface(gui)
