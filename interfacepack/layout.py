import PySimpleGUI as sg

from ..configpack.config import Interface
from ..interfacepack import sub_layouts as sl
from ..interfacepack.window import Layout



def build_layout(title: str, conf: Interface) -> list[list]:
    layout = Layout()

    imgs_path = conf.images
    img_btn_size = conf.sizes.img_button
    blue_cloudy_ocean = conf.colors.blue_cloudy_ocean

    

    #      SPEC SECTION SHOULD LOOK LIKE THIS
    #     
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