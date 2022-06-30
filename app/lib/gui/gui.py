from dataclasses import dataclass
import tkinter
import tkinter.messagebox
from typing import Protocol
import customtkinter

# Types Aliases
CTkElement = customtkinter.CTkBaseClass


@dataclass
class GUI(Protocol):
    
    def add_sub_layout(self, sub_layout: CTkElement):
        ...
    
    def remove_sub_layout(self, sub_layout: CTkElement):
        ...

    