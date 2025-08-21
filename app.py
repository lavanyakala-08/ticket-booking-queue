# app.py

from queue import Queue
from frontend import display_menu, get_user_choice, get_booking_details

class TicketBookingSystem:
    """Manages the ticket booking process using a queue."""

    def __init__(self):
        self.booking_queue = Queue()
        self.next_booking_id = 1

    def run(self):
        """Main method to run the ticket booking system."""
        print("🎫 Welcome to the Ultimate Ticket Booking System! 🎫")
        while True:
            display_menu()
            choice = get_user_choice()

            if choice == '1':
                self.handle_new_booking()
            elif choice == '2':
                self.process_next_booking()
            elif choice == '3':
                self.view_next_person()
            elif choice == '4':
                self.check_queue_size()
            elif choice == '5':
                print("Thank you for using the system. Have a great day! 👋")
                break
            else:
                print("❌ Invalid choice. Please select a number from the menu.")

    def handle_new_booking(self):
        """Adds a new booking to the queue."""
        name = get_booking_details()
        if name:
            booking = {"id": self.next_booking_id, "name": name, "status": "pending"}
            self.booking_queue.enqueue(booking)
            print(f"✅ Booking for {name} added to the queue. Your booking ID is {self.next_booking_id}.")
            self.next_booking_id += 1
        else:
            print("❗ Name cannot be empty. Please try again.")

    def process_next_booking(self):
        """Processes and confirms the next booking in the queue."""
        if not self.booking_queue.is_empty():
            processed_booking = self.booking_queue.dequeue()
            print(f"🎉 Booking ID {processed_booking['id']} for {processed_booking['name']} has been processed and confirmed!")
        else:
            print("⏳ The queue is currently empty. No bookings to process.")

    def view_next_person(self):
        """Shows the next person in line without processing their booking."""
        if not self.booking_queue.is_empty():
            next_booking = self.booking_queue.peek()
            print(f"👀 Next in line: {next_booking['name']} (Booking ID: {next_booking['id']}).")
        else:
            print("⏳ The queue is currently empty.")

    def check_queue_size(self):
        """Displays the current number of people in the queue."""
        size = self.booking_queue.size()
        print(f"📊 There are {size} people currently in the queue.")

# Run the application
if __name__ == "__main__":
    app = TicketBookingSystem()
    app.run()

