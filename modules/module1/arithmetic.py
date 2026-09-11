import logging


def add(a: float, b: float) -> float:
    """
    Returns result of a + b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Returns result of a - b
    """
    return a - b


def divide(a: float, b: float) -> float:
    """
    Returns result of a / b
    if b is negative, raises ValueError
    """
    if b == 0:
        raise ValueError("Cannot divide: Second number cannot be 0")
    return a / b


def multiply(a: float, b: float) -> float:
    """
    Returns result of a * b
    """
    return a * b


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("Module 1")


def get_input(prompt: str):
    try:
        number_input = input(prompt)
    except EOFError as ee:
        logger.warning("Input cancelled")
        raise ee

    try:
        number = float(number_input)
    except ValueError as ve:
        logger.info("Input must be valid floating point numbers")
        logger.info(f"Recieved input {number_input}")
        raise ve
    return number


def main():
    """
    Main CLI entrypoint
    """
    logger.info("Welcome to Module 1")
    try:
        a = get_input("First number: ")
        b = get_input("Second number: ")
    except ValueError:
        return
    # get input
    # calculate numbers
    logger.info("%g + %g = %g", a, b, add(a, b))
    logger.info("%g - %g = %g", a, b, subtract(a, b))
    logger.info("%g * %g = %g", a, b, multiply(a, b))
    try:
        logger.info("%g / %g = %g", a, b, divide(a, b))
    except ValueError as ve:
        logger.warning(ve.args[0])
        return


if __name__ == "__main__":
    main()
