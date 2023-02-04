from typing import Any, Callable

import customtkinter as ct

from lib.guipack.gui import GUI

CTkElement = ct.CTkBaseClass

module_build_funcs: dict[str, Callable[..., GUI]] = {}


def register(module: str, builder_func: Callable[..., GUI]) -> None:
    """Load a GUI section from a module."""
    module_build_funcs[module] = builder_func

def unregister(module: str) -> None:
    """Remove a GUI section."""
    module_build_funcs.pop(module, None)

def build(args: dict[str, Any]) -> CTkElement:
    """Buiild a loaded module and returns it."""
    element = 

