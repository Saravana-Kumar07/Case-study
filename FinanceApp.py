from dao.FinanceRepositoryImpl import FinanceRepositoryImpl
from entity.users import User
from entity.expense import Expense
from exception.exceptions import UserNotFoundException, ExpenseNotFoundException
from datetime import datetime

def display_menu():
    print("\n===== Finance Management System =====")
    print("1. Create User")
    print("2. Delete User")
    print("3. Add Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. View All Expenses")
    print("7. Exit")

def main():
    finance_repo = FinanceRepositoryImpl()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            user = User(username=username, password=password, email=email)
            finance_repo.create_user(user)

        elif choice == '2':
            try:
                user_id = int(input("Enter user ID to delete: "))
                finance_repo.delete_user(user_id)
            except UserNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                user_id = int(input("Enter user ID: "))
                amount = float(input("Enter expense amount: "))
                category_id = int(input("Enter category ID: "))
                date_str = input("Enter date (YYYY-MM-DD): ")
                description = input("Enter expense description: ")
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                expense = Expense(user_id=user_id, amount=amount, category_id=category_id, date=date, description=description)
                finance_repo.create_expense(expense)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                expense_id = int(input("Enter expense ID to update: "))
                amount = float(input("Enter new expense amount: "))
                category_id = int(input("Enter new category ID: "))
                date_str = input("Enter new date (YYYY-MM-DD): ")
                description = input("Enter new expense description: ")
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                expense = Expense(expense_id=expense_id, amount=amount, category_id=category_id, date=date, description=description)
                finance_repo.update_expense(expense)
            except ExpenseNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                expense_id = int(input("Enter expense ID to delete: "))
                finance_repo.delete_expense(expense_id)
            except ExpenseNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '6':
            try:
                user_id = int(input("Enter user ID: "))
                expenses = finance_repo.get_all_expenses(user_id)
                print("\n===== Expense List =====")
                print(f"{'ID':<5} {'Amount':<10} {'Category':<15} {'Date':<12} {'Description'}")
                for exp in expenses:
                    print(f"{exp[0]:<5} {exp[1]:<10} {exp[2]:<15} {exp[3]:<12} {exp[4]}")
            except ExpenseNotFoundException as e:
                print(f"Error: {e}")

        elif choice == '7':  # Exit
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()