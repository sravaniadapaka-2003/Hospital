def main():
    print(f"running expense tracker!")
 #get user input for expense.
    get_user_expense()
 #write their expense to a file
    save_expense_to_file()
 #read file and summarize expenses.
    summarize_expense
   

def get_user_expense():
    print(f"getting user expense")
   
def save_expense_to_file():
    print(f"getting user expense")
   
def summarize_expense():
    print(f"getting user expense")
  
import datetime

class Expense:
    """Represents a single hospital expense."""
    def __init__(self, date, description, amount):
        if not isinstance(date, datetime.date):
            raise TypeError("Date must be a datetime.date object.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Description cannot be empty.")

        self.date = date
        self.description = description
        self.amount = float(amount)

    def __str__(self):
        """String representation of an expense."""
        return f"Date: {self.date}, Description: {self.description}, Amount: ₹{self.amount:.2f}"

class HospitalExpenseTracker:
    """Manages a collection of hospital expenses."""
    def __init__(self):
        self.expenses = []

    def add_expense(self, date_str, description, amount_str):
        """Adds a new expense to the tracker."""
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            amount = float(amount_str)
            expense = Expense(date, description, amount)
            self.expenses.append(expense)
            print(f"Expense added successfully: {expense}")
        except ValueError as e:
            print(f"Error adding expense: {e}. Please ensure date is YYYY-MM-DD and amount is a number.")
        except TypeError as e:
            print(f"Error adding expense: {e}")

    def view_expenses(self):
        """Displays all recorded expenses."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("\n--- All Hospital Expenses ---")
        for i, expense in enumerate(self.expenses):
            print(f"{i+1}. {expense}")
        print("-----------------------------\n")

    def get_total_expenses(self):
        """Calculates and returns the total of all expenses."""
        total = sum(expense.amount for expense in self.expenses)
        return total

    def save_expenses_to_file(self, filename="hospital_expenses.txt"):
        """Saves current expenses to a text file."""
        try:
            with open(filename, "w") as f:
                for expense in self.expenses:
                    f.write(f"{expense.date},{expense.description},{expense.amount}\n")
            print(f"Expenses saved to {filename} successfully.")
        except IOError as e:
            print(f"Error saving expenses to file: {e}")

    def load_expenses_from_file(self, filename="hospital_expenses.txt"):
        """Loads expenses from a text file."""
        self.expenses = [] # Clear current expenses before loading
        try:
            with open(filename, "r") as f:
                for line in f:
                    try:
                        date_str, description, amount_str = line.strip().split(',')
                        self.add_expense(date_str, description, amount_str)
                    except ValueError as e:
                        print(f"Skipping malformed line in file: {line.strip()} - {e}")
            print(f"Expenses loaded from {filename} successfully.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with no previous expenses.")
        except IOError as e:
            print(f"Error loading expenses from file: {e}")

def main():
    """Main function to run the hospital expense tracker."""
    tracker = HospitalExpenseTracker()
    tracker.load_expenses_from_file() # Try to load existing expenses at startup

    while True:
        print("\n--- Hospital Expense Tracker Menu ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Save Expenses")
        print("5. Load Expenses (will overwrite current in memory)")
        print("6. Exit")
        print("-------------------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            date_str = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description of expense: ")
            amount_str = input("Enter amount: ")
            tracker.add_expense(date_str, description, amount_str)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            total = tracker.get_total_expenses()
            print(f"\nTotal Hospital Expenses: ₹{total:.2f}")
        elif choice == '4':
            tracker.save_expenses_to_file()
        elif choice == '5':
            tracker.load_expenses_from_file()
        elif choice == '6':
            print("Exiting Hospital Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()