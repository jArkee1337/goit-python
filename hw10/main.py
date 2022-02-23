from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    pass


class Record:
    name = Name("Vladimir")

    def __init__(self):
        self.phones = []

    def add_func(self, phone_number):
        self.phones.append(phone_number)
        return self.phones

    def change_func(self, phone_number, new_phone_number):
        if phone_number in self.phones:
            self.phones.remove(phone_number)
        self.phones.append(new_phone_number)

    def remove_func(self, phone_number):
        if phone_number in self.phones:
            self.phones.remove(phone_number)


class AddressBook(UserDict):

    def add_record(self, key, value):
        self.data[key] = value
