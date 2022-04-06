from collections import UserDict
from datetime import datetime
from datetime import timedelta


class Field:
    pass


class Name(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value.capitalize()


class Phone(Field):

    def __init__(self, phone_number):
        self.__phone_number = None
        self.phone_number = phone_number

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.checking_signs = ('-', '+', ' ')
        for i in phone_number:
            if i in self.checking_signs:
                phone_number_modifier = phone_number.replace(i, '')
        if len(phone_number_modifier) == 11:
            self.__phone_number = phone_number
        else:
            raise Exception("You input wrong number")

    def __str__(self):
        return f"{self.phone_number}"

class Birthday:

    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if birthday == None:
            self.__birthday = birthday
        elif 1900 <= birthday.year <= datetime.now().year:
            self.__birthday = birthday
        else:
            raise Exception("Wrong year")

class Record:

    def __init__(self, value, birthday=None):
        self.phones = []
        self.name = Name(value)
        self.birthday = Birthday(birthday)

    def __str__(self):
        self.phones_list = [str(i) for i in self.phones]
        result_phone = " ".join(self.phones_list)

        return f'Phones: {result_phone}, birthday: None'

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

    def days_to_birthday(self):

        if self.birthday.birthday == None:
            return 'You have not set the birthday for this contact'

        else:
            now_date = datetime.now()
            self.next_birthday = datetime(year=now_date.year, month=self.birthday.birthday.month,
                                          day=self.birthday.birthday.day)
            self.next_year_birthday = datetime(year=now_date.year + 1, month=self.birthday.birthday.month,
                                          day=self.birthday.birthday.day)

            if self.birthday.birthday.month > now_date.month:
                remaining_days = self.next_birthday - now_date
                return f' For next birthday remains {remaining_days.days} days'

            elif self.birthday.birthday.month == now_date.month and self.birthday.birthday.day >= now_date.day:
                remaining_days = self.next_birthday - now_date
                return f' For next birthday remains {remaining_days.days + 1} days'

            else:
                remaining_days = self.next_year_birthday - now_date
                return f' For next birthday remains {remaining_days.days} days'

class AddressBook(UserDict):

    def iterator(self, n=1):
        result = list(self.data.items())

        while result:
            yield result[:n]
            result = result[n:]

    def add_record(self, record_name_value, record):
        self.data[record_name_value] = record

    def remove_record(self, record_name_value):
        self.data.pop(record_name_value)


address = AddressBook()
dr = datetime(year=1999, month=2, day=3)
Vova = Record('vladimir1',dr )
Vova.add_func('8-913-177-73-83')
Vova.add_func('8-913-177-73-84')
Vova.add_func('8-913-177-73-85')
Kostya = Record('Kostya')
Kostya.add_func('8-913-177-73-83')
Kostya.add_func('8-913-177-73-84')
Kostya.add_func('8-913-177-73-85')
address.add_record(Vova.name.value, Vova)
address.add_record(Kostya.name.value, Kostya)
Igor = Record('Igor')
Igor.add_func('8-913-177-73-83')
Igor.add_func('8-913-177-73-84')
Igor.add_func('8-913-177-73-85')
address.add_record(Igor.name.value, Igor)
print(Vova.days_to_birthday())





