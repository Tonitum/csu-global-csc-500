import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("Shopping Cart")


def get_input(prompt: str, var_type: type) -> str | int | float:
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
    logger.info("Welcome to Module 2")
    cart_items: list[tuple[str, float, int]] = []
    total_cart_items: int = 0
    try:
        customer_name: str = get_string("Hello! What is your name? ")
        cart_count: int = get_int(
            "How many items should we add to your shopping cart? "
        )
        if cart_count <= 0:
            logger.warning("Cart count must be positive")
            raise ValueError
        for cart_item in range(cart_count):
            logger.info(f"Item {cart_item + 1}:------------------")
            item_name: str = get_string("Name: ")
            item_cost: float = get_float("Cost: $")
            if item_cost <= 0:
                logger.warning("Item cost must be positive")
                raise ValueError
            item_count: int = get_int("Count: ")
            if item_count <= 0:
                logger.warning("Item count must be positive")
                raise ValueError

            total_cart_items += (
                item_count  # basic arithmetic expression #1, adding to a total count
            )
            cart_items.append((item_name, item_cost, item_count))
    except ValueError:
        return

    logger.info(f"{customer_name}'s cart:")
    logger.info(f"Total items: {total_cart_items}")
    cart_total = 0
    for cart_item in cart_items:
        item_subtotal = (
            cart_item[1] * cart_item[2]
        )  # basic arithmetic expression #2, calculating item cost
        logger.info(f"""------------------
                    Item: {cart_item[0]}
                    Cost: ${cart_item[1]:.2f}
                    Count: {cart_item[2]}
                    Item subtotal: ${item_subtotal:.2f}""")
        cart_total += item_subtotal
    logger.info(f"Cart total: ${cart_total:.2f}")


if __name__ == "__main__":
    main()
