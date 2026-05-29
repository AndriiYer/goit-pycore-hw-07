from birthday import Birthday
from name import Name
from phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old, new):
        for p in self.phones:
            if p.value == old:
                self.phones.remove(p)
                self.add_phone(new)
                return
        raise ValueError("Old phone not found.")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = str(self.birthday) if self.birthday else "No birthday"
        return f"{self.name.value}: {phones}. Birthday: {birthday}"