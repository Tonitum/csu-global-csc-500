import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("Course Information")


course_room: dict[str, str] = {}
course_instructor: dict[str, str] = {}
course_time: dict[str, str] = {}

# CSC101
course_room["CSC101"] = "3004"
course_instructor["CSC101"] = "Haynes"
course_time["CSC101"] = "12:30 PM"

# CSC102
course_room["CSC102"] = "4501"
course_instructor["CSC102"] = "Alvarado"
course_time["CSC102"] = "08:00 AM"

# CSC103
course_room["CSC103"] = "6755"
course_instructor["CSC103"] = "Rich"
course_time["CSC103"] = "09:15 AM"

# NET110
course_room["NET110"] = "1244"
course_instructor["NET110"] = "Burke"
course_time["NET110"] = "05:00 PM"

# COM241
course_room["COM241"] = "1411"
course_instructor["COM241"] = "Lee"
course_time["COM241"] = "11:00 AM"


def get_string(prompt: str) -> str:
    """
    Function to make getting string input from users encapsulated and easy.

    Args:
        prompt: A string that is displayed to the user with the input prompt

    Returns:
        The string value result of input

    Raises:
        EOFError: If the user cancels the input prompt
        ValueError: If the user inputs a value not castable as string
    """
    try:
        value = input(prompt)
    except EOFError as ee:
        print("Input cancelled")
        raise ee
    # Normalize the user input by making all letters uppercase. This is to
    # allow more flexibility with user input while maintaining program
    # functionality and efficiency.
    normalized_value = value.strip().upper()
    return normalized_value


def print_course_information(course: str) -> None:
    """
    Pretty-print the course information from the three information dictionaries

    Args:
        course: A string course id that acts as the 'key' to the information
            dictionaries
    Returns:
        None
    """
    print(f"Course Information: {course}")
    print("-" * 30)
    print(f"Room:       {course_room[course]}")
    print(f"Instructor: {course_instructor[course]}")
    print(f"Time:       {course_time[course]}")
    print()


def main() -> None:
    """
    Main CLI entrypoint
    """
    logger.info("Welcome to Module 7")
    print("Welcome to the Course Information Tool")
    # Begin the main program loop. This loop runs until the user enters Q/QUIT
    while True:
        # Prompt the user for a course number
        try:
            course_number = get_string("Please enter a course number(Q/QUIT to exit): ")
        except EOFError:
            # The function "get_string" handles printing a warning to the user,
            # so we can just end the program
            break

        # If the user enters a sentinel value, exit the program
        if course_number in ["QUIT", "Q"]:
            print("Exiting")
            break

        # Check if the user entered a valid course number
        if course_number not in course_room:
            # If they did not, print an error message and show them the
            # available courses with information
            print("That course number does not exist. Please try again.")
            print("Available courses: ")
            # Note: we only need to look at one dictionary's keys to get all of
            # our course names.
            for key in course_room.keys():
                print(f"- {key}")
            continue
        # If the user entered a course number, print out the information about
        # that course in a visually pleasing and useful way.
        print_course_information(course_number)


if __name__ == "__main__":
    main()
