# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth):
        """
        Constructor method, creates a person object
        """
        if not isinstance(name, str):
            raise TypeError("name is not a string")
        if name == "":
            raise ValueError("name is an empty string")
        if not isinstance(birth, (date)):
            raise TypeError("birth is not of type date")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """
        translates the persons name into initials
        """
        newinitials = ""

        new_name = (self.name).strip().split()

        for i in range(0, len(new_name)):
            newinitials = newinitials + new_name[i][0]

        return newinitials.upper()

    def is_birthday(self):
        """
        checks if the date is the same as the person's birthday
        """

        current_date = date.today()

        if current_date.day == self.birth.day and current_date.month == self.birth.month:
            return True
        else:
            return False

myPerson = Person("josephine ofelia montgomery", date(1973, 10, 28))

print(myPerson.initials())
print(myPerson.is_birthday())
