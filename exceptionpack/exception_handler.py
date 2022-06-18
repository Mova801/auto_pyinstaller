from dataclasses import dataclass


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        cls = args[0]
        try:
            message = None
            func(*args, **kwargs)
        except FileNotFoundError as error:
            message = error
        except SyntaxError as error:
            message = error
        except ImportError as error:
            message = error

        if cls._debug and message is not None:
            print(error)
        return cls
    return wrapper


@dataclass
class ExceptionHandler(Exception):
    _debug: bool

    def __init__(self, debug=False, *args: object) -> None:
        self._debug = debug
        super().__init__(*args)


