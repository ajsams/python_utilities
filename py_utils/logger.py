"""
Logger Module

This module provides a Logger class and a log_function decorator for logging messages.
It can be used for both centralized logging across a project or script-specific logging.

Classes
-------
Logger
    A class for logging messages with methods for logging informational, warning, error,
    and debug messages, as well as setting log parameters.

Functions
---------
log_function(func=None, *, logger_instance: Optional[Logger] = None)
    A decorator to log the beginning and end of a function, including the module name.
    Can use either the built-in logger instance or a custom Logger instance.

Instances
---------
logger
    An instance of the Logger class initialized for centralized logging across a project.
"""

import functools
import logging
from pathlib import Path
from typing import Optional


class Logger:
    """
    Class for logging messages.

    This class provides a Logger class that wraps around the Python logging module
    to facilitate formatted print and logging statements. It includes methods for
    logging informational messages, debug messages, and processing logs.

    Attributes
    ----------
    logger : logging.Logger
        - The logger object from the logging module.
    log_file : Optional[pathlib.Path]
        - The file to log messages to. If None, no log file is set.

    Examples
    --------

    .. code-block:: python

        from utils.logs import logs

        # General Usage.
        logs.info("This is an informational message.")
        logs.warning("This is a warning message.")
        logs.error("This is an error message.")
        logs.debug("This is a debug message.")
        logs.processing_log("Starting the processing stage...")

        # Setting log configuration parameters, this should be done once right
        # after the config is first initialized:

        from utils.logs import set_log_config_params
        from pathlib import Path

        set_log_config_params(log_level="DEBUG", write_log=True, logfile=Path("logfile.log"))

        # Using the ``@log_function`` decorator to log the beginning and
        # end of a function in debug mode:

        from utils.logs import log_function

        @log_function
        def example_function():
            # Function implementation
            pass

        example_function()
    """

    def __init__(
        self, log_file: Optional[Path] = None, level: int = logging.INFO
    ) -> None:
        """
        Initialize the Logger with an optional log file and logging level.

        Parameters
        ----------
        log_file : pathlib.Path, optional
            The file to log messages to.
        level : int
            The logging level (e.g., logging.DEBUG, logging.INFO).
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        self.log_file = log_file

        # Create console handler and set level to the specified level.
        handler = logging.StreamHandler()
        handler.setLevel(level)

        # Create formatter.
        formatter = logging.Formatter(f"%(asctime)s - %(levelname)s - %(message)s")

        # Add formatter to handler.
        handler.setFormatter(formatter)

        # Add handler to logger.
        self.logger.addHandler(handler)

        if log_file:
            self.set_log_file(log_file)

    def set_params(self, log_level: str, log_file: Optional[Path] = None) -> None:
        """
        Set the logging level and log file.

        Parameters
        ----------
        log_level : str
            The logging level to set. Can be "INFO", "DEBUG", "WARNING", "ERROR",
            or "CRITICAL".
        log_file : Optional[pathlib.Path], optional
            The file to log messages to. If None, no log file is set.
        """
        log_level_value = getattr(logging, log_level.upper(), logging.INFO)
        self.logger.setLevel(log_level_value)

        for handler in self.logger.handlers:
            handler.setLevel(log_level_value)

        if log_file is not None:
            self.set_log_file(log_file)
        else:
            self.clear_log_file()

    def info(self, msg: str) -> None:
        """
        Log a message to the terminal and optionally to a file.

        Parameters
        ----------
        msg : str
            The message to log.
        """
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        """
        Log a warning message to the terminal and optionally to a file.

        Parameters
        ----------
        msg : str
            The message to log.
        """
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """
        Log an error message to the terminal and optionally to a file.

        Parameters
        ----------
        msg : str
            The message to log.
        """
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        """
        Log an error message to the terminal and optionally to a file.

        Parameters
        ----------
        msg : str
            The message to log.
        """
        self.logger.critical(msg)

    def set_log_file(self, log_file: Path) -> None:
        """
        Set a file to log messages to.

        Clears the log file, if it already exists, by opening it in write mode.

        Parameters
        ----------
        log_file : pathlib.Path
            The file to log messages to.
        """
        self.log_file = log_file
        # Clear the log file by opening it in write mode.
        with open(self.log_file, "w"):
            pass
        # Check if a file handler already exists.
        if not any(
            isinstance(handler, logging.FileHandler) for handler in self.logger.handlers
        ):
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter(f"%(asctime)s - %(levelname)s - %(message)s")
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def clear_log_file(self) -> None:
        """
        Clear the log file setting.

        This method removes the file handler from the logger and sets the log file to None.
        """
        self.log_file = None
        for handler in self.logger.handlers[:]:
            if isinstance(handler, logging.FileHandler):
                self.logger.removeHandler(handler)

    def debug(self, msg: str) -> None:
        """
        Log a debug message to the terminal.

        Parameters
        ----------
        msg : str
            A message string that informs the user what stage of processing
            the program is currently in.

        Returns
        -------
        None
        """
        self.logger.debug(msg)

    def processing_log(self, msg: str) -> None:
        """
        Log a section begin/end level message.

        Parameters
        ----------
        msg : str
            A message string that informs the user what stage of processing
            the program is currently in.

        Returns
        -------
        None
        """
        outmsg = (
            "\n========================================\n"
            f"{msg}\n"
            "========================================"
        )
        self.logger.info(outmsg)


# Initialize an instance of Logger to use a centralized log across a project.
logger = Logger()


def log_function(func=None, *, logger_instance: Optional[Logger] = None):
    """
    Decorator to log the beginning and end of a function, including the module name.

    Parameters
    ----------
    func : function
        The function to be wrapped by the decorator.
    logger_instance : Optional[Logger], default=None
        An instance of the Logger class. If None, the built-in logger is used.

    Returns
    -------
    wrapper : function
        The wrapped function with logging.

    Examples
    --------
    Using the built-in logger instance:

    .. code-block:: python

        from py_utils.logger import log_function

        @log_function
        def example_function():
            # Function implementation
            pass

        example_function()

    Using a custom logger instance:

    .. code-block:: python

        from py_utils.logger import Logger, log_function
        from pathlib import Path

        custom_logger = Logger(log_file=Path("custom_logfile.log"), level=logging.DEBUG)

        @log_function(logger_instance=custom_logger)
        def another_example_function():
            # Function implementation
            pass

        another_example_function()
    """

    if func is None:
        return lambda f: log_function(f, logger_instance=logger_instance)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger_to_use = logger_instance if logger_instance else logger
        module_name = func.__module__
        logger_to_use.debug(f"{module_name}.{func.__name__} BEGIN")
        result = func(*args, **kwargs)
        logger_to_use.debug(f"{module_name}.{func.__name__} END")
        return result

    return wrapper
