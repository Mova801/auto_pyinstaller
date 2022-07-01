from dataclasses import dataclass


@dataclass
class Colors:
    blue_cloudy_ocean: str


@dataclass()
class Sizes:
    window: str
    bar: str
    button: str
    img_button: str
    image: str
    frame: str


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
    default_window_read_timeout: int
    inputs_num: int


@dataclass
class Fonts:
    app: str


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


@dataclass
class AutoPyConfig:
    app: App
    paths: Paths
    links: Links
    gui: Gui
