from lib.configpack.config import Gui
import tkinter
from typing import Optional
import PIL.Image
import PIL.ImageTk

import customtkinter
import webbrowser as wb

import sys

sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")


def open_link(link: str) -> None:
    """Opens the given link if valid."""
    if link:
        wb.open(link)


def open_image(image_name: str):
    """Opens an image file and returns it as bytes."""
    return PIL.ImageTk.PhotoImage(
        PIL.Image.open(image_name))


class AutoPyApp(customtkinter.CTk):
    """Class that represents the AutoPyGUI."""

    _app_win_size: str
    _app_title: str

    def __init__(
        self,
        win_size: str,
        title: str,
        version: Optional[str] = None,
        build: Optional[str] = None,
        gui_conf: Optional[Gui] = None,
        apprearance_mode: Optional[str] = None,
        color_theme: Optional[str] = None,
    ):
        if not apprearance_mode:
            apprearance_mode = "Dark"
        if not color_theme:
            color_theme = "blue"
        customtkinter.set_appearance_mode(
            apprearance_mode
        )  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme(
            color_theme
        )  # Themes: "blue" (standard), "green", "dark-blue"
        super().__init__()
        self._app_win_size = win_size
        self._app_title = title
        self._gui_conf = gui_conf
        self._version = version
        self._build = build
        self.title = title  # CTk Title
        self.geometry(win_size)
        self.protocol(
            "WM_DELETE_WINDOW", self.on_closing
        )  # call .on_closing() when app gets closed

    def create_gui(
        self,
    ):
        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=180, corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(
            master=self.frame_left,
            text=self._app_title,
            text_font=(self._gui_conf.fonts.app, -16),
        )  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(
            master=self.frame_left, text="Spec", command=self.spec_button_event
        )
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(
            master=self.frame_left, text="Exe", command=self.exe_button_event
        )
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(
            master=self.frame_left, text="Settings", command=self.config_button_event
        )
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        # ============ frame_left: build info ============

        self.label_build = customtkinter.CTkLabel(
            master=self.frame_left, text=f"build {self._build} v{self._version}"
        )
        self.label_build.grid(row=10, column=0, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(
            row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew"
        )

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure((0, 1, 2, 3), weight=0)
        self.frame_info.columnconfigure((0, 1), weight=0)

        # self.label_info_1 = customtkinter.CTkLabel(
        #     master=self.frame_info,
        #     text="CTkLabel: Lorem ipsum dolor sit,\n"
        #     + "amet consetetur sadipscing elitr,\n"
        #     + "sed diam nonumy eirmod tempor",
        #     height=100,
        #     fg_color=("white", "gray38"),  # <- custom tuple-color
        #     justify=tkinter.LEFT,
        # )
        # self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        # self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        # self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        # ============ frame_right: main entry ============
        main_row: int = 0
        btn_img_size: int = int(self._gui_conf.sizes.img_button)

        self.entry = customtkinter.CTkEntry(
            master=self.frame_info, width=220, placeholder_text="Select main file"
        )
        self.entry.grid(row=main_row, column=0, pady=5, padx=5, sticky="w")

        self.button_browse_main = customtkinter.CTkButton(
            master=self.frame_info, text="BROWSE", command=self.button_event
        )
        self.button_browse_main.grid(row=main_row, column=1, sticky="e")

        HELP_IMG = open_image(self._gui_conf.images.help)

        self.button_help_main = customtkinter.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            corner_radius=50,
            width=btn_img_size,
            height=btn_img_size
        )
        self.button_help_main.grid(row=main_row, column=2, padx=5, sticky="")

        # ============ frame_right: data entry ============
        data_row: int = 1

        self.entry = customtkinter.CTkEntry(
            master=self.frame_info, width=220, placeholder_text="Select main file"
        )
        self.entry.grid(row=data_row, column=0, pady=5, padx=5, sticky="w")

        self.button_browse_main = customtkinter.CTkButton(
            master=self.frame_info, text="BROWSE", command=self.button_event
        )
        self.button_browse_main.grid(row=data_row, column=1, sticky="e")

        HELP_IMG = open_image(self._gui_conf.images.help)

        self.button_help_main = customtkinter.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            corner_radius=50,
            width=10,
            height=10,
        )
        self.button_help_main.grid(row=data_row, column=2, padx=5, sticky="")

        # ============ frame_right: hidden imports entry ============
        imports_row: int = 2

        self.entry = customtkinter.CTkEntry(
            master=self.frame_info, width=220, placeholder_text="Select main file"
        )
        self.entry.grid(row=imports_row, column=0, pady=5, padx=5, sticky="w")

        self.button_browse_main = customtkinter.CTkButton(
            master=self.frame_info, text="BROWSE", command=self.button_event
        )
        self.button_browse_main.grid(row=imports_row, column=1, sticky="e")

        HELP_IMG = open_image(self._gui_conf.images.help)

        self.button_help_main = customtkinter.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            corner_radius=50,
            width=10,
            height=10,
        )
        self.button_help_main.grid(
            row=imports_row, column=2, padx=5, sticky="")

        # self.radio_var = tkinter.IntVar(value=0)

        # self.label_radio_group = customtkinter.CTkLabel(
        #     master=self.frame_right, text="CTkRadioButton Group:"
        # )
        # self.label_radio_group.grid(
        #     row=0, column=2, columnspan=1, pady=20, padx=10, sticky=""
        # )

        # self.radio_button_1 = customtkinter.CTkRadioButton(
        #     master=self.frame_right, variable=self.radio_var, value=0
        # )
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_2 = customtkinter.CTkRadioButton(
        #     master=self.frame_right, variable=self.radio_var, value=1
        # )
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_3 = customtkinter.CTkRadioButton(
        #     master=self.frame_right, variable=self.radio_var, value=2
        # )
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # self.slider_1 = customtkinter.CTkSlider(
        #     master=self.frame_right,
        #     from_=0,
        #     to=1,
        #     number_of_steps=3,
        #     command=self.progressbar.set,
        # )
        # self.slider_1.grid(row=4, column=0, columnspan=2,
        #                    pady=10, padx=20, sticky="we")

        # self.slider_2 = customtkinter.CTkSlider(
        #     master=self.frame_right, command=self.progressbar.set
        # )
        # self.slider_2.grid(row=5, column=0, columnspan=2,
        #                    pady=10, padx=20, sticky="we")

        # self.switch_1 = customtkinter.CTkSwitch(
        #     master=self.frame_right, text="CTkSwitch"
        # )
        # self.switch_1.grid(row=4, column=2, columnspan=1,
        #                    pady=10, padx=20, sticky="we")

        # self.switch_2 = customtkinter.CTkSwitch(
        #     master=self.frame_right, text="CTkSwitch"
        # )
        # self.switch_2.grid(row=5, column=2, columnspan=1,
        #                    pady=10, padx=20, sticky="we")

        # self.combobox_1 = customtkinter.CTkComboBox(
        #     master=self.frame_right, values=["Value 1", "Value 2"]
        # )
        # self.combobox_1.grid(
        #     row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we"
        # )

        # self.check_box_1 = customtkinter.CTkCheckBox(
        #     master=self.frame_right, text="CTkCheckBox"
        # )
        # self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        # self.check_box_2 = customtkinter.CTkCheckBox(
        #     master=self.frame_right, text="CTkCheckBox"
        # )
        # self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # self.entry = customtkinter.CTkEntry(
        #     master=self.frame_right, width=120, placeholder_text="CTkEntry"
        # )
        # self.entry.grid(row=8, column=0, columnspan=2,
        #                 pady=20, padx=20, sticky="we")

        # self.button_5 = customtkinter.CTkButton(
        #     master=self.frame_right,
        #     text="CTkButton",
        #     border_width=2,  # <- custom border_width
        #     fg_color=None,  # <- no fg_color
        #     command=self.button_event,
        # )
        # self.button_5.grid(row=8, column=2, columnspan=1,
        #                    pady=20, padx=20, sticky="we")

        # # set default values
        # self.combobox_1.set("CTkCombobox")
        # self.radio_button_1.select()
        # # self.slider_1.set(0.2)
        # # self.slider_2.set(0.7)
        # # self.progressbar.set(0.5)
        # self.switch_2.select()
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        # self.check_box_1.configure(
        #     state=tkinter.DISABLED, text="CheckBox disabled")
        # self.check_box_2.select()

    def spec_button_event(self):
        ...

    def exe_button_event(self):
        ...

    def config_button_event(self):
        ...

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        """Destroy the window when closed."""
        self.destroy()


if __name__ == "__main__":
    app = AutoPyApp("800x600", "GUI")
    app.mainloop()
