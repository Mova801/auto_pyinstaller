import time 
import psutil


def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percentage = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percentage * bars) + '-' * (bars - int(cpu_percentage * bars))
    mem_percentage = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percentage * bars) + '-' * (bars - int(mem_percentage * bars))
    print(f"\rCPU Usage: |{cpu_bar}|{cpu_usage:.2f}%  ", end="")
    print(f"Mem Usage: |{mem_bar}|{mem_usage:.2f}%  ", end="\r")

def get_usage():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return cpu, mem

