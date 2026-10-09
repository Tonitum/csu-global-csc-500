import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("Bookstore Points")


def main():
    """
    Main CLI entrypoint
    """
    logger.info("Welcome to Module MODULE_NUMBER")


if __name__ == "__main__":
    main()
