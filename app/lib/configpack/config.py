from dataclasses import dataclass


@dataclass
class Colors:
    blue_cloudy_ocean: str


@dataclass()
class Sizes:
    window: str
    bar: int
    button: str
    img_button: int
    image: int
    frame: str
    font: int


@dataclass
class Images:
    github: str
    help: str
    bug: str
    shutdown: str
    logo: str


@dataclass
class Params:
    percentage_range: int
    update_time_ticks: int
    inputs_num: int


@dataclass
class Fonts:
    roboto: str


class Window:
    resizable_width: bool
    resizable_height: bool
    appearance_mode: str
    color_theme: str


@dataclass
class App:
    title: str
    version: str
    build: str
    name: str


@dataclass
class Paths:
    specs: str


@dataclass
class Links:
    github: str


@dataclass
class Gui:
    colors: Colors
    sizes: Sizes
    images: Images
    params: Params
    fonts: Fonts
    window: Window


@dataclass
class AutoPyConfig:
    app: App
    paths: Paths
    links: Links
    gui: Gui


def str_to_tuple(string: str) -> tuple[int, int]:
    return tuple(map(int, string.split('x')))


def format_size(sizes: Sizes) -> Sizes:
    format_size: list = []
    for size in sizes.values():
        format_size.append(size)
    return Sizes(*format_size)
