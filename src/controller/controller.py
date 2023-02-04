from model.model import Model
from view.abc_view import View


class App:
    """"""

    def __init__(self, model: Model, view: View) -> None:
        self.model: Model = model
        self.view: View = view

    def start(self) -> None:
        """"""

    def stop(self) -> None:
        """"""
