### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox(email_address, subject, content):
    email = Email(email_address, subject, content)
    inbox.append(email)
    # Create 3 sample emails and add it to the Inbox list.
populate_inbox("sam@email.com", "Happy Birthday", "Great day ahead for you!")
populate_inbox("jamjar@email.com", "Lunch date", "The table is booked for 2PM")
populate_inbox("aden@email.com", "Great food", "The food is great")
# Decided to call the function multiply times externally. 


def list_emails():
    for i, email in enumerate(inbox):
        print(f"{i} {email.email_address}")
    # Create a function which prints the email’s subject_line, along with a corresponding number.
# Used a for loop to take the enumeration and email object, displaying it within an 
# f string.

# The provided documentation referenced the following; This function can be used to list the messages when the user
# chooses to read, mark as spam, and delete an email. I cant see a reason to implement this, so have omitted. 

def read_email(index):
    email = inbox[index]
    print(f'''
          From: {email.email_address}\n
          Subject: {email.subject_line}\n
          Content: {email.email_content}\n''')
    print(f"NOTIFICATION: Email from {email.email_address} marked as read\n")
    email.mark_as_read()
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        in_inbox = True
        while in_inbox:
            print("Inbox: All ---------------")
            list_emails()
            print("-----------------------------")
            email_selection = int(input("Which email would you like to read? Enter a number: "))
            if email_selection >= len(inbox):
                print(f"Please enter a number in range of 0-{len(inbox) - 1}")
            else:
                read_email(email_selection)
                user_read_again = input("Back to Inbox? (Y or N)").lower()
                if user_read_again == "n":
                    in_inbox = False
    # Added an additional while loop to allow the user to cycle back into the inbox
    # used .lower() to support bug avoidance.
        
    elif user_choice == 2:
        in_unread = True
        while in_unread:
            print("Inbox: Unread ---------------")
            for email in inbox:
                if email.has_been_read == False:
                    print(f"Email Subject: {email.subject_line}")
            print("-----------------------------")
            user_unread_again = input("Back to Inbox? (Y or N)").lower()
            if user_unread_again == "n":
                in_unread = False

    elif user_choice == 3:
        print("Thank you for visiting, You will be signed out")
        break
    else:
        print("Oops - incorrect input.")
