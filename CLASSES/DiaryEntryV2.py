#THIS IS THE SAME AS DiaryEntry.py, inalis lang yung example usage


from EncryptionClass import Encryption
from datetime import datetime
from abc import ABC, abstractmethod

# -------------------------
# Abstract DiaryEntry Class
# -------------------------
class DiaryEntry(ABC):
    def __init__(self, title, content, location, mood, entry_date=None):
        self.__title = title
        self.__content = content
        self.__entry_date = entry_date if entry_date else datetime.now()
        self.location = location
        self.mood = mood

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


    # -------------------------
# Subclass: MyEntry
# -------------------------
class MyEntry(DiaryEntry):
    def __init__(self, title, content, location, mood, encryption: Encryption, entry_date=None):
        super().__init__(title, content, location, mood, entry_date)
        # self.encrypted_content = encryption.encrypt(content)

    def get_decrypted_content(self, encryption: Encryption):
        return encryption.decrypt(self.encrypted_content)

    def update_content(self, new_content: str, encryption: Encryption):
        self.set_content(new_content)
        self.encrypted_content = encryption.encrypt(new_content)

    def display_entry(self):
        return (
            f"\033[1mTitle:\033[0m {self.get_title()}\n"
            f"\033[1mWritten on:\033[0m {self.get_entry_date()}\n"
            f"\033[1mLocation:\033[0m {self.location}\n"
            f"\033[1mMood:\033[0m {self.mood}\n"
            f"\033[1mDiary Content:\033[0m {self.get_content()}"
        )
    


# Example usage
first = MyEntry("First Entry", "Dear Diary, \n I'm so happy today because my grades are good.", location= "At Home", mood="Happy", encryption= 'kjnedjdw123')
second = MyEntry("Second Entry", "Dear Diary, \n The class is about to end and I'm excited for vacation even though it is only 2 weeks vecay.", location="At School", mood="Happy", encryption=None)
