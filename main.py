from termcolor import colored
from colorama import init

from generator_lib import Pyinstaller
from ios.iostream import IOstream, File
from messagehandler.message_handler import MessageHandler
init()

io = IOstream()
msg = MessageHandler()

version = "0.3.1"


def format_data(data_str: str) -> list:
    data_list = data_str.split(",")
    data = [tuple((x, '.')) for x in data_list]
    if data[0][0] == "":
        data = [tuple(('', '.'))]
    return data


def spec_main():
    msg.clsprint("SPEC_MULTI_INPUT")
    msg.colprint("SPEC_START", "cyan")
    main = msg.iprint("SPEC_ENTER_MAIN", True)
    IOstream.invalid_char(main)
    data_str = msg.print("SPEC_ENTER_DATA", input=True)
    data_list = format_data(data_str)
    hidden_imports = msg.iprint("SPEC_ENTER_HI").split(",")
    if not hidden_imports:
        hidden_imports = None
    name = msg.iprint("SPEC_ENTER_NAME")
    name = IOstream.invalid_char(name)
    if not name:
        name = main
    icon = msg.iprint("SPEC_ENTER_ICON")
    icon = IOstream.invalid_char(icon)
    installer = Pyinstaller(main, name, data=data_list,
                            hidden_imports=hidden_imports, icon=icon)
    file = File(name + ".spec")
    spec_file = installer.build_spec()
    file.write(spec_file)

    msg.myprint(installer.spec, color="green", clear=True, add="\n")
    if spec_file:
        msg.print("SPEC_GEN_END", add=colored("0", "cyan"))
    else:
        msg.print("SPEC_GEN_END", add=colored("-1", "red"))
    return installer


def exe_main(installer: Pyinstaller):
    match msg.iprint(f"EXE_ENTER_GEN"):
        case 'Y':
            IOstream.clear_terminal()
            build_result = installer.build_exe()
            print()
            if build_result == 0:
                build_result = colored(build_result, 'cyan')
                msg.iprint("EXE_GEN_END", add=build_result)
            else:
                build_result = colored(build_result, 'red')
                msg.iprint("EXE_GEN_END", add=build_result)


def main() -> None:
    io.update_terminal(name="AutoPyinstaller", cols=95, lines=42)
    msg.clsprint("APP_INFO", color="cyan")
    msg.print("INFO")
    while True:
        match msg.clsprint("APP_MENU", input=True):
            case 'bp':
                spec_file = spec_main()
                if not spec_file:
                    continue
                exe_main(spec_file)

            case 'ex':
                msg.print("EXE_START", color="cyan", clear=True)
                specname = msg.print("EXE_ENTER_BP", input=True)
                spec_file = Pyinstaller('', specname)
                exe_main(spec_file)

            case 'o':
                io.open_link('https://github.com/Mova801')

            case '-':
                break


if __name__ == "__main__":
    main()
