import tyro
from project.foundation import add
import logging

logger = logging.getLogger(__name__)


def add_cli(a: int, b:int) -> None:
    """Add two numbers

    Args:
        a: the first number
        b: the second number
    """
    logger.info(f"The sum of {a} and {b} is {add(a, b)}")
