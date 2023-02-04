from dataclasses import dataclass
from pathlib import Path
from lib.color.color import Color


@dataclass
class AppColors:
    """Default app colors."""
    CYAN = Color('#37517e')
    AZURE = Color('#2986CC')
    DARK_BLUE = Color("#181b2c")
    MISTIC_BLUE = Color("#22274b")
    GLOW_AZURE = Color("#2336d2")
    RED = Color("#ff0000")
    BLUE = Color("#0000ff")
    GREEN = Color("#00ff00")
    WHITE = Color("#ffffff")
    BLACK = Color("#000000")


@dataclass
class AppConfig:
    version: str = '0.0.1-alpha'
    name: str = 'PythonBuilder'
    assets_path = Path.cwd().joinpath('src/icons')
    appearance_mode: str = "dark"
    color_theme: str = "blue"


@dataclass
class LinkConfig:
    github = Path.cwd().joinpath('https:/github.com/Mova801')


@dataclass
class ImagesConfig:
    github: str = 'github.png'
    info: str = 'info.png'
    bug: str = 'bug.png'
    shutdown: str = 'shutdown.png'
    settings: str = 'settings.png'
    spec: str = 'file.png'
    exe: str = 'exe.png'
    image: str = 'image.png'
    save: str = 'save.png'
    in_app_logo: str = 'logo3.png'
    logo: str = 'rock.ico'


@dataclass
class ScreenConfig:
    size: tuple[int, int] = '900x600'
    resizable: bool = False


@dataclass
class LayoutConfig:
    show_resource_usage: bool = True


class FontConfig:
    font: str = 'Roboto Medium'
    size_S: int = 10
    size_M: int = 14
    size_L: int = 18
    size_T: int = 28
