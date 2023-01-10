class Client:
    def __init__(self, id: int, name: str, age: int, ide: int, phone: int):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__ide = ide
        self.__phone = phone

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_ide(self, ide):
        self.__ide = ide

    def get_ide(self):
        return self.__ide

    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone


class Librarian:

    def __init__(self, id: int, name: str, age: int, ide: int, empType: str):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__ide = ide
        self.__empType = empType

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_ide(self, ide):
        self.__ide = ide

    def get_ide(self):
        return self.__ide

    def set_empType(self, empType):
        self.__empType = empType

    def get_empType(self):
        return self.__empType


class Book:

    def __init__(self, id: int, title: str, desc: str, author: str, status: str):
        self.__id = id
        self.__title = title
        self.__desc = desc
        self.__author = author
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_desc(self, desc):
        self.__desc = desc

    def get_desc(self):
        return self.__desc

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status


class Borrowing_order:
    def __init__(self, id: int, date: str, clientId: int, bookId: int, status: str):
        self.__id = id
        self.__date = date
        self.__clientId = clientId
        self.__bookId = bookId
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_clientId(self, clientId):
        self.__clientId = clientId

    def get_clientId(self):
        return self.__clientId

    def set_bookId(self, bookId):
        self.__bookId = bookId

    def get_bookId(self):
        return self.__bookId

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
