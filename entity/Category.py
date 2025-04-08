class Category:
    def __init__(self, category_id=0, category_name=""):
        self.__category_id = category_id
        self.__category_name = category_name

    @property
    def category_id(self):
        return self.__category_id

    @property
    def category_name(self):
        return self.__category_name

    @category_id.setter
    def category_id(self, category_id):
        self.__category_id = category_id

    @category_name.setter
    def category_name(self, category_name):
        self.__category_name = category_name

    def __str__(self):
        return f"Category [ID: {self.__category_id}, Name: {self.__category_name}]"
