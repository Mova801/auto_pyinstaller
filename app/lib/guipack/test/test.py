import PIL.Image 

img = r"C:\Users\marco\Desktop\script\hex_icon.ico"


def show_image(image_path: str) -> None:
    """Shows an image file on screen."""
    if image_path:
        PIL.Image.open(image_path).show()

show_image(img)