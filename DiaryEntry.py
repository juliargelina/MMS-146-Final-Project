from datetime import datetime
from abc import ABC, abstractmethod

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
        return self.__entry_date.strftime("%B %d, %Y %I:%M %p")

    @abstractmethod
    def display_entry(self):
        pass


# Subclass: My Entries
class MyEntry(DiaryEntry):
    def __init__(self, title, content, location, mood, entry_date=None):
        super().__init__(title, content, entry_date)
        self.mood = mood
        self.location = location

    def display_entry(self):
        return (
            f"\033[1mTitle:\033[0m {self.get_title()}\n"
            f"\033[1mWritten on:\033[0m {self.get_entry_date()}\n"
            f"\033[1mLocation:\033[0m {self.location}\n"
            f"\033[1mMood:\033[0m {self.mood}\n"
            f"\033[1mDiary Content:\033[0m {self.get_content()}"
        )



# Example usage
first = MyEntry("First Entry", "Dear Diary, \n I'm so happy today because my grades are good.", location= "At Home", mood="Happy")
second = MyEntry("Second Entry", "Dear Diary, \n The class is about to end and I'm excited for vacation even though it is only 2 weeks vecay.", location="At School", mood="Happy")

# Displaying entries
print(first.display_entry())
print("\n" + "-" * 50 + "\n")
print(second.display_entry())

