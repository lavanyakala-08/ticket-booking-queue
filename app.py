from queue import Queue

# Ticket Booking System
class TicketBooking:
    def __init__(self, total_tickets=5):
        self.queue = Queue()
        self.total_tickets = total_tickets

    def book_ticket(self, name):
        if self.total_tickets > 0:
            self.queue.enqueue(name)
            self.total_tickets -= 1
            return f"✅ Ticket booked for {name}"
        else:
            return "❌ No tickets available"

    def serve_customer(self):
        person = self.queue.dequeue()
        if person:
            return f"🎟️ Ticket issued to {person}"
        return "Queue is empty!"
