from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.phone_number}"


class Record:

    def __init__(self, name):
        self.phones = []
        self.name = Name(name)

    def add_func(self, phone_number):
        self.phones.append(Phone(phone_number))

        return self.phones

    def change_func(self, phone_number, new_phone_number):

        for i in self.phones[:]:
            if str(i) == phone_number:
                self.phones.remove(i)
        self.phones.insert(0, Phone(new_phone_number))

    def remove_func(self, phone_number):
        for i in self.phones:
            if str(i) == phone_number:
                self.phones.remove(i)


class AddressBook(UserDict):

    def add_record(self, record_name_value, record):
        self.data[record_name_value] = record

    def remove_record(self, record_name_value):
        self.data.pop(record_name_value)
