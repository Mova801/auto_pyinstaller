from dataclasses import dataclass

DictOfStrings = dict[str]
DictOfTuples = dict[tuple[str, str]]


def adapt_str_to_tuple(dic: DictOfStrings) -> DictOfTuples:
    return {key: val.split(",") for key, val in dic.items()}


@dataclass
class Colors:
    blue_cloudy_ocean: str


@dataclass()
class Sizes:
    window: tuple[str, str]
    bar: tuple[str, str]
    button: tuple[str, str]
    img_button: tuple[str, str]
    image: tuple[str, str]
    frame: tuple[str, str]


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
class App:
    version: str
    name: str


@dataclass
class Paths:
    specs: str


@dataclass
class Links:
    github: str


@dataclass
class Interface:
    colors: Colors
    sizes: Sizes
    images: Images
    params: Params


@dataclass
class AutoPyConfig:
    app: App
    paths: Paths
    links: Links
    interface: Interface
