from tkinter import filedialog
from typing import Optional
import customtkinter as ct


def open_file_dialog(
    title: str = "Select A File",
    filetypes: list[str] = (("python files", "*.py"), ("All files", "*.*")),
    initialdir: Optional[str] = "/",
) -> str:
    global root
    root.path = filedialog.askdirectory(
        initialdir=initialdir, title=title
    )
    print(root.path)


root = ct.CTk()
root.path = None
button_help_main = ct.CTkButton(
    master=root,
    command=open_file_dialog,
    text="Bottone",
    corner_radius=20,
    width=30,
    height=30,
)
button_help_main.pack()
root.mainloop()
label = ct.CTkLabel(text=root.path)
label.pack()
