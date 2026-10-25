import datetime
from enum import Enum
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


logger = logging.getLogger("Shopping Cart")


class ItemToPurchase:
    """
    Representative object of an item in an online shopping cart.
    """

    item_name: str
    item_price: float
    item_quantity: int
    item_description: str

    def __init__(self):
        """
        Create a new instance of ItemToPurchase with all fields initialized
        to default items.
        """
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        """
        Helper method to print out the details about this item to help reduce the
        amount of repeated code.
        """
        item_cost = self.item_price * self.item_quantity
        output = f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${item_cost:.2f}"
        print(output)


class ShoppingCart:
    def __init__(self, name: str = "none", date: str = "January 1, 2020"):
        self.customer_name: str = name
        self.current_date: str = date
        self.cart_items: list[ItemToPurchase] = []

    # Core Methods:
    def add_item(self, item: ItemToPurchase):  # Adds an object to the list.
        self.cart_items.append(item)

    def remove_item(
        self, item_name: str
    ) -> (
        ItemToPurchase | None
    ):  # Removes an item by name; if not found, output: Item not found in cart. Nothing removed.
        item = self.find_item(item_name)
        if item is not None:
            self.cart_items.remove(item)
            return item
        print("Item not found in cart. Nothing removed")
        return None

    def modify_item(
        self, new_item: ItemToPurchase
    ):  # Updates an item's attributes if it exists in the cart.
        item = self.find_item(new_item.item_name)
        if item is not None:
            item.item_quantity = new_item.item_quantity

    def get_num_items_in_cart(self) -> int:  # Returns total quantity of all items.
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total

    def get_cost_of_cart(self) -> float:  # Returns total cost of all items.
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):  # Displays the full cart or SHOPPING CART IS EMPTY.
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        total = 0
        for item in self.cart_items:
            total += item.item_quantity * item.item_price
            item.print_item_cost()
        print("--------------------------------------------------------------")
        print(f"total {total:.2f}")

    def print_descriptions(self):  # Displays the description of every item in the cart.
        print("--------------------------------------------------------------")
        for item in self.cart_items:
            print(item.item_name, "-", item.item_description)

    def find_item(self, item_name: str) -> ItemToPurchase | None:
        """Return the first cart item with the given name, or None if not found."""
        for item in self.cart_items:
            if item.item_name == item_name:
                return item
        return None


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
        print("Input cancelled")
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


class MenuOption(Enum):
    ADD_ITEM = "a"
    REMOVE_ITEM = "r"
    CHANGE_ITEM = "c"
    OUTPUT_DESCRIPTIONS = "i"
    OUTPUT_CART = "o"
    QUIT = "q"


def get_new_item() -> ItemToPurchase:
    try:
        # Prompt the user for the name of the current item
        item_name: str = get_string("Enter Item Name: ")
        # Prompt the user for the cost of the current item
        item_price: float = get_float("Cost: $")
        # Prompt the user for the quantity of the current item
        item_quantity: int = get_int("Count: ")
        # Prompt the user for the description of the current item
        item_description: str = get_string("Description: ")
    except ValueError as ve:
        # If the user enters an invalid value, log a warning
        # (handled by get_input) and raise an error
        raise ValueError from ve
    if item_price <= 0:
        # If the user entered a value <= 0, then raise an error. An item cannot
        # have a price of 0 or a negative price
        raise ValueError("Item Cost must be greater than 0")
    if item_quantity <= 0:
        # If the user entered a value <= 0, then raise an error. An item cannot
        # have a price of 0 or a negative price. An item cannot have a quanity
        # of 0 or a negative quantity
        raise ValueError("Item Quantity must be greater than 0")
    cart_item = ItemToPurchase()
    cart_item.item_name = item_name
    cart_item.item_price = item_price
    cart_item.item_quantity = item_quantity
    cart_item.item_description = item_description
    return cart_item


def print_menu(cart: ShoppingCart):
    while True:
        # Begin the menu loop
        print("--------------------------------------------------------------")
        print("Welcome to the shopping cart,", cart.customer_name)
        print("Date: ", cart.current_date)
        print("Main Menu")
        print(
            "\ta: Add item\n"
            "\tr: Remove item\n"
            "\tc: Change quantity\n"
            "\ti: Output descriptions\n"
            "\to: Output shopping cart\n"
            "\tq: Quit"
        )

        choice: str = get_string("What would you like to do? ")
        match choice:
            case MenuOption.ADD_ITEM.value:
                try:
                    item = get_new_item()
                except ValueError as ve:
                    print(ve)
                    continue
                if cart.find_item(item.item_name):
                    print(
                        f"An Item with name {item.item_name} already exists. Please try again."
                    )
                    continue
                cart.add_item(item)
            case MenuOption.REMOVE_ITEM.value:
                # Prompt the user for the name of the current item
                item_name: str = get_string("Enter Item Name: ")
                cart.remove_item(item_name)
            case MenuOption.CHANGE_ITEM.value:
                try:
                    # Prompt the user for the name of the current item
                    new_item = ItemToPurchase()
                    new_item.item_name = get_string("Enter Item Name: ")

                    old_item = cart.find_item(new_item.item_name)
                    if old_item is None:
                        print(
                            f"No item with name {new_item.item_name} exists. Please try again."
                        )
                        continue
                    new_item.item_quantity = get_int("Enter New Item Quantity: ")
                    if new_item.item_quantity <= 0:
                        # If the user entered a value <= 0, then raise an error. An item cannot
                        # have a price of 0 or a negative price. An item cannot have a quanity
                        # of 0 or a negative quantity
                        raise ValueError("Item Quantity must be greater than 0")
                    new_item.item_price = old_item.item_price
                    cart.modify_item(new_item)
                except ValueError as ve:
                    print(ve)
                    continue
            case MenuOption.OUTPUT_DESCRIPTIONS.value:
                cart.print_descriptions()
            case MenuOption.OUTPUT_CART.value:
                cart.print_total()
            case MenuOption.QUIT.value:
                break
            case _:
                print(choice, " is not a valid option.")
    print("Goodbye")


def main():
    """
    Main CLI entrypoint
    """
    print("Welcome to Module 6")
    # Get the customer name (to make it more personal)
    customer_name: str = get_string("Hello! What is your name? ")
    cart = ShoppingCart(
        name=customer_name, date=datetime.datetime.today().strftime("%Y-%m-%d")
    )
    print_menu(cart)


if __name__ == "__main__":
    main()
