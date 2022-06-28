import resource_usage
from test_interface import build_layout
import PySimpleGUI as sg
from threading import Thread
from time import sleep

cpu = 0
ram = 0


def update_bars(window: sg.Window) -> None:
    global cpu, ram
    while True:
        cpu, ram = resource_usage.get_usage()
        print(cpu, ram)
        sleep(1)
    # window['-CBAR-'].update(cpu)
    # window['-RBAR-'].update(ram)


def update_usage_bar(window):
    window['-CBAR-'].update(cpu)
    window['-RBAR-'].update(ram)


def update_usage_text(window, key, value):
    text: str = window[key].DisplayText
    text, _ = text.split(":")
    window[key].update(f'{text}: {int(value)}%')


def main():
    layout = build_layout()
    window = sg.Window("Resource % Usage [WIP]", layout, size=(800, 600))
    update_bars_thread = Thread(
        target=update_bars, args=(window,), daemon=True)
    update_bars_thread.start()
    while True:
        event, values = window.read(timeout=10)

        update_usage_bar(window)
        update_usage_text(window, '-CTEXT-', cpu)
        update_usage_text(window, '-RTEXT-', ram)


        if event == '-OK-' or sg.WIN_CLOSED:
            break

    window.close()
    window = None


if __name__ == "__main__":
    main()