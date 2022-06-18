import os
from termcolor import colored, cprint
from dataclasses import dataclass
from getpass import getpass


# lib info
__email__: str = "imova2882@gmail.com"
__version__: str = "0.1.0"
__author__: str = "Mova801"



@dataclass
class MessageHandler:
    _debug: bool
    _messages_location: str
    _dict_messages: dict

    # inizializza la classe
    #   crea un dizionario in cui verranno salvati i messaggi da utilizzare nell'applicazione
    def __init__(self, **kwargs) -> None:
        self._debug = kwargs.get("debug", False)
        self._messages_location = kwargs.get("_import", "messages")
        self._dict_messages = {}

    # inizializza un certo messaggio
    #   importa il messaggio
    #   aggiunge il messaggio al dizionario
    #   cancella il messaggio importato (rimane nel dict)
    def init(self, *messages) -> None:
        for message in messages:
            exec(f"from {self._messages_location} import {message} as MSG")
            exec("self._dict_messages[message] = MSG")
            exec("del MSG")
            if not self._dict_messages.get(message):
                raise ImportError

            if self._debug:
                cprint(f"{message} imported correcly", "cyan")
            return True

    def get_preset_msgs(self):
        return [msg_item for msg_item in self._dict_messages]

    # stampa messaggi preimpostati o personalizzati
    # flags:
    #   mymsg    - stampa msg personalizzato
    #   color    - stampa il messaggio con un certo colore
    #   input    - richiede input all'utente e lo restituisce
    #   password - stessa funzione di input, ma non mostra cosa viene digitato
    #   clear    - pulisce il terminale (dopo INPUT/PASSWORD)
    #   add      - aggiunge testo personalizzato al msg

    def private_print(self, msg: str, **flags: any) -> str:
        if flags.get("mymsg", False) is False:
            get_msg = self._dict_messages.get(msg, None)
            if get_msg is not None:
                msg: str = get_msg
            else:
                self.init(msg)
                msg = self._dict_messages.get(msg)
                # else:
                #     msg = "<-MESSAGE NOT FOUND - TRY ANOTHER MESSAGE CODE OR CHECK THE GIVEN VALUE->"
                #     flags["color"] = "red"

        # se non è presente il campo "colore" negli argomenti lo crea e lo imposta a "None"
        color: any = flags.get("color", None)

        user_input: any
        printmsg: bool
        if flags.get("input"):
            user_input = input(colored(msg, color))
            printmsg = False
        elif flags.get("password"):
            # getpass(prompt=colored(msg, color))
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

    def print(self, msg: str, **kwargs: dict) -> str:
        return self.private_print(msg, **kwargs)

    def iprint(self, msg: str, **kwargs: dict) -> str:
        return self.private_print(msg, input=True, **kwargs)

    def colprint(self, msg: str, **kwargs: dict) -> str:
        return self.private_print(msg, mymsg=True, **kwargs)

    def clsprint(self, msg: str, **kwargs: dict) -> str:
        return self.private_print(msg, clear=True, **kwargs)

    def myprint(self, msg: str, **kwargs: dict) -> str:
        return self.private_print(msg, mymsg=True, **kwargs)
