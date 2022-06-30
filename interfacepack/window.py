import PySimpleGUI as sg


class Layout:
    def __init__(self) -> None:
        self._layout: list[list] = []

    def add_sub_layout(self, sub_layout: sg.PySimpleGUI) -> None:
        self._layout.append(sub_layout)

    def remove_sub_layout(self) -> None:
        self._layout.remove()

    @property
    def layout(self) -> list[list]:
        return self._layout


def build_window(
    title: str, size: tuple[str, str], layout: list[list], icon: bytes = None
) -> sg.Window:
    return sg.Window(title=title, size=size, layout=layout, icon=icon, finalize=True)
