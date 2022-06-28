import PySimpleGUI as sg
CPU_MAX = RAM_MAX = 100
BAR_WIDTH = 5
BAR_HEIGHT = 10

def build_layout() -> list[list]:
    resources = [
        [
            sg.ProgressBar(CPU_MAX, orientation='h', size=(
                BAR_WIDTH, BAR_HEIGHT), key='-CBAR-', bar_color=("#00ce22", None)),
            sg.Text("CPU: ", key='-CTEXT-')
        ],
        [
            sg.ProgressBar(RAM_MAX, orientation='h', size=(
                BAR_WIDTH, BAR_HEIGHT), key='-RBAR-', bar_color=("#3A91FB", None)),
            sg.Text("Memory: ", key='-RTEXT-')
        ]
    ]

    resource_usage = [
        [sg.Frame("Resource Usage", layout=resources)]
    ]

    button = [
        [sg.Button("OK", s=(8, 2), k='-OK-')]
    ]

    layout = [
        [resource_usage],
        [button]
    ]

    return layout


def main():
    layout = build_layout()

    window = sg.Window("Resource % Usage [WIP]", layout, size=(800, 600))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()
    window = None


if __name__ == "__main__":
    main()
