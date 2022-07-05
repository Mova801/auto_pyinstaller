
from lib.guipack.ctk_gui1.modules.support_functions import open_image
from lib.guipack.ctk_gui1.modules.left_frame import resource_usage
from lib.guipack.gui import GUI
import sys
import customtkinter as ct


sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")


class LeftFrame:
    """Represents a frame."""

    def __init__(self) -> None:
        self.main = ct.CTkFrame()

    def _build_left_frame_buttons(self) -> None:
        button_pady: int = self.gui_info.left_frame.button_pady
        icon_size_scale: int = 1
        img_size: int = int(self.gui_info.sizes.img_button * icon_size_scale)

        SPEC_ICON = open_image(self.gui_info.images.spec, img_size)
        self.button_1 = ct.CTkButton(
            master=self.frame_left,
            text="  Spec",
            image=SPEC_ICON,
            compound=self.gui_info.params.img_pos,
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=self.spec_button_event,
            height=self.gui_info.sizes.buttonh
        )
        self.button_1.grid(row=2, column=0, pady=button_pady, padx=20)

        EXE_ICON = open_image(self.gui_info.images.exe, img_size)
        self.button_2 = ct.CTkButton(
            master=self.frame_left,
            text="  Exe",
            image=EXE_ICON,
            compound=self.gui_info.params.img_pos,
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=self.exe_button_event,
            height=self.gui_info.sizes.buttonh
        )
        self.button_2.grid(row=3, column=0, pady=button_pady, padx=20)

        SETTINGS_ICON = open_image(self.gui_info.images.settings, img_size)
        self.button_3 = ct.CTkButton(
            master=self.frame_left,
            text="Settings",
            image=SETTINGS_ICON,
            compound=self.gui_info.params.img_pos,
            text_font=(self.gui_info.fonts.roboto, self.gui_info.sizes.font),
            command=self.config_button_event,
            height=self.gui_info.sizes.buttonh
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
            master=self.frame_left, width=self.gui_info.sizes.bar)
        self.cpu_bar.set(0.0)
        self.cpu_bar.grid(row=7, column=0, sticky="we", padx=15)

        resource_usage._cpu_usage()

        # ============ frame_left: mem usage ============

        self.label_mem = ct.CTkLabel(
            master=self.frame_left,
            text=f"MEM: {0:2d}%",
            text_font=(self.gui_info.fonts.roboto, 8),
        )  # font name and size in px
        self.label_mem.grid(row=8, column=0, sticky="we")

        self.mem_bar = ct.CTkProgressBar(
            master=self.frame_left, width=self.gui_info.sizes.bar)
        self.mem_bar.set(0.0)
        self.mem_bar.grid(row=9, column=0, sticky="we", padx=15)

        resource_usage._mem_usage()

        # ============ frame_left: build info ============

        self.label_build = ct.CTkLabel(
            master=self.frame_left,
            text=f"build {self.app.build} v{self.app.version}",
            text_font=(self.gui_info.fonts.roboto, 7),
        )
        self.label_build.grid(row=10, column=0, sticky="we", padx=20, pady=0)

    def _build_left_frame(self):
        # ============ frame_left ============
        self.frame_left = ct.CTkFrame(
            master=self.gui, width=180, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        # gui_infoigure grid layout (1x11)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(
            5, minsize=20, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(9, minsize=20)
        self.frame_left.grid_rowconfigure(
            10, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing

        self.label_1 = ct.CTkLabel(
            master=self.frame_left,
            text=self._app_title,
            text_font=(self.gui_info.fonts.roboto,
                       self.gui_info.sizes.title_small),
        )  # font name and size in px
        self.label_1.grid(row=1, column=0)

        self._build_left_frame_buttons()

        if self.gui_info.left_frame.show_resource_usage:
            self._build_resource_usage_interface()
