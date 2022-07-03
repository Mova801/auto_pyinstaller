import PIL.Image, PIL.ImageTk
import tkinter
import psutil
from tkinter import filedialog
from typing import Optional


def get_cpu_usage():
    return int(psutil.cpu_percent())


def get_mem_usage():
    return int(psutil.virtual_memory().percent)


def open_image(image_name: str, size: int) -> PIL.ImageTk.PhotoImage:
    """Opens and resizes an image file and returns it as PhotoImage."""
    image = PIL.Image.open(image_name).resize((size, size), PIL.Image.ANTIALIAS)
    return PIL.ImageTk.PhotoImage(image)


def open_file_dialog(
    title: Optional[str] = "Select A File",
    filetypes: list[str] = (),
    initialdir: Optional[str] = "/",
) -> str:
    return filedialog.askopenfilename(
        initialdir=initialdir, title=title, filetypes=filetypes
    )


def open_files_dialog(
    title: Optional[str] = "Select A Directory",
    filetypes: list[str] = (),
    initialdir: Optional[str] = "/",
) -> str:
    return filedialog.askopenfilenames(
        initialdir=initialdir, title=title, filetypes=filetypes
    )
