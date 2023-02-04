import PIL.Image, PIL.ImageTk
import psutil


def get_cpu_usage():
    return int(psutil.cpu_percent())


def get_mem_usage():
    return int(psutil.virtual_memory().percent)


def open_image(image_name: str, size: int) -> PIL.ImageTk.PhotoImage:
    """Opens and resizes an image file and returns it as PhotoImage."""
    image = PIL.Image.open(image_name).resize((size, size), PIL.Image.ANTIALIAS)
    return PIL.ImageTk.PhotoImage(image)

def show_image(image_path: str) -> None:
    """Shows an image file on screen."""
    if image_path:
        PIL.Image.open(image_path).show()


def save_spec_file(main: str, data: str, imports: str, icon: str) -> None:
    print(main, data, imports, icon)
    if not main or not data or not imports:
        return None
    print("SAVE")
