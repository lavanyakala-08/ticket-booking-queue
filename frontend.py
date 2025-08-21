from app import TicketBooking

def main():
    system = TicketBooking(total_tickets=5)

    while True:
        print("\n--- Ticket Booking System ---")
        print("1. Book Ticket")
        print("2. Serve Customer")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            print(system.book_ticket(name))
        elif choice == "2":
            print(system.serve_customer())
        elif choice == "3":
            print("Exiting... Bye 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
