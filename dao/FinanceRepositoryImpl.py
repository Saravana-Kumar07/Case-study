import mysql.connector
from util.db_connection import get_connection
from util.dbproperty import get_connection_props
from exception.exceptions import UserNotFoundException, ExpenseNotFoundException

class FinanceRepositoryImpl:
    def __init__(self):
        props = get_connection_props("util/db.properties")
        self.conn = get_connection(props)
        self.cursor = self.conn.cursor()

    def create_user(self, user):
        query = "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)"
        values = (user.username, user.password, user.email)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("User created successfully!")

    def create_expense(self, expense):
        query = "INSERT INTO Expenses (user_id, amount, category_id, date, description) VALUES (%s, %s, %s, %s, %s)"
        values = (expense.user_id, expense.amount, expense.category_id, expense.date, expense.description)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Expense added successfully!")

    def delete_user(self, user_id):
        query = "DELETE FROM Users WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        if self.cursor.rowcount == 0:
            raise UserNotFoundException("User not found.")
        self.conn.commit()
        print("User deleted successfully!")

    def delete_expense(self, expense_id):
        query = "DELETE FROM Expenses WHERE expense_id = %s"
        self.cursor.execute(query, (expense_id,))
        if self.cursor.rowcount == 0:
            raise ExpenseNotFoundException("Expense not found.")
        self.conn.commit()
        print("Expense deleted successfully!")

    def get_all_expenses(self, user_id):
        query = "SELECT e.expense_id, e.amount, c.category_name, e.date, e.description " \
                "FROM Expenses e INNER JOIN ExpenseCategories c ON e.category_id = c.category_id " \
                "WHERE e.user_id = %s"
        self.cursor.execute(query, (user_id,))
        results = self.cursor.fetchall()
        if not results:
            raise ExpenseNotFoundException("No expenses found for the given user.")
        return results

    def update_expense(self, expense):
        query = "UPDATE Expenses SET amount = %s, category_id = %s, date = %s, description = %s " \
                "WHERE expense_id = %s"
        values = (expense.amount, expense.category_id, expense.date, expense.description, expense.expense_id)
        self.cursor.execute(query, values)
        if self.cursor.rowcount == 0:
            raise ExpenseNotFoundException("Expense not found.")
        self.conn.commit()
        print("Expense updated successfully!")

    def __del__(self):
        self.cursor.close()
        self.conn.close()
