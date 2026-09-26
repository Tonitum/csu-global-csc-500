import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("Restaurant Tip Calculator")

# Define global variables for the Sales Tax and Tip rates to support alternate scenarios
TIP_PERCENTAGE = 0.18
SALES_TAX_PERCENTAGE = 0.07


def main():
    """
    Main CLI entrypoint
    """
    logger.info("Welcome to Module 3")
    try:
        # Load the base cost of the meal.
        input_food_charge = input("How much did the food cost? $")
    except EOFError:
        # If the user cancelles the input, log it and exit gracefully
        logger.warning("Input cancelled")
        return

    try:
        # Attempt to cast the base cost input as a floating point number
        food_charge: float = float(input_food_charge)
    except ValueError:
        # If this fails, that likely means the user input an invalid value
        # Log this as a warning and exit
        logger.warning("Input must be valid float")
        logger.warning(f"Received input {input_food_charge}")
        return

    if food_charge <= 0:
        # If the user entered 0 or a negative number for the meal, we consider
        # that an invalid input (though it is a valid number).
        # Meals do not cost $0 or less
        logger.warning("Received an invalid amount for food cost.")
        logger.warning("Food cost must be greater than 0.")
        return

    # Calculate the tip based on the base food charge
    tip_amount = TIP_PERCENTAGE * food_charge
    # Calculate the sales tax based on the base food charge
    sales_tax_amount = SALES_TAX_PERCENTAGE * food_charge
    # Calculate the total cost
    total_charge = food_charge + tip_amount + sales_tax_amount

    # Print each line item and its cost to the user
    logger.info("---------------")
    logger.info(f"Food Cost ${food_charge:.2f}")
    logger.info(f"Sales Tax ${sales_tax_amount:.2f}")
    logger.info(f"Tip ${tip_amount:.2f}")
    logger.info("---------------")
    logger.info(f"Total Charge ${total_charge:.2f}")
    logger.info("---------------")


if __name__ == "__main__":
    # If this script is executed directly (e.g. python3 restaurant_calculator.py)
    # run the `main` function
    main()
