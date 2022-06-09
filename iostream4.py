import os
import re
from dataclasses import dataclass
import json
import webbrowser as wb
import time
import ctypes

DESKTOP: str = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

module_name: str = "iostream4"  # library name
vlib: str = "4.0.02.06.2022"  # library version
author: str = "Mova801"


# info sulla libreria
def __lib_info__() -> dict:
    return {
        "module_name": module_name,
        "version": vlib,
        "author": author
    }


@dataclass
class File:
    filename: str
    path: str
    mode: str
    data: any
    encoding: any

    def __init__(self, filename: str, **opt: any) -> None:
        io = IOstream()
        self.path = opt.get("path", "")
        self.mode = opt.get("mode", "w")
        self.filename = io.invalid_char(filename)
        self.data = opt.get("data", "")
        self.encoding = opt.get("encoding", None)
        del io

    # aggiunge dati ai vecchi dati presenti nella variabile "data" di "File" (__le__ equivale a <=)
    def __le__(self, string: str) -> any:
        self.data += string
        return self

    # sovrascrive i vecchi dati presenti nella variabile "data" di "File" (__ilshift__ equivale a <<=)
    def __ilshift__(self, string: str) -> any:
        self.data = string
        return self

    def get_data(self) -> any:
        return self.data

    def get_filename(self) -> str:
        return self.filename

    def set_filename(self, filename: str) -> None:
        iostream = IOstream()
        self.filename = iostream.invalid_char(filename)

    def set_mode(self, mode: str) -> bool:
        match mode:
            case 'r' | 'w' | 'wb' | 'rb' | 'r+' | 'a':
                self.mode = mode
                return True
            case _:
                return False

    def set_data(self, data: any) -> None:
        if type(data) is str or dict or tuple or list or set:
            self.data = data


@dataclass
class IOstream:

    # legge un file
    def __ge__(self, file: File):
        path: str = self.join_path(file.path, file.filename)
        with open(path, file.mode, encoding=file.encoding) as f:
            file.data = f.readline()

    # legge un file json, ne legge i dati e li salva in un istanza File (>>)
    def __rshift__(self, file: File):
        path: str = self.join_path(file.path, file.filename)
        with open(path, file.mode, encoding=file.encoding) as f:
            file.data = json.load(f)

    # crea un file e ci scrive dentro i dati presenti nell'istanza File corrente (<=)
    def __le__(self, file: File) -> None:
        path: str = self.join_path(file.path, file.filename)
        with open(path, file.mode, encoding=file.encoding) as f:
            f.write(file.data)

    # crea un file json e ci scrive dentro i dati presenti nell'istanza File corrente (<<)
    def __lshift__(self, file: File) -> None:
        path: str = self.join_path(file.path, file.filename)
        with open(path, file.mode, encoding=file.encoding) as f:
            json.dump(file.data, f, indent=4)

    def get_login(self) -> str:
        return os.getlogin()

    def get_date(self, div=".") -> str:
        return time.strftime(f"%d{div}%m{div}%Y")

    def get_time(self, div=":") -> str:
        return time.strftime(f"%H{div}%M{div}%S")

    # create a new folder in the given path
    def mkdir(self, path: str) -> bool:
        try:
            os.mkdir(path)
            return True
        except FileExistsError:
            return False

    # apre il link passato
    def open_link(self, link: str) -> None:
        wb.open(link)

    # unisce due percorsi e restituisce un singolo percorso (unione dei due)
    def join_path(self, path1: str, path2: str) -> str:
        return os.path.join(path1, path2)

    # pulisce il terminale
    def clear_terminal(self) -> None:
        os.system('cls')

    # controlla se nella stringa passata sono presenti caratteri invalidi per il nome di un file
    def invalid_char(self, string: str) -> str:
        if string == "":
            return ""
        inv: list = [r'\\', r'\/', r'\:', r'\*',
                     r'\?', r'\"', r'\<', r'\>', r'\|']
        for char in inv:
            string = re.sub(char, "", string)
        return string

    # aggiorna le impostazioni della console
    def update_terminal(self, **opt: any) -> None:
        name: str = opt.get("name", "Console")
        cols: str = opt.get("cols", 50)
        lines: str = opt.get("lines", 20)

        # modifica il nome della console e lo imposta col nome dell'app nel file di configurazione
        ctypes.windll.kernel32.SetConsoleTitleW(name)
        # modifica la dimensione della console (colonne e linee)
        os.system(f"mode con cols={cols} lines={lines}")


# Log class inherit from File
#   a Log is a File which create 2 directories and a file in append mode
#       dir 1: contains the daily logs dirs
#       dir 2: daily directory (every day a new one is generated)
#   in the log file are stored data
#   
#   [!]: each time new informations are added the log write on file!

class Log(File):
    def __init__(self, filename: str, **opt) -> None:
        io = IOstream()
        self.log_dir_1 = io.invalid_char(opt.get("dir1", "LOG"))
        self.log_dir_2 = io.invalid_char(
            opt.get("dir2", f"log_{io.get_date()}"))
        io.mkdir(self.log_dir_1)
        log_path = io.join_path(self.log_dir_1, self.log_dir_2)
        io.mkdir(log_path)
        super().__init__(filename + ".log", mode='a', path=log_path)
        del io

    def log_data(self, data):
        io = IOstream()
        self.data = f"[{io.get_date()} - {io.get_time()}] {data}\n"
        io <= self
        del io
