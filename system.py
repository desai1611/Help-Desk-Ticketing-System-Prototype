from ticket import Ticket

class TicketingSystem:
    def __init__(self):
        # Initializing instance variables
        self.tickets = []  # List to store ticket objects
        self.counter = 2000  # Counter to assign unique ticket IDs
        self.open_tickets = 0  # Counter to keep track of open tickets
        self.total_tickets = 0  # Counter to keep track of total tickets

    def submit_ticket(self):
        # Method to submit a new ticket
        ticket_id = self.counter
        designation = input("Enter Your Designation:")
        employee_code = input("Enter Your Employee Code:")
        email_address = input("Enter Your E-mail ID:")
        problem_description = input("What is the problem:")

        # Creating a new Ticket object
        ticket = Ticket(ticket_id, designation, employee_code,
                        email_address, problem_description)
        self.tickets.append(ticket)  # Adding the ticket to the list
        self.counter += 1
        self.open_tickets += 1  # Incrementing open ticket count
        self.total_tickets += 1  # Incrementing total ticket count

        print("Your ticket is submitted successfully")

    def display_tickets(self):
        # Method to display all tickets
        for ticket in self.tickets:
            print()
            print("***** TICKET *****")
            print("Ticket ID:", ticket.ticket_id)
            print("Designation:", ticket.designation)
            print("Employee Code:", ticket.employee_code)
            print("E-mail:", ticket.email_address)
            print("Problem:", ticket.problem)  # Updated attribute name
            print("Response:", ticket.response)
            print("Status:", ticket.status)

    def response_ticket(self):
        # Method to respond to a ticket
        ticket_id = int(input("Enter Ticket ID: "))
        for ticket in self.tickets:
            if ticket_id == ticket.ticket_id:
                response = input("Enter Response: ")
                ticket.response = response
                ticket.status = "Closed"
                self.open_tickets -= 1  # Decrementing open ticket count
                print("The issue has been resolved")
                break
        else:
            print("Ticket not found.")

    def reopen_ticket(self):
        # Method to reopen a closed ticket
        ticket_id = int(input('Enter Ticket ID: '))
        for ticket in self.tickets:
            if ticket_id == ticket.ticket_id:
                ticket.status = "Reopened"
                self.open_tickets += 1  # Incrementing open ticket count
                print("Ticket reopened successfully.")
                break
        else:
            print("Ticket not found.")

    def status(self):
        # Method to display total and open ticket counts
        print("Total Tickets:", self.total_tickets)
        print("Open Tickets:", self.open_tickets)


def main():
    ticketing_system = TicketingSystem()

    while True:
        print("===== TICKETING SYSTEM MAIN MENU =====")
        print("1. Submit a Ticket")
        print("2. View Tickets")
        print("3. Respond to a Ticket")
        print("4. Reopen a Ticket")
        print("5. View open/closed tickets")
        print("6. Quit the System")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            ticketing_system.submit_ticket()
        elif choice == '2':
            ticketing_system.display_tickets()
        elif choice == '3':
            ticketing_system.response_ticket()
        elif choice == '4':
            ticketing_system.reopen_ticket()
        elif choice == '5':
            ticketing_system.status()
        elif choice == '6':
            print("Exiting the ticketing system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
