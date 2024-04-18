class Ticket:
    # Represents a ticket for assistance request in the ticketing system.

    # Constructor method to initialize a new Ticket object with provided attributes.
    def __init__(self, ticket_id, designation, employee_code, email_address, problem):
        # start ticket attributes
        self.ticket_id = ticket_id
        self.designation = designation
        self.employee_code = employee_code
        self.email_address = email_address
        self.problem = problem
        # Default response and status
        self.response = "Not Provided"
        self.status = "Open"

        # Process the problem
        self.process_problem()

    # Method to process the problem and update response and status accordingly
    def process_problem(self):
        if "change" in self.problem and "password" in self.problem:
            self.generate_new_password()
            self.status = "Closed"

    # Method to generate a new password based on employee code and designation
    def generate_new_password(self):
        password = self.employee_code[:2] + self.designation[:3]
        self.response = f"Your new password is -> {password}"
