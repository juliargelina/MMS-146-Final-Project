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


#-----------------------------------------------------

import os
import string
import random
from datetime import datetime
from abc import ABC, abstractmethod

# -------------------------
# Encryption Class
# -------------------------
class Encryption:
    def __init__(self, key: str):
        self.key = key
        self.alphabet = string.ascii_letters + string.digits + string.punctuation + " "
        self.cipher = self._make_cipher(key)
        self.reverse_cipher = {v: k for k, v in self.cipher.items()}

    def _make_cipher(self, password: str):
        chars = list(self.alphabet)
        random.seed(password)
        shuffled = chars.copy()
        random.shuffle(shuffled)
        return dict(zip(chars, shuffled))

    def encrypt(self, text: str) -> str:
        return "".join(self.cipher.get(c, c) for c in text)

    def decrypt(self, text: str) -> str:
        return "".join(self.reverse_cipher.get(c, c) for c in text)


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
        self.encrypted_content = encryption.encrypt(content)

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


# -------------------------
# User Class
# -------------------------
class User:
    def __init__(self, username: str, password: str, name: str):
        self.username = username
        self._password = password
        self.name = name

    def check_password(self, password: str):
        return self._password == password

    def change_password(self, old_pw: str, new_pw: str):
        if self._password == old_pw:
            self._password = new_pw
            print("Password changed successfully.")
            return True
        else:
            print("Wrong old password.")
            return False


# -------------------------
# DiarySystem Class
# -------------------------
class DiarySystem:
    USER_FILE = "users.txt"
    ENTRY_FILE = "entries.txt"

    def __init__(self, user: User):
        self.user = user
        self.encryption = Encryption(user._password)
        self.entries = self._load_entries()

    # ----------------- user handling -----------------
    @classmethod
    def login_or_register(cls):
        users = {}
        if os.path.exists(cls.USER_FILE):
            with open(cls.USER_FILE, "r") as f:
                for line in f:
                    u, p, n = line.strip().split(",")
                    users[u] = (p, n)

        username = input("Enter username: ")
        if username in users:
            password = input("Enter password: ")
            if users[username][0] == password:
                print("Login successful!")
                return User(username, password, users[username][1])
            else:
                print("Wrong password.")
                return None
        else:
            print("New user. Let's register!")
            password = input("Set a password: ")
            name = input("Enter your name: ")
            with open(cls.USER_FILE, "a") as f:
                f.write(f"{username},{password},{name}\n")
            print("Account created successfully. Please login again.")
            return None

    # ----------------- entry handling -----------------
    def _load_entries(self):
        entries = []
        if os.path.exists(self.ENTRY_FILE):
            with open(self.ENTRY_FILE, "r") as f:
                for line in f:
                    u, date, title, location, mood, encrypted = line.strip().split("||")
                    if u == self.user.username:
                        entry = MyEntry(title, "", location, mood, self.encryption, datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
                        entry.encrypted_content = encrypted
                        entries.append(entry)
        return entries

    def _save_entries(self):
        with open(self.ENTRY_FILE, "w") as f:
            for entry in self.entries:
                raw_date = datetime.strptime(entry.get_entry_date(), "%B %d, %Y %I:%M %p").strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{self.user.username}||{raw_date}||{entry.get_title()}||{entry.location}||{entry.mood}||{entry.encrypted_content}\n")

    def add_entry(self, title: str, content: str, location: str, mood: str):
        entry = MyEntry(title, content, location, mood, self.encryption)
        self.entries.append(entry)
        self._save_entries()
        print("Entry added.")

    def list_entries(self):
        if not self.entries:
            print("No entries yet.")
        for i, entry in enumerate(self.entries):
            print(f"{i}: {entry.get_title()} ({entry.get_entry_date()})")

    def view_entry(self, index: int):
        try:
            entry = self.entries[index]
            print(f"\nTitle: {entry.get_title()}")
            print(f"Date: {entry.get_entry_date()}")
            print(f"Location: {entry.location}")
            print(f"Mood: {entry.mood}")
            print("Content:", entry.get_decrypted_content(self.encryption))
        except IndexError:
            print("Invalid entry index.")

    def update_entry(self, index: int, new_content: str):
        try:
            self.entries[index].update_content(new_content, self.encryption)
            self._save_entries()
            print("Entry updated.")
        except IndexError:
            print("Invalid entry index.")

    def delete_entry(self, index: int):
        try:
            del self.entries[index]
            self._save_entries()
            print("Entry deleted.")
        except IndexError:
            print("Invalid entry index.")


# -------------------------
# CLI (User Journey)
# -------------------------
def main():
    print("Welcome to the Encrypted Diary System!")

    user = None
    while not user:
        user = DiarySystem.login_or_register()

    diary = DiarySystem(user)

    while True:
        print("\nMenu:")
        print("1. Add entry")
        print("2. List entries")
        print("3. View entry")
        print("4. Update entry")
        print("5. Delete entry")
        print("6. Change password")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Write your entry: ")
            location = input("Location: ")
            mood = input("Mood: ")
            diary.add_entry(title, content, location, mood)
        elif choice == "2":
            diary.list_entries()
        elif choice == "3":
            index = int(input("Enter entry index: "))
            diary.view_entry(index)
        elif choice == "4":
            index = int(input("Enter entry index: "))
            new_content = input("Enter new content: ")
            diary.update_entry(index, new_content)
        elif choice == "5":
            index = int(input("Enter entry index: "))
            diary.delete_entry(index)
        elif choice == "6":
            old_pw = input("Enter old password: ")
            new_pw = input("Enter new password: ")
            if user.change_password(old_pw, new_pw):
                diary.encryption = Encryption(new_pw)  # update encryption
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


main()
