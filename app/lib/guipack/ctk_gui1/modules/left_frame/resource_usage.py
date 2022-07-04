import sys

sys.path.append(r"C:\Users\marco\Documents\GitHub\auto_pyinstaller\app")
from lib.guipack.gui import GUI
from lib.guipack.ctk_gui1.modules.support_functions import (
    get_cpu_usage,
    get_mem_usage,
)


def _cpu_usage(gui: GUI):
    cpu = get_cpu_usage()
    gui.label_cpu.config(text=f"CPU: {cpu:2d}%")
    gui.cpu_bar.set(cpu / 100)
    gui.cpu_bar.after(gui.update_time_ticks, _cpu_usage, gui)


def _mem_usage(gui: GUI):
    mem = get_mem_usage()
    gui.label_mem.config(text=f"MEM: {mem:2d}%")
    gui.mem_bar.set(mem / 100)
    gui.mem_bar.after(gui.update_time_ticks, _mem_usage, gui)
