"""
Dinner guest list.

- Add guest
- Remove Guest
- Show invitations

"""

# List
guest_name = []


def add_guest(): # Add guest
    """Add one guest and their name to the list."""

    name = input("Enter guest name: ").strip().title()

    guest_name.append(name)


def modify_guest(): # Modify guest
    """Modify a guest, ex. rename"""

    # Ask which guest
    name = input("Enter guest to update: ").strip().title()

    # Search for guest name and ask for new name
    if name in guest_name:
        index = guest_name.index(name) # Gets index of entered name
        new_guest = int(input("Enter new name: ").strip().title)
        guest_name[index] = new_guest
        print("Guest updated.")
        
    # If entered name not in guest list
    else:
        print("Guest not found.")


def remove_guest(): # Remove guest
    """Removes selected guest from the list"""


def sort_guests(): # Sort guests
    """Sort guests by alphabetical or numerical order, option given to user"""


def guest_number(): # Show number of guests
    """Show the total number of guests on the list"""


def show_invitations(): # Show invitations
    """Show each invitation for everyone on the list."""


def check_duplicates():  # Duplicate checker
    """Check the list for duplicate names"""


def main(): # Main
    """Main function that calls all the other functions."""

    # Welcome user to course
    print("Welcome to Guest List Creator!")

    while True:
        # Options
        print("\n1- Add Guest")
        print("2- Modify Guest")
        print("3- Remove Guest")
        print("4- Sort Guests")
        print("5- Show Number of Guests")
        print("6- Show Invitations")
        print("7- Check for Duplicates")
        print("0- Exit")

        # Get input
        choice = input("Please enter your choice:")

        if choice == "1":
            # Add a guest to the list
            add_guest()

        elif choice == "2":
            # Modify a guest, ex. rename
            modify_guest()

        elif choice == "3":
            # Remove guest from the list
            remove_guest()

        elif choice == "4":
            # Sort guests by alphabetical or numerical order.
            sort_guests()

        elif choice == "5":
            # Show the total number of guests
            guest_number()

        elif choice == "6":
            # Show each invitation for everyone on the list.
            show_invitations()

        elif choice == "7":
            # Check the list for duplicate names
            check_duplicates()

        elif choice == "0":
            break

        else:
            # everything thats not 0-7
            print("Please enter your choice.")


# Run main function

if __name__ == "__main__":
    main()