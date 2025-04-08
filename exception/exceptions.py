class UserNotFoundException(Exception):
    def __init__(self, message="User not found in the system."):
        super().__init__(message)


class ExpenseNotFoundException(Exception):
    def __init__(self, message="Expense not found in the system."):
        super().__init__(message)


class InvalidInputException(Exception):
    def __init__(self, message="Invalid input provided."):
        super().__init__(message)


class DatabaseConnectionException(Exception):
    def __init__(self, message="Failed to establish a database connection."):
        super().__init__(message)
