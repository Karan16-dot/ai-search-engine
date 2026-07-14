import time

from utils.logger import logger


class Timer:
    """
    Measures execution time of a block of code.
    """

    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start

        logger.info(
            "%s completed in %.3f seconds",
            self.name,
            elapsed
        )