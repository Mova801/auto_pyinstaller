import customtkinter as ct

from view.abc_view import View


class Gui(ct.CTk, View):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        """"""
        self.mainloop()

    def close(self) -> None:
        """"""
        self.destroy()

    def build(self, controller) -> None:
        """"""
