import hydra
from hydra.core.config_store import ConfigStore
from hydra import MissingConfigException

from lib.gui.autopygui import AutoPyApp
from lib.gui.popups import poperror
from lib.configpack.config import AutoPyConfig


CONFIG_PATH = "conf"
CONFIG_FILE = "autopy"


cf = ConfigStore.instance()
cf.store(name="autopy_config", node=AutoPyConfig)

# load the config file


@hydra.main(config_path=CONFIG_PATH, config_name=CONFIG_FILE)
def main(conf: AutoPyConfig) -> None:
    # create the App obj
    app = AutoPyApp(
        conf.gui.sizes.window,
        conf.app.title,
        conf.app.version,
        conf.app.build,
        conf.gui,
    )
    app.create_gui()
    # handler the application loop
    app.mainloop()


if __name__ == "__main__":
    try:
        main()
    except MissingConfigException as e:
        poperror(
            "AutoPyApp Error Popup", e.args[0]
        )  # "An error has occurred during the configuration file loading.")
        print(e.strerror)
