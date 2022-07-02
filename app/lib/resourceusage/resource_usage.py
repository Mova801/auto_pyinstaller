import psutil

# BAR_CHAR = "■"  #'█'


def display_usage(
    cpu_usage: int | float, mem_usage: int | float, bars: int = 50, bar_char: str = "█"
) -> None:
    cpu_percentage = cpu_usage / 100.0
    cpu_bar = bar_char * int(cpu_percentage * bars) + "-" * (
        bars - int(cpu_percentage * bars)
    )
    mem_percentage = mem_usage / 100.0
    mem_bar = bar_char * int(mem_percentage * bars) + "-" * (
        bars - int(mem_percentage * bars)
    )
    print(f"\rCPU Usage: |{cpu_bar}|{int(cpu_usage)}%  ", end="")
    print(f"Mem Usage: |{mem_bar}|{int(mem_usage)}%  ", end="\r")


def get_cpu_usage():
    return int(psutil.cpu_percent())


def get_mem_usage():
    return int(psutil.virtual_memory().percent)


def get_usage():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return cpu, mem


def main():
    while True:
        cpu, mem = get_usage()
        display_usage(cpu, mem)  # , bar_char=BAR_CHAR)


if __name__ == "__main__":
    main()
