import random

# Database to store the available seats
seats = {
    'A': [1, 2, 3, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [1, 2, 3, 4, 5]
}

# Database to store registered users
users = {}

# Function to register a new user
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("Registration Failed: Username already exists.")
    else:
        users[username] = password
        print("Registration Successful: Registration successful!")

# Function to authenticate a user
def authenticate_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login Successful: Login successful!")
    else:
        print("Login Failed: Invalid username or password.")

# Function to book a ticket
def book_ticket():
    seat = input("Enter seat class (A, B, C, D): ")
    if seat in seats:
        row = int(input("Enter row number: "))
        if row in seats[seat]:
            seats[seat].remove(row)
            ticket_number = random.randint(1000, 9999)
            send_email("Ticket Booked", f"Ticket booked!\nTicket Number: {ticket_number}")
            print(print_ticket(seat, row, ticket_number))
        else:
            print("Invalid Row: Invalid row number.")
    else:
        print("Invalid Seat: Invalid seat class.")

# Function to cancel a ticket
def cancel_ticket():
    ticket_number = int(input("Enter ticket number: "))
    # Logic to cancel the ticket and make the seat available again
    print("Ticket Cancelled: Ticket cancelled!")

# Function to send email notification
def send_email(subject, message):
    # Logic to send email notification to the user
    pass

# Function to print the ticket
def print_ticket(seat, row, ticket_number):
    # Logic to generate and print the ticket
    pass

# Function to search for trains and view schedules
def search_trains():
    # Logic to search for trains and display schedules
    pass

# Prompt user for action
while True:
    print("\nTrain Ticket Booking System")
    print("1. Register")
    print("2. Login")
    print("3. Book a ticket")
    print("4. Cancel a ticket")
    print("5. Search trains")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        authenticate_user()
    elif choice == "3":
        book_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        search_trains()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
