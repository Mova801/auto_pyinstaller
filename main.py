from generator_lib import Generator
from termcolor import colored
from colorama import init
from iostream4 import IOstream, File
from message_handler_6 import MessageHandler
init()

io = IOstream()
dec = MessageHandler()

version = "b3.0.09.06.2022"

io.update_terminal(name="AutoPyinstaller", cols=95, lines=42)


def format_data(data_str: str) -> list:
    data_list = data_str.split(",")
    data = [tuple((x, '.')) for x in data_list]
    if data[0][0] == "":
        data = [tuple(('', '.'))]
    return data


def spec_main():
    dec.pretty("SPEC_MULTI_INPUT", clear=True)
    dec.pretty("SPEC_START", color="cyan")
    main = dec.pretty("SPEC_ENTER_MAIN", input=True)
    io.invalid_char(main)

    data_str = dec.pretty("SPEC_ENTER_DATA", input=True)
    data_list = format_data(data_str)

    hidden_imports = dec.pretty("SPEC_ENTER_HI", input=True).split(",")
    if hidden_imports == "":
        hidden_imports = None

    name = dec.pretty("SPEC_ENTER_NAME", input=True)
    name = io.invalid_char(name)
    if name == "":
        name = main

    icon = dec.pretty("SPEC_ENTER_ICON", input=True)
    icon = io.invalid_char(icon)

    spec = Generator(main, name, data=data_list,
                     hidden_imports=hidden_imports, icon=icon)

    file = File(name + ".spec")

    outspec = spec.spec()
    file <= outspec
    io <= file

    dec.pretty(spec.get_spec(), color="green", mymsg=True, clear=True)
    print()
    if outspec is not None:
        dec.pretty("SPEC_GEN_END", add=colored("0", "cyan"))
    else:
        dec.pretty("SPEC_GEN_END", add=colored("-1", "red"))
    return spec


def exe_main(spec):
    match dec.pretty(f"EXE_ENTER_GEN", input=True):
        case 'Y':
            io.clear_terminal()
            outexe = spec.exe()
            print()
            if outexe == 0:
                dec.pretty("EXE_GEN_SUCCESS", add=colored(
                    outexe, 'cyan'), wait=True)

            else:
                dec.pretty("EXE_GEN_SUCCESS", add=colored(
                    outexe, 'red'), wait=True)

    io.clear_terminal()
    return


def main() -> None:
    dec.pretty("APP_INFO", color="cyan", clear=True)
    dec.pretty("INFO")
    while True:
        match dec.pretty("APP_MENU", input=True):
            case 'bp':
                spec_file = spec_main()
                if spec_file is None:
                    continue
                exe_main(spec_file)

            case 'ex':
                dec.pretty("EXE_START", color="cyan", clear=True)
                specname = dec.pretty("EXE_ENTER_BP", input=True)
                spec_file = Generator('', specname)
                exe_main(spec_file)
                break

            case 'o':
                io.open_link('https://github.com/Mova801')
                io.clear_terminal()
                continue

            case '-':
                break

            case _:
                dec.pretty("ERR_INV_INPUT", color="red", clear=True)
                break


if __name__ == "__main__":
    main()
