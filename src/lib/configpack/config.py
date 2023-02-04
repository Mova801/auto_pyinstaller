from dataclasses import dataclass


@dataclass
class Colors:
    blue_cloudy_ocean: str


@dataclass()
class Sizes:
    window: str
    bar: int
    buttonw: str
    buttonh: str
    img_button: int
    info_button: int
    image: int
    frame: str
    font: int
    title_small: int
    title: int


@dataclass
class Images:
    github: str
    help: str
    bug: str
    shutdown: str
    settings: str
    spec: str
    exe: str
    image: str
    save: str
    in_app_logo: str
    logo: str


@dataclass
class Params:
    img_pos: str
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
class LeftFrame:
    button_pady: int
    show_resource_usage: bool


@dataclass
class RightFrame:
    entry_pad: int
    entry_width: int
    btn_i_padx: int
    btn_i_pady: int

@dataclass
class App:
    build: str
    name: str
    version: str


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
    right_frame: RightFrame
    left_frame: LeftFrame


@dataclass
class AutoPyConfig:
    app: App
    paths: Paths
    links: Links
    gui: Gui


def str_to_tuple(string: str) -> tuple[int, int]:
    return tuple(map(int, string.split("x")))


def format_size(sizes: Sizes) -> Sizes:
    format_size: list = []
    for size in sizes.values():
        format_size.append(size)
    return Sizes(*format_size)
