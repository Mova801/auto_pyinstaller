from base64 import b64encode

import PySimpleGUI as sg
import webbrowser as wb
import hydra
from hydra.core.config_store import ConfigStore

from lib.configpack.config import AutoPyConfig, adapt_str_to_tuple
from lib.interfacepack import window as win, layout as lt


CONFIG_PATH = "conf"
CONFIG_FILE = "autopy"


def open_link(link: str) -> None:
    """apre il link passato"""
    if link:
        wb.open(link)


def load_image(image):
    with open(image, "rb") as img:
        image = img.read()
    return b64encode(image)


def prepare_window_interface(conf: AutoPyConfig) -> sg.Window:
    # prepare window title
    title = conf.app.name + conf.app.version
    # build the interface layout
    layout = lt.build_layout(title, conf.interface)
    # prepare window logo image
    icon = load_image(conf.interface.images.logo)
    # build the window system
    return win.build_window(title=title, size=conf.interface.sizes.window, layout=layout, icon=icon)


def application_loop(conf: AutoPyConfig, window: sg.Window) -> None:
    default_window_read_timeout = conf.interface.params.default_window_read_timeout
    git_link = conf.links.github
    while True:
        event, values = window.read(timeout=default_window_read_timeout)
        if event == "-NEW_SPEC-":
            ...
        if event == "-NEW_EXE-":
            ...
        if event == "-GITHUB-":
            open_link(git_link)
        if event == "-QUIT-" or event == sg.WIN_CLOSED:
            break
    window.close()
    window = None


cf = ConfigStore.instance()
cf.store(name="autopy_config", node=AutoPyConfig)

# load the config file
@hydra.main(config_path=CONFIG_PATH, config_name=CONFIG_FILE)
def main(conf: AutoPyConfig) -> None:
    conf.interface.sizes = adapt_str_to_tuple(conf.interface.sizes)
    # prepare the app interface
    window = prepare_window_interface(conf)
    # handler the application loop events
    application_loop(conf, window)


if __name__ == "__main__":
    main()
