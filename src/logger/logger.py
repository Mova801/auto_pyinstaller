"""
Module that implements all a bunch of features related to logging.
Provides simple and useful logging decorator and support a decent amount of settings for customization.
"""
import functools
import logging
import time
from os import PathLike
from pathlib import Path
from typing import Any, Callable


def check_folder_structure(path: Path) -> None:
    """
    Check the given path. Create the not existent directories.
    :param path: path to check.
    :return: None
    """
    Path.mkdir(path, parents=True, exist_ok=True)


def create_stream_handler(level: int) -> logging.StreamHandler:
    """
    Return a StreamHandler.
    :param level: logging level.
    :return: formatted StreamHandler.
    """
    c_handler = logging.StreamHandler()
    c_handler.setLevel(level)
    c_handler.set_name(f"{__name__}stream_handler")
    return c_handler


def format_stream_handler(handler: logging.StreamHandler, formatting: str | None = None,
                          dateformat: str | None = ...) -> logging.StreamHandler:
    """
    Format the given StreamHandler.
    :param handler:
    :param formatting: handler formatting.
    :param dateformat: date format used in the formatting.
    :return: formatted StreamHandler.
    """
    if formatting:
        c_format = logging.Formatter(formatting, datefmt=dateformat)
        handler.setFormatter(c_format)
    return handler


def create_filestream_handler(level: int, filename: str | PathLike[str]) -> logging.FileHandler:
    """
    Return a StreamHandler.
    :param level: logging level.
    :param filename: filename used to log the file stream messages.
    :return: FileStreamHandler.
    """
    f_handler = logging.FileHandler(filename)
    f_handler.setLevel(level)
    f_handler.set_name(f"{__name__}file_handler")
    return f_handler


def format_filestream_handler(handler: logging.FileHandler, formatting: str | None = None,
                              dateformat: str | None = ...) -> logging.FileHandler:
    """
    Format the given StreamHandler.
    :param handler:
    :param formatting: handler formatting.
    :param dateformat: date format used in the formatting.
    :return: formatted FileStreamHandler.
    """
    if formatting:
        f_format = logging.Formatter(formatting, datefmt=dateformat)
        handler.setFormatter(f_format)
    return handler


def setup(logger_name: str | None = None, level: int | None = logging.WARNING, stream: bool | None = False,
          filestream: bool | None = False, formatting: str | None = "", filename: Path | None = "") -> logging.Logger:
    """
    Return a Logger object which can handle both Stream and FileStream logging.
    :param logger_name: name assigned to the Logger. If no name is passed the Logger name is going to be the name of
    the module which create the Logger.
    :param level: specify the logging level.
    :param stream: specify the addition of a Stream Handler to the logger. If None is passed is assumed False.
    :param filestream: specify the addition of a FileStream Handler to the logger. If None is passed is assumed False.
    :param formatting: Logger formatting options.
    :param filename: path to the directory (and file name) used for the logs.
    :return: new configured Logger.
    """
    if not logger_name or logger_name is None:
        logger_name = __name__.split(".")[-1].strip("__")

        # create Logger
    logger = logging.getLogger(logger_name)

    if not formatting or formatting is None:
        formatting = f'[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s'
    if not filename or filename is None:
        filename = time.strftime('%H_%M_%S') + '.log'
    datefmt: str = '%H:%M:%S'
    # check for StreamHandler addition
    if stream:
        c_handler = create_stream_handler(level)
        logger.addHandler(format_stream_handler(c_handler, formatting, datefmt))
    # check for FileStreamHandler addition
    if filestream:
        f_handler = create_filestream_handler(level, filename)
        logger.addHandler(format_filestream_handler(f_handler, formatting, datefmt))

    logger.setLevel(level)
    return logger


def log_with_level(logger: logging.Logger, msg: str) -> None:
    """
    Log a message with the level of the given logger.
    :param logger: logger used to log the message.
    :param msg: message to log.
    :return: None
    """
    level = logger.level
    if level == logging.DEBUG:
        logger.debug(msg)
    elif level == logging.INFO:
        logger.info(msg)
    elif level == logging.WARNING:
        logger.warning(msg)
    elif level == logging.ERROR:
        logger.error(msg)
    else:  # is critical
        logger.critical(msg)


# check project structure
logpath = Path.cwd().joinpath('logs').joinpath(time.strftime('%Y-%m-%d'))
check_folder_structure(logpath)

# init logger
app_logger = setup(
    level=logging.INFO, stream=True, filestream=True,
    filename=logpath.joinpath(time.strftime('%H_%M_%S') + '.log')
)
log_with_level(app_logger, f"'{app_logger.name}' logger initialized")


def log(func: Callable[..., Any], logger: logging.Logger) -> Callable[..., Any]:
    """
    Log the function call.
    :param func: called function.
    :param logger: used logger.
    :return: called function result.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        log_with_level(logger, f"Calling {func.__name__}")
        try:
            value = func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            raise e
        log_with_level(logger, f"Finished calling {func.__name__}")
        return value

    return wrapper


def init_log(func: Callable[..., Any], logger: logging.Logger) -> Callable[..., Any]:
    """
    Log the function call.
    :param func: called function.
    :param logger: used logger.
    :return: called function result.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        log_with_level(logger, f"{func.__name__} initialization started")
        try:
            value = func(*args, **kwargs)
        except Exception as e:
            log_with_level(logger, e.__str__())
            raise e
        log_with_level(logger, f"{func.__name__} initialization completed successfully")
        return value

    return wrapper


basic_log = functools.partial(log, logger=app_logger)
basic_init_log = functools.partial(init_log, logger=app_logger)
