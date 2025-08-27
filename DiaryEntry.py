from datetime import datetime

class DiaryEntry:
    def __init__(self, content, encrypted_content, entry_date):
        self.__content = content
        self.__encrypted_content = encrypted_content
        self.__entry_date = entry_date


    def get_content(self):
        self.__content

    def set_content(self, content):
        self.__content = content

    def get_entry_date(self):
        self.__entry_date

    def get_encrypted_content(self):
        self.__encrypted_content

#--------------------DIART ENTRIES WITH INHERITANCE AND POLYMORPHISM------------------------

from datetime import datetime
from abc import ABC, abstractmethod

# Base Class
class DiaryEntry(ABC):
    def __init__(self, title, content, entry_date=None):
        self.__title = title
        self.__content = content
        self.__entry_date = entry_date if entry_date else datetime.now()

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content

    def get_entry_date(self):
        return self.__entry_date

    @abstractmethod
    def display_entry(self):
        pass


# Subclass 1: First Entry (includes weather info)
class FirstEntry(DiaryEntry):
    def __init__(self, title, content, mood, entry_date=None):
        super().__init__(title, content, entry_date)
        self.mood = mood

    def display_entry(self):
        return (
            f"[GOOD GRADES]\n"
            f"Date: {self.get_entry_date()}\n"
            f"mood: {self.mood}\n"
            f"Content: {self.get_content()}"
        )


# Subclass 2: Second Entry (includes location info)
class SecondEntry(DiaryEntry):
    def __init__(self, title, content, location, entry_date=None):
        super().__init__(title, content, entry_date)
        self.location = location

    def display_entry(self):
        return (
            f"[VACATION]\n"
            f"Location: {self.location}\n"
            f"Written on: {self.get_entry_date()}\n"
            f"Content: {self.get_content()}"
        )


# Example usage
first = FirstEntry("First Entry", "Dear Diary, \n I'm so happy today because my grades are good.", mood="Happy")
second = SecondEntry("Second Entry", "Dear Diary, \n The class is about to end and I'm excited for vacation even though it is only 2 weeks vecay.", location="At School")

# Displaying entries
print(first.display_entry())
print("\n" + "-" * 50 + "\n")
print(second.display_entry())

