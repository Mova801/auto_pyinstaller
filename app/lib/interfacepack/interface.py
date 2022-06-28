from configparser import ConfigParser
from pathlib import Path
from re import I
import PySimpleGUI as sg
CPU_MAX = RAM_MAX = 100
BAR_WIDTH = 5
BAR_HEIGHT = 10


def extract_interface_variables(config: ConfigParser):
    name = config['APP'].get("name", "Application Name")
    version = config['APP'].get("version", "")
    title: str = f"{name} v{version}"
    window_size: tuple[str, str] = config['SIZES'].get(
        'window', "(800,600)").split(',')
    btn_size: tuple[str, str] = config['SIZES'].get(
        "btn", "(10,10)").split(",")
    btn_img_size: tuple[str, str] = config['SIZES'].get(
        "btn_img", "(10,10)").split(",")
    btn_clk_clr: str = config['COLORS'].get("btn_click", "#37517e").split(",")
    images_path: Path = config['PATH'].get("icons", "")
    logo: tuple[str, str] = config['APP'].get(
        "logo", "")
    max_percentage: int = int(
        config['INTERFACE_VARS'].get("max_percentage", "100"))
    return title, window_size, btn_size, btn_img_size, btn_clk_clr, images_path, logo, max_percentage


def buildImageButton(image, size, color, key):
    return sg.Button(image_source=image,
                     image_size=size, key=key,
                     border_width=1, mouseover_colors=color)


def build_resource_usage_interface():
    return [
        [
            sg.ProgressBar(CPU_MAX, orientation='h', size=(
                BAR_WIDTH, BAR_HEIGHT), key='-CBAR-', bar_color=("#00ce22", None)),
            sg.Text("CPU: ", key='-CTEXT-')
        ],
        [
            sg.ProgressBar(RAM_MAX, orientation='h', size=(
                BAR_WIDTH, BAR_HEIGHT), key='-RBAR-', bar_color=("#3A91FB", None)),
            sg.Text("Memory: ", key='-RTEXT-')
        ]
    ]


def build_title_row_interface(images_path: Path, title: str):
    return [
        [
            sg.Image(images_path + "logo.png", size=(
                40, 40), key="-LOGO-"),
            sg.Text(title, font="bold 14", key="-APP_NAME-")
        ]
    ]


def build_input_1_interface(images_path, btn_size, btn_clr):
    HELP_ICON = images_path+"help.png"
    return [
        [sg.Input(), sg.FileBrowse(),
         buildImageButton(HELP_ICON, btn_size, btn_clr, '-HELP1-')]
    ]


def build_input_2_interface(images_path, btn_size, btn_clr):
    HELP_ICON = images_path+"help.png"
    return [
        [sg.Input(), sg.FileBrowse(), buildImageButton(HELP_ICON, btn_size, btn_clr, '-HELP2-'),
            sg.Listbox(values=[], size=(20, 2))]
    ]


def build_input_3_interface(images_path, btn_size, btn_clr):
    HELP_ICON = images_path+"help.png"
    return [
        [sg.Input(), sg.FileBrowse(), buildImageButton(HELP_ICON, btn_size, btn_clr, '-HELP3-'),
         sg.Listbox(values=[], size=(20, 2))]
    ]


def build_input_4_interface(images_path, btn_size, btn_clr):
    HELP_ICON = images_path+"help.png"
    return [
        [sg.Input(), sg.FileBrowse(), buildImageButton(HELP_ICON, btn_size, btn_clr, '-HELP4-'),
         sg.Frame(title="", layout=[[sg.Image(k='-ICON-')]], size=(150, 100))]
    ]


def build_buttons_row_interface(btn_size, btn_clk_clr):
    return [
        [
            sg.Button("New Spec", image_size=btn_size, key="-SPEC-",
                      border_width=1, mouseover_colors=btn_clk_clr, disabled=True),
            sg.Button("New Exe", image_size=btn_size, key="-EXE-",
                      border_width=1, mouseover_colors=btn_clk_clr, disabled=True)
        ],
    ]
    return [
        [sg.Button("New Spec", size=btn_img_size, mouseover_colors=btn_clk_clr, k='-SPEC-'),
         sg.Button("New Exe", size=btn_img_size, mouseover_colors=btn_clk_clr, k='-EXE-')]
    ]

# def build_third_row_interface():
#     ...

# def build_fourth_row_interface():
#     ...


def build_buttons_col_interface(btn_img_size, btn_clk_clr, images_path):
    # ICONS PATHS
    BUG_ICON = f"{images_path}bug.png"
    GITHUB_ICON = f"{images_path}github.png"
    QUIT_ICON = f"{images_path}shutdown.png"
    return [
        [sg.Push()],
        [buildImageButton(BUG_ICON, btn_img_size, btn_clk_clr, '-BUG-')],
        [sg.Push()],
        [buildImageButton(GITHUB_ICON, btn_img_size, btn_clk_clr, '-GITHUB-')],
        [sg.Push()],
        [buildImageButton(QUIT_ICON, btn_img_size, btn_clk_clr, '-QUIT-')],
    ]


