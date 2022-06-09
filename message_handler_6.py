import os
from termcolor import colored, cprint
from dataclasses import dataclass


module_name: str = "message_handler_6"  # library name
vlib: str = "6.0.02.06.2022"  # library version
author: str = "Mova801"


# info sulla libreria
def __lib_info__() -> dict:
    return {
        "module_name": module_name,
        "version": vlib,
        "author": author
    }


APP_LOADING = f"""
 ╔══════════════════════════════════════════════════════════╗
 ║   INITIALIZING {module_name}{vlib} LIBRARY...   ║
 ╚══════════════════════════════════════════════════════════╝
 """


@dataclass
class Decoration:

    # inizializza la classe
    #   crea un dizionario in cui verranno salvati i messaggi da utilizzare nell'applicazione
    def __init__(self, **kwargs) -> None:
        self.show_info = kwargs.get("show_info", False)
        self.dict_messages = {}
        print(APP_LOADING)

    # inizializza un certo messaggio
    #   importa il messaggio
    #   aggiunge il messaggio al dizionario
    #   cancella il messaggio importato (rimane nel dict)
    def init(self, *messages) -> None:
        for msg in messages:
            try:
                exec(f"from messages import {msg} as MSG")
                exec("self.dict_messages[msg] = MSG")
                exec("del MSG")
                if self.show_info:
                    cprint(f"{msg} imported correcly", "cyan")
                return True
            except ImportError as error:
                cprint(error, "red")
                return False

    # stampa messaggi preimpostati o personalizzati
    # flags:
    #   mymsg - stampa msg personalizzato
    #   color - stampa il messaggio con un certo colore
    #   input - richiede input all'utente e lo restituisce
    #   clear - pulisce il terminale (dopo INPUT)
    #   add   - aggiunge testo personalizzato al msg

    def pretty(self, msg: str, **flags: any) -> str:
        if flags.get("mymsg", False) is False:
            get_msg = self.dict_messages.get(msg, None)
            if get_msg is not None:
                msg: str = get_msg
            else:
                if self.init(msg):
                    msg = self.dict_messages.get(msg)
                else:
                    msg = "<-MESSAGE NOT FOUND - TRY ANOTHER MESSAGE CODE OR CHECK THE GIVEN VALUE->"
                    flags["color"] = "red"
                

        # se non è presente il campo "colore" negli argomenti lo crea e lo imposta a "None"
        color: any = flags.get("color", None)

        user_input: any
        printmsg: bool
        if flags.get("input"):
            user_input = input(colored(msg, color))
            printmsg = False
        else:
            user_input = None
            printmsg = True

        if flags.get("clear", False):
            os.system('cls')

        if printmsg:
            add_text = flags.get("add", "")
            cprint(msg + colored(add_text, "cyan"), color)

        return user_input
