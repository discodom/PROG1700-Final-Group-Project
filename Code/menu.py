#Dominic Radley
#Final Project - PROG1700
#W0534133
#I am the only contributer to this file.

def show_menu():
    print("1. Manage Patients")
    print("2. Manage Doctors")
    print("3. Schedule Appointments")
    print("4. View Reports")
    print("5. Exit this application")


def patient_management():
    print("Waiting for this to be implemented")

def doctor_management():
    print("Waiting for this to be implemented")

def schedule_appointments():
    print("Waiting for this to be implemented")

def view_reports():
    print("Waiting for this to be implemented")


def user_choice():
    try:
        number = int(input("Enter your choice (1-5): ").strip())

        if number > 5:
            print("Please choose options 1 through 5.")
            return ""

        return str(number)

    except ValueError:
        print("Wrong input. Must be a number between 1 and 5.")
        return ""

    except (KeyboardInterrupt, EOFError):
        return "5"

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""


def run_menu():
    while True:
        show_menu()
        userchoice = user_choice()

        if userchoice == "1":
            patient_management()
        elif userchoice == "2":
            doctor_management()
        elif userchoice == "3":
            schedule_appointments()
        elif userchoice == "4":
            view_reports()
        elif userchoice == "5":
            print("Goodbye!")
            break
        elif userchoice != "":
            print("Invalid choice. Please select a valid option.")
