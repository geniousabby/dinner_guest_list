"""
Dinner guest list.

- Add guest
- Remove Guest
- Show invitations

"""

# Create empty list for guest names
guest_name = []


def add_guest(): # Add guest
    """Add one guest name to the list."""

    # Get user input
    name = input("Enter guest name: ").strip().title()

    # Add entered name to guest list
    guest_name.append(name) # Append adds the name to the end of the list
    print("Guest added.")


def modify_guest(): # Rename guest
    """Rename a guest that has already been added."""

    # Ask which guest to update
    name = input("Enter the guest name to update: ").strip().title()

    # Search for guest name and ask for new name
    if name in guest_name:
        index = guest_name.index(name)
        new_name = str(input("Enter new name: ").strip().title())
        guest_name[index] = new_name
        print("Guest updated.")

    # If entered name not in guest list
    else:
        print("Guest not found.")


def remove_guest(): # Remove guest
    """Removes selected guest from the list."""

    # Ask for name to remove
    name = input("Enter a name to remove: ").strip().title()

    # Search for name in list
    if name in guest_name:
        index = guest_name.index(name)
        guest_name.pop(index) # Remove guest from index using "pop"
        print("Guest removed.")

    # If input not a name in guest list
    else:
        print("Guest not found.")


def sort_guests(): # Sort guests
    """Sort guests by alphabetical or numerical order, option given to user."""

    # Get user input
    sort = input(
        "Would you like to sort the guests by numerical or alphabetical order? (n or a): "
        ).strip().lower()

    # If user entered "n"
    if sort == "n":
        print("Here are the guests sorted by date added:")
        for name in guest_name:
            print(name)

    # If user entered "a"
    elif sort == "a":
        print("Here are the guests sorted alphabetically:")
        for name in sorted(guest_name):
            print(name)

    # If there are no names in the list
    elif not guest_name: # If there are no guests in the list
        print("No guests in the list")

    # Anything else
    else:
        print("Invalid choice. Please enter 'n' or 'a'.")


def guest_number(): # Show number of guests
    """Show the total number of guests on the list."""

    print(f"Total guests: {len(guest_name)}") # Len counts the number of guests in the list


def show_invitations(): # Show invitations
    """Show each invitation for everyone on the list."""

    # If guest name is empty
    if not guest_name:
        print("No guest in the list.")
        return

    # Sort through names and print guest list
    print("\nGuest Invitation List:")
    for i in range(len(guest_name)): # Loop through the list of guest names using their index
        print(f"{guest_name[i]}, you are invited to my dinner party!")


def check_duplicates():  # Duplicate checker
    """Check the list for duplicate names."""

    # Get name to check for duplicates
    name = input("Please enter a name to see if it's in the list already: ").strip().title()

    # Find name in list
    if name in guest_name:
        print("That name is already in the list.")

    # If name not in list
    elif name not in guest_name:
        print("That name is not in the list.")

    # If name not entered
    else:
        print("Please enter a valid name.")


def main(): # Main function
    """Main function that calls all the other functions."""

    # Welcome user to course and show options
    print("Welcome to Guest List Creator!")

    # Choices loop
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
        choice = input("Please enter your choice: ")

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
            # Exit game
            print("Thanks for playing!")
            break

        else:
            # Everything thats not 0-7
            print("Please enter a valid choice.")


# Run main function
if __name__ == "__main__":
    main()
