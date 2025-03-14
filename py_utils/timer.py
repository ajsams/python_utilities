import logging
import time
from typing import Optional

from tqdm import tqdm


class Timer:
    """A context manager to time blocks of code.

    This class implements the context manager protocol (__enter__ and __exit__ methods).

    When you enter the context, it records the start time.
    When you exit the context, it records the end time and logs the elapsed time.

    Attributes
    ----------
    name : str
        Text that prints before listing the elapsed time.
    logger : Optional[logging.Logger]
        Logging module used for logging info. If None, no logging is performed.
    total : Optional[int]
        Total number of iterations for the progress bar. If None, no progress bar is shown.
    progress_bar : Optional[tqdm.tqdm]
        Progress bar object from tqdm.

    Methods
    -------
    set_logger(logger: logging.Logger) -> None
        Set the logger for the Timer instance.
    update(n: int = 1) -> None
        Update the progress bar by n steps.

    Examples
    --------
    .. code-block:: python

        from utils.timer import Timer

        # No progress bar.
        with Timer("Timing a block of code"):
            # Do stuff that you want to time

        # To indicate progress for each stage in a loop.
        with Timer("Timing a block of code", total=100) as timer:
            for i in range(100):
                # Do stuff that you want to time
                timer.update(1)

        # To indicate progress in a single long-running task.
        with Timer("Timing a long-running task", total=3) as timer:
            # Stage 1
            time.sleep(2)
            timer.update(1)
            # Stage 2
            time.sleep(3)
            timer.update(1)
            # Stage 3
            time.sleep(1)
            timer.update(1)
    """

    def __init__(
        self,
        name: str,
        total: Optional[int] = None,
        logger: Optional[logging.Logger] = None,
    ):
        # Initialize the Timer object with a name, logger, and optional progress bar.
        self.name = name
        self.logger = logger
        self.total = total
        self.progress_bar = None

    def set_logger(self, logger: logging.Logger) -> None:
        """Set the logger for the Timer instance.

        Parameters
        ----------
        logger : logging.Logger
            The logger to use for logging info.
        """
        self.logger = logger

    def __enter__(self):
        self.start = time.time()
        if self.total is not None:
            self.progress_bar = tqdm(total=self.total, desc=self.name)
        return self

    # Even though not used, exc_type, exc_val, exc_tb are required for __exit__.
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = self.end - self.start
        if self.progress_bar is not None:
            self.progress_bar.close()
        if self.logger:
            self.logger.info(f"{self.name} took {self.elapsed:4.2f} seconds.\n")
        else:
            print(f"{self.name} took {self.elapsed:4.2f} seconds.\n")

    def update(self, n: int = 1) -> None:
        if self.progress_bar is not None:
            self.progress_bar.update(n)
