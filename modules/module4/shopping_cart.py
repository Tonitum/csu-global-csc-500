import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("Shopping Cart")


SENTINEL_VALUES = ["quit", "q"]

class ItemToPurchase:
    item_name: str
    item_price: float
    item_quantity: int

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        output = f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${(self.item_price * self.item_quantity):.2f}"
        logger.info(output)


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


def get_string(prompt: str) -> str:
    """
    String specific wrapper around get_input

    Args:
        prompt: A string that is displayed to the user with the input prompt

    Returns:
        The string value result of input

    Raises:
        EOFError: If the user cancels the input prompt
        ValueError: If the user inputs a value not castable as string
    """
    try:
        string_value = get_input(prompt, str)
    except EOFError as ee:
        raise ee
    except ValueError as ve:
        raise ve
    if not isinstance(string_value, str):
        raise ValueError("Did not get string value")
    return string_value


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


def get_float(prompt: str) -> float:
    """
    Float specific wrapper around get_input

    Args:
        prompt: A string that is displayed to the user with the input prompt

    Returns:
        The float value result of input

    Raises:
        EOFError: If the user cancels the input prompt
        ValueError: If the user inputs a value not castable as float
    """
    try:
        float_value = get_input(prompt, float)
    except EOFError as ee:
        raise ee
    except ValueError as ve:
        raise ve
    if not isinstance(float_value, float):
        raise ValueError("Did not get float value")
    return float_value


def main():
    """
    Main CLI entrypoint
    """
    logger.info("Welcome to Module 4")
    # Create the list of all items to be added to the cart
    cart_items: list[ItemToPurchase] = []

    # Create a variable to track the total number of items in the cart
    # We need a separate variable for this because each ItemToPurchase may
    # have a quantity greater than 1, so we cannot just use the length of
    # cart_items
    total_cart_items: int = 0

    # Get the customer name (to make it more personal)
    customer_name: str = get_string("Hello! What is your name? ")

    while True:
        # Begin the item addition loop
        try:
            # Prompt the user for the name of the current item
            item_name: str = get_string(
                "Enter Item Name (enter 'quit' or 'q' to stop): "
            )
        except ValueError:
            # If the user enters an invalid string value, log a warning 
            # (handled by get_string) and return the loop to the beginning
            continue
        if item_name in SENTINEL_VALUES:
            # If the user enters one of the sentinel values, we can stop
            # the loop.
            break
        try:
            # Prompt the user for the cost of the current item
            item_price: float = get_float("Cost: $")
        except ValueError:
            # If the user enters an invalid float value, log a warning 
            # (handled by get_float) and return the loop to the beginning
            continue
        if item_price <= 0:
            # If the user entered a value <= 0, then log a warning and return
            # to the beginning of the loop. An item cannot have a price of 0
            # or a negative price
            logger.warning("Item Cost must be greater than 0")
            continue
        try:
            # Prompt the user for the quantity of the current item
            item_quantity: int = get_int("Count: ")
        except ValueError:
            # If the user enters an invalid int value, log a warning 
            # (handled by get_int) and return the loop to the beginning
            continue
        if item_quantity <= 0:
            # If the user entered a value <= 0, then log a warning and return
            # to the beginning of the loop. An item cannot have a quanity of 0
            # or a negative quantity
            logger.warning("Item Quantity must be greater than 0")
            continue

        # Add quantity to cart item count
        total_cart_items += item_quantity
        # Instantiate a new ItemToPurchase and assign the user input
        cart_item = ItemToPurchase()
        cart_item.item_name = item_name
        cart_item.item_price = item_price
        cart_item.item_quantity = item_quantity

        # Add the item to the cart list
        cart_items.append(cart_item)

    logger.info(f"{customer_name}'s cart:")
    # Variable to track the total cost of the items in the cart
    cart_total = 0
    # For each item in the cart, calculate the subtotal and print it out,
    # and add it to the running cart total
    for cart_item in cart_items:
        item_subtotal = (
            cart_item.item_price * cart_item.item_quantity
        )
        cart_item.print_item_cost()
        cart_total += item_subtotal
    # Output the final results
    logger.info(f"Total items: {total_cart_items}")
    logger.info(f"Cart total: ${cart_total:.2f}")


if __name__ == "__main__":
    main()
