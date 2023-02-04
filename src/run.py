from model.model import Model
from view.view import View
from

def main() -> None:
    view = View()
    app = App(Model(), view=view)
    # handler the application loop
    app.loop()


if __name__ == "__main__":
    main()
