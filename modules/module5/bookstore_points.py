import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("Bookstore Points")


def get_input(prompt: str, var_type: type) -> str | int | float:
    """
    General function for obtaining user input

    Args:
        prompt: A string that is displayed to the user with the input prompt
        var_type: Python Type that the value should be cast as

    Returns:
        A value of type <var_type>

    Raises:
        EOFError: If the user cancels the input prompt
        ValueError: If the user inputs a value not castable as type <var_type>
    """
    try:
        value_input = input(prompt)
    except EOFError as ee:
        logger.warning("Input cancelled")
        raise ee
    try:
        value: str | int | float = var_type(value_input)
    except ValueError as ve:
        logger.warning(f"Input must be valid {var_type}")
        logger.warning(f"Received input {value_input}")
        raise ve
    return value


def get_int(prompt: str) -> int:
    """
    Int specific wrapper around get_input

    Args:
        prompt: A string that is displayed to the user with the input prompt

    Returns:
        The int value result of input

    Raises:
        EOFError: If the user cancels the input prompt
        ValueError: If the user inputs a value not castable as int
    """
    try:
        int_value = get_input(prompt, int)
    except EOFError as ee:
        raise ee
    except ValueError as ve:
        raise ve
    if not isinstance(int_value, int):
        raise ValueError("Did not get integer value")
    return int_value


NO_REWARD_POINTS = 0
LEVEL_ONE_POINTS = 2
LEVEL_TWO_POINTS = 4
LEVEL_THREE_POINTS = 6
LEVEL_FOUR_POINTS = 8

POINTS_REFERENCE = {
    NO_REWARD_POINTS: 0,  # 0 book
    LEVEL_ONE_POINTS: 5,  # 2 books
    LEVEL_TWO_POINTS: 15,  # 4 books
    LEVEL_THREE_POINTS: 30,  # 6 books
    LEVEL_FOUR_POINTS: 60,  # 8+ books
}


def main():
    """
    Main CLI entrypoint
    """
    logger.info("Welcome to Module 5")
    book_count: int
    try:
        # Prompt the user for the number of purchased books
        book_count = get_int("Enter the number of books purchased this month: ")
        if book_count < 0:
            # If the user entered a negative value, log a warning and exit
            logger.warning("Must enter a value >= 0")
            return
    except ValueError:
        # If the user enters an invalid int value, log a warning
        # (handled by get_int) and exit
        return

    # initialize the number of earned points
    points_count = 0
    if book_count >= NO_REWARD_POINTS and book_count < LEVEL_ONE_POINTS:
        points_count = POINTS_REFERENCE[NO_REWARD_POINTS]
    elif book_count >= LEVEL_ONE_POINTS and book_count < LEVEL_TWO_POINTS:
        points_count = POINTS_REFERENCE[LEVEL_ONE_POINTS]
    elif book_count >= LEVEL_TWO_POINTS and book_count < LEVEL_THREE_POINTS:
        points_count = POINTS_REFERENCE[LEVEL_TWO_POINTS]
    elif book_count >= LEVEL_THREE_POINTS and book_count < LEVEL_FOUR_POINTS:
        points_count = POINTS_REFERENCE[LEVEL_THREE_POINTS]
    elif book_count >= LEVEL_FOUR_POINTS:
        points_count = POINTS_REFERENCE[LEVEL_FOUR_POINTS]
    print("You have earned", points_count, "points for purchasing", book_count, "books")


if __name__ == "__main__":
    main()
