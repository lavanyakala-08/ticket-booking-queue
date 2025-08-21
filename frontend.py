# frontend.py

def display_menu():
    """Prints the main menu options for the user."""
    print("\n--- Ticket Booking System Menu ---")
    print("1. Book a new ticket")
    print("2. Process next ticket booking")
    print("3. View next person in line")
    print("4. Check queue size")
    print("5. Exit")
    print("-----------------------------------")

def get_user_choice():
    """
    Prompts the user for their choice and returns a validated input.

    Returns:
        str: The user's choice as a string.
    """
    return input("Enter your choice (1-5): ").strip()

def get_booking_details():
    """
    Prompts the user for their name and returns it.

    Returns:
        str: The name provided by the user.
    """
    name = input("Enter your name for the booking: ").strip()
    return name

