from collections import UserDict
import datetime
from record import Record


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.date.today()
        next_week = today + datetime.timedelta(days=7)

        result = []

        for record in self.data.values():
            if not record.birthday:
                continue

            bday = record.birthday.value.date()
            bday_this_year = bday.replace(year=today.year)

            if today <= bday_this_year <= next_week:
                result.append(f"{record.name.value}: {bday_this_year.strftime('%d.%m.%Y')}")

        return result