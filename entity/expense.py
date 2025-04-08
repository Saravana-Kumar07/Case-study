class Expense:
    def __init__(self, expense_id=0, user_id=0, amount=0.0, category_id=0, date=None, description=""):
        self.__expense_id = expense_id
        self.__user_id = user_id
        self.__amount = amount
        self.__category_id = category_id
        self.__date = date
        self.__description = description

    @property
    def expense_id(self):
        return self.__expense_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def amount(self):
        return self.__amount

    @property
    def category_id(self):
        return self.__category_id

    @property
    def date(self):
        return self.__date

    @property
    def description(self):
        return self.__description

    @expense_id.setter
    def expense_id(self, expense_id):
        self.__expense_id = expense_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @category_id.setter
    def category_id(self, category_id):
        self.__category_id = category_id

    @date.setter
    def date(self, date):
        self.__date = date

    @description.setter
    def description(self, description):
        self.__description = description

    def __str__(self):
        return (f"Expense [ID: {self.__expense_id}, User ID: {self.__user_id}, Amount: {self.__amount}, "
                f"Category ID: {self.__category_id}, Date: {self.__date}, Description: {self.__description}]")
