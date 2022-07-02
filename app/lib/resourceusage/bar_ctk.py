from resource_usage import get_cpu_usage, get_mem_usage
import customtkinter as ct
from threading import Thread


UPDATE_TICKS = 1000
LEN = 100

global label_cpu, label_mem, cpu_bar, mem_bar, cpu
cpu = mem = 50


def _cpu_usage() -> None:
    global label_cpu, cpu_bar, cpu
    cpu = get_cpu_usage()
    label_cpu.config(text=f"CPU: {cpu:2d}%")
    cpu_bar.set(cpu / LEN)
    # print(cpu / LEN)
    cpu_bar.after(UPDATE_TICKS, _cpu_usage)


def _mem_usage() -> None:
    global label_mem, mem_bar, mem
    mem = get_mem_usage()
    label_mem.config(text=f"MEM: {mem:2d}%")
    mem_bar.set(mem / LEN)
    # print(cpu / LEN)
    mem_bar.after(UPDATE_TICKS, _mem_usage)


def read_int():
    global mem
    while True:
        mem = int(input("cpu: "))


def main():
    global label_cpu, label_mem, cpu_bar, mem_bar
    root = ct.CTk()
    root.title("Resource Usage")
    root.resizable(width=400, height=400)

    cpu_bar = ct.CTkProgressBar(master=root, width=LEN)
    cpu_bar.set(cpu // LEN)
    cpu_bar.grid(row=8, column=0, padx=10)

    label_cpu = ct.CTkLabel(
        master=root,
        text=f"CPU: 00%",
        text_font=("Roboto Medium", 8),
    )  # font name and size in px
    label_cpu.grid(row=8, column=1, padx=10)

    _cpu_usage()

    # ============ frame_left: mem usage ============

    mem_bar = ct.CTkProgressBar(master=root, width=LEN)
    mem_bar.set(0.5)
    mem_bar.grid(row=9, column=0, padx=10)

    label_mem = ct.CTkLabel(
        master=root,
        text=f"MEM: 50%",
        text_font=("Roboto Medium", 8),
    )  # font name and size in px
    label_mem.grid(row=9, column=1, padx=10)

    _mem_usage()

    root.mainloop()


if __name__ == "__main__":
    # t = Thread(target=read_int, args=())
    # t.start()
    main()
