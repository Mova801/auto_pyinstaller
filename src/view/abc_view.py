from abc import ABC, abstractmethod


class View(ABC):
    """"""

    @abstractmethod
    def build(self, controller) -> None:
        """"""

    @abstractmethod
    def run(self) -> None:
        """"""

    def close(self) -> None:
        """"""
