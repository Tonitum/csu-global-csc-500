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
    if b is 0, raises ValueError
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
        num1 = get_input("Please input num1: ")
        num2 = get_input("Please input num2: ")
    except ValueError:
        return
    # get input
    # calculate numbers
    logger.info("%g + %g = %g", num1, num2, add(num1, num2))
    logger.info("%g - %g = %g", num1, num2, subtract(num1, num2))
    logger.info("%g * %g = %g", num1, num2, multiply(num1, num2))
    try:
        logger.info("%g / %g = %g", num1, num2, divide(num1, num2))
    except ValueError as ve:
        logger.warning(ve.args[0])
        return


if __name__ == "__main__":
    main()
