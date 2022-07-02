from dataclasses import dataclass
from typing import Protocol
import customtkinter

# Types Aliases
CTkElement = customtkinter.CTkBaseClass


@dataclass
class GUI(Protocol):

    def change_appearance_mode(apprearance_mode: str) -> None:
        raise NotImplementedError()

    def change_appearance_mode(color_theme: str) -> None:
        raise NotImplementedError()

    def build(self, *args, **kwargs):
        raise NotImplementedError()

    def loop(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()