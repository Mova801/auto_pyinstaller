from termcolor import colored

version = "b3.0.09.06.2022"

APP_INFO = f""" ╔{"═" * len(version)}═════════════════════════════╗
 ║ AutoPyinstaller - version: {version} ║
 ╚{"═" * len(version)}═════════════════════════════╝"""


APP_DEV = f""" ╔════════════════════════════════╗
 ║       Developer Contacts       ║
 ╠════════════════════════════════╣
 ║ mail: marco.vita2222@gmail.com ║
 ║ github: Mova801                ║
 ╚════════════════════════════════╝"""


APP_START = """ ╔═══════════════════════════╗
 ║ PRESS 'Enter[←]' TO START ║
 ╚═══════════════════════════╝"""


### APP START MENU ###

# ║ [{colored("*", "magenta")}] → Edit Settings    ║
APP_MENU = f""" ╔════════════════════════╗
 ║ [{colored("-", "red")}]      Menu          ║
 ╠════════════════════════╣
 ║ [{colored("bp", "blue")}] → New Spec File   ║
 ║ [{colored("ex", "magenta")}] → New Exe File    ║
 ║ [{colored("o", "yellow")}] → Visit Dev GitHub ║
 ╚════════════════════════╝

 {colored('►', 'cyan')} """


### QR GENERATION MESSAGES ###

### --- ###

INFO = f""" ╔═══════════════════════════════════════════════════════════════════════════════╗
 ║                                      {colored("Info","cyan")}                                     ║
 ╠═══════════════════════════════════════════════════════════════════════════════╣
 ║ {colored("■: I FILE SPECIFICATI DEVONO ESSERE NELLA STESSA CARTELLA DI QUESTO PROGRAMMA", "red")} ║
 ║ {colored('*', 'red')}: {colored("campo obbligatorio (in caso contrario si può lasciare il campo vuoto)", "cyan")}      ║
 ║ {colored('*', 'green')}: {colored("possibilità di specificare più file", "cyan")}                                        ║
 ╚═══════════════════════════════════════════════════════════════════════════════╝"""

EXE_ENTER_BP = f" {colored('╠', 'cyan')} Seleziona {colored('blueprint', 'blue')} (spec file): "

EXE_ENTER_GEN = f" {colored('╚', 'cyan')} Genera {colored('EXE', 'magenta')} file[{colored('Y', 'green')}|{colored('n', 'red')}]: "

EXE_GEN_END = f" {colored('■', 'cyan')} Exe file generation ended with code: "

SPEC_START = """
 ╔══════════════════════════╗
 ║   SPEC FILE GENERATION   ║
 ╠══════════════════════════╝"""

EXE_START = """
 ╔══════════════════════════╗
 ║   SPEC FILE GENERATION   ║
 ╠══════════════════════════╝"""

SPEC_ENTER_MAIN = f" {colored('╠', 'cyan')} Nome {colored('main','yellow')}{colored('(script di avvio)','red')} script da usare{colored('*', 'red')}: "

SPEC_MULTI_INPUT = f" [{colored('*', 'green')}] Modalità inserimento multiplo -> {colored('filename,filename,...', 'green')}"

SPEC_ENTER_DATA = f" {colored('╠', 'cyan')} Inserisci {colored('file aggiuntivi', 'yellow')} (come txt o json){colored('*', 'green')}: "

SPEC_ENTER_HI = f" {colored('╠', 'cyan')} Inserici i nomi dei {colored('moduli di supporto', 'yellow')}{colored('*', 'green')}: "

SPEC_ENTER_NAME = f" {colored('╠', 'cyan')} Inserisci il {colored('nome', 'yellow')} del file EXE che verrà generato {colored('(se omesso = nome main script)', 'red')}: "

SPEC_ENTER_ICON = f" {colored('╚', 'cyan')} Inserici il nome dell'{colored('icona', 'yellow')} da usare {colored('(.ico)', 'red')}: "

SPEC_GEN_END = f" {colored('■', 'cyan')} Spec file generation ended with code: "
### OPERATION OUTCOME ###

### POSITIVE ###

MSG_VALID_INPUT = """ ╔═════════════╗
 ║ valid input ║
 ╚═════════════╝"""

MSG_UPDATE = """ ╔═════════════════════╗
 ║ updated output file ║
 ╚═════════════════════╝"""

### OTHER ERRORS ###

ERR_FILE = """ ╔════════════════╗
 ║ file not found ║
 ╚════════════════╝"""

ERR_INV_INPUT = """ ╔═══════════════╗
 ║ invalid input ║
 ╚═══════════════╝"""

ERR_INV_CHARS = """ ╔══════════════════════════════════╗
 ║ invalid chars → \ /: * ? " < > | ║
 ╚══════════════════════════════════╝"""

ERR_INTERNAL = """ ╔════════════════╗
 ║ INTERNAL ERROR ║
 ╚════════════════╝"""

ERR_INV_PATH = """ ╔════════════╗
 ║ PATH ERROR ║
 ╚════════════╝"""

ERR_PERMISSION = """
 ╔═══════════════════╗
 ║ permission denied ║
 ╚═══════════════════╝
 """
