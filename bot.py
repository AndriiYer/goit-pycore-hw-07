from address_book import AddressBook
from record import Record


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            return f"Error: {e}"
    return wrapper


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message



@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.edit_phone(old_phone, new_phone)
    return "Phone updated."


@input_error
def show_phones(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    return "; ".join(p.value for p in record.phones)


def show_all(book):
    if not book.data:
        return "Address book is empty."
    return "\n".join(str(record) for record in book.data.values())

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    if not record.birthday:
        return "No birthday set."
    return str(record.birthday)

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays next week."
    return "\n".join(upcoming)

def parse_input(user_input):
    parts = user_input.split()
    return parts[0], parts[1:]
