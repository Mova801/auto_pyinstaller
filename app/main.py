from base64 import b64encode
from configparser import ConfigParser
import PySimpleGUI as sg
import sys

sys.path.append(r"C:\Users\marco\OneDrive\Documenti\GitHub")
from auto_pyinstaller.app.lib.autopypack.pyinstaller import SpecFile, PyInstaller
from auto_pyinstaller.app.lib.interfacepack import interface
from LIB.ios.iostream import open_link, is_file

title = btn_size = btn_img_size = btn_clk_clr = images_path = window_size = logo_size = max_percentage = None


CONFIG_PATH = r'C:\Users\marco\OneDrive\Documenti\GitHub\auto_pyinstaller\app\src\config\autopy.ini'


def format_data(data_str: str) -> list:
    data_list = data_str.split(",")
    data = [tuple((x, '.')) for x in data_list]
    if data[0][0] == "":
        data = [tuple(('', '.'))]
    return data


def application_loop(config: ConfigParser, window: sg.Window) -> None:
    vars = config['INTERFACE_VARS']
    dev = config['DEV']
    DEFAULT_TIMEOUT_SEC = int(vars.get('default_win_read_timeout', "10"))
    github = dev.get("github", "")
    while True:
        event, values = window.read(timeout=DEFAULT_TIMEOUT_SEC)
        if event == '-NEW_SPEC-':
            ...
        if event == '-NEW_EXE-':
            ...
        if event == '-GITHUB-':
            open_link(github)
        if event == '-QUIT-' or event == sg.WIN_CLOSED:
            break
    window.close()
    window = None


def load_config() -> list:
    config = ConfigParser()
    if is_file(CONFIG_PATH):
        config.read(CONFIG_PATH)
    else:
        raise FileNotFoundError(CONFIG_PATH)
    return config


def prepare_layout(interface_vars: list):
    return interface.build_layout(interface_vars)


def load_image(image):
    with open(image, 'rb') as img:
        image = img.read()
    return b64encode(image)


def prepare_image(interface_vars: list):
    image = interface_vars[5] + interface_vars[6]
    return load_image(image)


def prepare_window(title, window_size, layout: list[list], icon: bytes):
    return interface.build_window(title=title, window_size=window_size, layout=layout, icon=icon)


def prepare_interface(config: ConfigParser) -> sg.Window:
    # get the vars used to build the interface
    interface_vars = interface.extract_interface_variables(config)
    # build the interface layout
    layout = prepare_layout(interface_vars)
    # prepare logo image
    icon = prepare_image(interface_vars)
    # build the window system
    title = interface_vars[0]
    win_size = interface_vars[1]
    return prepare_window(title, win_size, layout, icon)


def main() -> None:
    # load the configuration file
    config = load_config()
    # prepare the app interface
    window = prepare_interface(config)
    # handler the application loop events
    application_loop(config, window)


if __name__ == "__main__":
    main()