def build_layout(interface_vars: list) -> list[list]:
    title, _, btn_size, btn_img_size, btn_clk_clr, images_path, _, max_percentage = interface_vars

    title_row = build_title_row_interface(images_path, title)

    #      SPEC SECTION SHOULD LOOK LIKE THIS
    #      _______ _______
    #     | SPEC  \__EXE__|____________________________________
    #     |                _________                           |
    #     | main_input    |_C:\m..._| [BROWSE] (?)  _________  |
    #     | data_input    |_________| [BROWSE] (?) |_0_files_| |
    #     | imports_input |_________| [BROWSE] (?) |_5_files_| |
    #     | icon_input    |_________| [BROWSE] (?)             |
    #     |  ________________________________________________  |
    #     | |               ####        ^                ^   | |
    #     | |_______       ######      ^              \/     | |
    #     | |#######\______ #### __________________  ^   /\  | |
    #     | |##############\____/##################\____     | |
    #     | |###########################################\____| |
    #     | ┴────────────────────────────────────────────────┴ |
    #     |────────────────────────────────────────────────────|
    #     | [SAVE] (○) open spec file                          |
    #     |____________________________________________________|
    #     |  ________            |                             |
    #     | |█_______| CPU: 10%  |                             |
    #     | |███_____| MEM: 30%  |                             |
    #     |──────────────────────┴─────────────────────────────|
    #     |  build 0.5.0.27.06.2022                            |
    #     |____________________________________________________|
                                                              
    #      EXE SECTION SHOULD LOOK LIKE THIS
    #      _______ _______              
    #     |__SPEC_/  EXE  \____________________________________
    #     |                _________                           |
    #     | spec_input    |_C:\spec_| [BROWSE] (?)             | 
    #     |                                                    |
    #     |  ________________________________________________  |
    #     | | 00:25:24 [main] laoding hidden imports...      | |
    #     | | 00:25:24 [main] hooking files...               | |
    #     | | 00:25:24 [main] building exe file...           | |
    #     | | 00:25:24 [main] build finished!                | |
    #     | | 00:25:24 [main] exe file generated successfully| |
    #     | | ■                                              | |
    #     | | ╚[exit code: 0]                                | |
    #     | |                                                | |
    #     | |                                                | |
    #     | |________________________________________________| |
    #     |                                                    |
    #     |────────────────────────────────────────────────────|
    #     | [GENERATE] (x) start exe file                      |
    #     |____________________________________________________|
    #     |  ________            |                             |
    #     | |██______| CPU: 20%  |                             |
    #     | |████____| MEM: 50%  |                             |
    #     |──────────────────────┴─────────────────────────────|
    #     |  build 0.5.0.27.06.2022                            |
    #     |____________________________________________________|

    


    input_row_1 = build_input_1_interface(
        images_path, btn_img_size, btn_clk_clr)
    input_row_2 = build_input_2_interface(
        images_path, btn_img_size, btn_clk_clr)
    input_row_3 = build_input_3_interface(
        images_path, btn_img_size, btn_clk_clr)
    input_row_4 = build_input_4_interface(
        images_path, btn_img_size, btn_clk_clr)
    tabs = ...

    input_col_1 = ...
    buttons_col_2 = ...
    resource_usage_col_3 = ...
    foot_row = ...
    [sg.Submit(), sg.Cancel()]

    FRAME_SIZE = (800, 100)
    input_rows = [
        [sg.Frame("main", input_row_1, k='-IN1-', size=FRAME_SIZE,)],
        [sg.Frame("data", input_row_2, k='-IN2-', size=FRAME_SIZE)],
        [sg.Frame("imports", input_row_3, k='-IN3-', size=FRAME_SIZE)],
        [sg.Frame("icon", input_row_4, k='-IN4-', size=FRAME_SIZE)]
    ]

    layout = [
        [title_row],
        [input_rows]

    ]

    # first_row = build_title_row_interface(images_path, title)
    # second_row = build_buttons_row_interface(btn_size, btn_clk_clr)
    # # third_row = build_third_row_interface()
    # # fourth_row = build_fourth_row_interface()

    # btns_row = build_buttons_col_interface(
    #     btn_img_size, btn_clk_clr, images_path)

    # resources = build_resource_usage_interface()
    # third_row = [
    #     [sg.Column(layout=btns_row, k='-BTNS-'),
    #      sg.Push(),
    #      sg.Column(layout=resources, k='-RESOURCE-')]
    # ]
    # layout = [
    #     [first_row],
    #     [sg.Frame(title=" Main Buttons ", layout=second_row,
    #               k='-MAIN_BTNS-', size=(600, 180))],
    #     [sg.Frame(title=" Info ", layout=third_row, k='-INFO-', size=(600, 200))]

    # ]
    return layout


def build_window(title: str, window_size: tuple[int, int], layout: list[list], icon: bytes = None) -> sg.Window:
    return sg.Window(title=title, size=window_size, layout=layout, icon=icon, finalize=True)


def main():

    layout = build_layout()
    window = build_window("interface", (800, 600), layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()
    window = None


if __name__ == "__main__":
    main()
