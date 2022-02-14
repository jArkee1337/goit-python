phone_book = {}
def input_error_decorator(func):
    def inner(*args, **kwargs):
        try:

            return func(*args, **kwargs)
        except KeyError:
            print("Your command isn't right please try again!")
        except IndexError:
            print("Please enter the name and phone number correctly")
        except TypeError:
            print("Please enter the name and phone")


    return inner


@input_error_decorator
def add_func(user_input):
    phone_book[user_input[1]] = user_input[2]


@input_error_decorator
def change_func(user_input):
    if user_input[1] in phone_book:
        phone_book[user_input[1]] = user_input[2]
    else:
        print(f"There is now such contact: {user_input[1]}, would you like to create it?")
        user_answer = input("Print yes or no: ").lower()
        if user_answer == "yes":
            add_func(user_input)
        elif user_answer == "no":
            return None


@input_error_decorator
def phone_func(user_input):
    print(phone_book[user_input[1]])


def show_all_func():
    for name, number in phone_book.items():
        print(name, number)


def exit_func():
    print("Good bye!")


def hello_func():
    print("How can I help you?")


exit_tuple = ("good bye", "close", "exit")
Commands = {
    "hello": hello_func,
    "add": add_func,
    "change": change_func,
    "phone": phone_func,
    "show all": show_all_func
}


@input_error_decorator
def get_handler(operator):
    return Commands[operator]


def main():

    while True:

        user_input = input("Enter the command: ").lower()

        if user_input in exit_tuple:
            exit_func()
            break
        elif user_input in Commands:
            get_handler(user_input)()
        else:
            user_input = user_input.split()
            handler = get_handler(user_input[0])
            if handler == None:
                continue
            else:
                handler(user_input)


if __name__ == "__main__":
    main()


