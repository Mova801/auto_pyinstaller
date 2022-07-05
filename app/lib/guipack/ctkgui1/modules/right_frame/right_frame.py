
import customtkinter as ct
import sys

sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")

INFO_BTN_W_PLUS = 10


class RightFrame:
    """Represents a frame."""

    def __init__(self) -> None:
        self.frame = ct.CTkFrame()

    def build(self):
        # ============ frame_right ============

        self.frame_right = ct.CTkFrame(master=self.self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # self_infoigure grid layout (2x1)
        self.frame_right.grid_rowconfigure(
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
            weight=1,
        )
        self.frame_right.grid_columnconfigure(0, weight=1)
        # self.frame_right.grid_columnconfigure(2, weight=1)

        self.label_title_spec = ct.CTkLabel(
            master=self.frame_right,
            text="Spec File Generation",
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font + 8),
        )
        self.label_title_spec.grid(row=1, column=0, pady=20, padx=20, sticky="w")

        self.frame_info = ct.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=2, column=0, padx=20, sticky="nsew")

        # ============ frame_info ============

        # self_infoigure grid layout (1x1)
        self.frame_info.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.frame_info.grid_columnconfigure((0, 1), weight=0)

        self._build_right_frame_main_row(self)
        self._build_right_frame_data_row(self)
        self._build_right_frame_imports_row(self)
        self._build_right_frame_icon_row(self)

        img_resize = int(self.self_info.sizes.img_button * 0.8)

        main = self._input_types_registry[InputTypes.MAIN]["data"]
        data = self._input_types_registry[InputTypes.DATA]["data"]
        imports = self._input_types_registry[InputTypes.IMPORTS]["data"]
        icon = self._input_types_registry[InputTypes.ICON]["data"]

        SAVE = open_image(self.self_info.images.save, img_resize)
        btn_size = self.self_info.sizes.img_button
        self.button_save = ct.CTkButton(
            master=self.frame_info,
            image=SAVE,
            command=lambda: save_spec_file(main, data, imports, icon),
            compound=self.self_info.params.img_pos,
            text="Save",
            text_font=(self.self_info.sizes.font, self.self_info.sizes.title_small),
            height=btn_size + 10,
        )
        self.button_save.grid(row=5, column=1, pady=20, sticky="ew")


    def _build_right_frame_main_row(self):
        entry_pad: int = self.self_info.right_frame.entry_pad
        entry_width: int = self.self_info.right_frame.entry_width
        btn_i_padx: int = self.self_info.right_frame.btn_i_padx
        btn_i_pady: int = self.self_info.right_frame.btn_i_pady

        # ============ frame_right: main entry ============
        main_row: int = 0
        btn_info: int = int(self.self_info.sizes.info_button)
        self.main_entry = ct.CTkEntry(
            master=self.frame_info,
            width=entry_width,
            placeholder_text="Select main file...",
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font),
        )
        self.main_entry.grid(
            row=main_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
        )
        self._input_types_registry[InputTypes.MAIN]["entry"] = self.main_entry
        # ============ frame_right: main browse button ============
        self.button_browse_main = ct.CTkButton(
            master=self.frame_info,
            text="Browse",
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font),
            command=lambda: file_dialog._open_dialog(
                self, (("python files", "*.py"),), InputTypes.MAIN
            ),
        )
        self.button_browse_main.grid(row=main_row, column=1, sticky="e")

        # ============ frame_right: main info button ============

        HELP_IMG = open_image(self.self_info.images.help,
                            self.self_info.sizes.info_button)

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            width=btn_info + INFO_BTN_W_PLUS,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=main_row, column=2, pady=btn_i_pady, padx=btn_i_padx, sticky="wn"
        )  # , sticky="n")


    def _build_right_frame_data_row(self):
        entry_pad: int = self.self_info.right_frame.entry_pad
        entry_width: int = self.self_info.right_frame.entry_width
        btn_i_padx: int = self.self_info.right_frame.btn_i_padx
        btn_i_pady: int = self.self_info.right_frame.btn_i_pady

        # ============ frame_right: data entry ============
        data_row: int = 1
        btn_info: int = int(self.self_info.sizes.info_button)
        self.data_entry = ct.CTkEntry(
            master=self.frame_info,
            width=entry_width,
            placeholder_text="Select data files...",
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font),
        )
        self.data_entry.grid(
            row=data_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
        )
        self._input_types_registry[InputTypes.DATA]["entry"] = self.data_entry
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
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font),
            command=lambda: file_dialog._open_dialog(self, types, InputTypes.DATA),
        )
        self.button_browse_main.grid(row=data_row, column=1, sticky="e")

        # ============ frame_right: data info button ============

        HELP_IMG = open_image(self.self_info.images.help,
                            self.self_info.sizes.info_button)

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            width=btn_info + INFO_BTN_W_PLUS,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=data_row, column=2, pady=btn_i_pady, padx=btn_i_padx, sticky="wn"
        )  # , sticky="n")


    def _build_right_frame_imports_row(self: self):
        entry_pad: int = self.self_info.right_frame.entry_pad
        entry_width: int = self.self_info.right_frame.entry_width
        btn_i_padx: int = self.self_info.right_frame.btn_i_padx
        btn_i_pady: int = self.self_info.right_frame.btn_i_pady

        # ============ frame_right: hidden imports entry ============
        imports_row: int = 2
        btn_info: int = int(self.self_info.sizes.info_button)
        self.imports_entry = ct.CTkEntry(
            master=self.frame_info,
            width=entry_width,
            placeholder_text="Select imports files...",
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font),
        )
        self.imports_entry.grid(
            row=imports_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
        )
        # ============ frame_right: imports browse button ============
        self.button_browse_main = ct.CTkButton(
            master=self.frame_info,
            text="Browse",
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font),
            command=lambda: file_dialog._open_dialog(
                self, (("python files", "*.py"),), InputTypes.IMPORTS, multifiles=True
            ),
        )
        self.button_browse_main.grid(row=imports_row, column=1, sticky="e")

        self._input_types_registry[InputTypes.IMPORTS]["entry"] = self.imports_entry
        # ============ frame_right: imports info button ============

        HELP_IMG = open_image(self.self_info.images.help,
                            self.self_info.sizes.info_button)

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            width=btn_info + INFO_BTN_W_PLUS,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=imports_row, column=2, pady=btn_i_pady, padx=btn_i_padx, sticky="wn"
        )  # , sticky="n")


    def _build_right_frame_icon_row(self: self):
        entry_pad: int = self.self_info.right_frame.entry_pad
        entry_width: int = self.self_info.right_frame.entry_width
        btn_i_padx: int = self.self_info.right_frame.btn_i_padx
        btn_i_pady: int = self.self_info.right_frame.btn_i_pady

        # ============ frame_right: icon entry ============
        icon_row: int = 3
        btn_info: int = int(self.self_info.sizes.info_button)
        self.icon_entry = ct.CTkEntry(
            master=self.frame_info,
            width=entry_width,
            placeholder_text="Select icon...",
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font),
        )
        self.icon_entry.grid(
            row=icon_row, column=0, pady=entry_pad, padx=entry_pad, sticky="w"
        )
        # ============ frame_right: imports browse button ============
        self.button_browse_main = ct.CTkButton(
            master=self.frame_info,
            text="Browse",
            text_font=(self.self_info.fonts.roboto, self.self_info.sizes.font),
            command=lambda: file_dialog._open_dialog(
                self, (("ico files", "*.ico"),), InputTypes.ICON
            ),
        )
        self.button_browse_main.grid(row=icon_row, column=1, sticky="e")

        self._input_types_registry[InputTypes.ICON]["entry"] = self.icon_entry
        # ============ frame_right: imports info button ============

        HELP_IMG = open_image(self.self_info.images.help,
                            self.self_info.sizes.info_button)

        self.button_help_main = ct.CTkButton(
            master=self.frame_info,
            image=HELP_IMG,
            command=self.button_event,
            text="",
            width=btn_info + INFO_BTN_W_PLUS,
            height=btn_info,
        )
        self.button_help_main.grid(
            row=icon_row, column=2, pady=btn_i_pady, padx=btn_i_padx, sticky="wn"
        )  # , sticky="n")

        # IMAGE = open_image(self.self_info.images.image, self.self_info.sizes.img_button)

        # self.button_help_main = ct.CTkButton(
        #     master=self.frame_info,
        #     image=IMAGE,
        #     command=lambda: show_image(self.icon_path),
        #     text="",
        #     bg_color=None,
        #     width=int(self.self_info.sizes.buttonw - 30),
        # )
        # self.button_help_main.grid(row=icon_row, column=3, padx=entry_pad)  # , sticky="n")



