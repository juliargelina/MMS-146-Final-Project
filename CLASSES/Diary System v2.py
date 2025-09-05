from DiaryEntryV2 import DiaryEntry, MyEntry
from EncryptionClass import Encryption
import os
import random
import string


class DiarySystem:
    '''Represents the system of the diary, includes entries and encryption key'''
    
    USER_FILE = "users.txt"
    ENTRY_FILE = "entries.txt"


    def __init__(self, entries, encryption_key):
        '''Initializes the Diary System class

        Parameters:
        entries: The list of diary entries.
        encryption_key: The encryption keys used to encrypt the diary
        '''
        self.entries = entries
        self.encryption_key = None
    
    def _load_entries(self):                                            #reads files
        entries = []
        if os.path.exists(self.ENTRY_FILE):
            with open(self.ENTRY_FILE, "r") as f:                       
                for line in f:
                    u, date, encrypted = line.strip().split("||")
                    if u == self.user.username:
                        entry = DiaryEntry("", self.encryption)
                        entry.entry_date = date
                        entry.encrypted_content = encrypted
                        entries.append(entry)
        return entries

    # def list_entries(self):                                         #enumerates entries, print
    #     if not self.entries:
    #         print("No entries yet.")
    #     for i, entry in enumerate(self.entries):                   
    #         print(f"{i}: {entry.get_date()}")

    def load_entry(self, index: int):
        ''' Displays a diary entry '''
        try:
            entry = self.entries[index]                     #an entry is indexed from entries[]
            print(f"Date: {entry.get_date()}")
            print("Content:", entry.get_content(self.encryption))
        except IndexError:
            print("Invalid entry index.")

    def save_entry (self):
        ''' Save a diary entry'''
        with open(self.ENTRY_FILE, "w") as f:                       #writes files
            for entry in self.entries:
                f.write(f"{self.user.username}||{entry.get_date()}||{entry.encrypted_content}\n")

    def update_entry (self, index: int, new_content: str):
        ''' Update a diary entry'''
        try:
            self.entries[index].update_content(new_content, self.encryption)  #index an entry then update, encrypt, and save
            self._save_entries()
            print("Entry updated.")
        except IndexError:
            print("Invalid entry index.")
    
    def add_entry (self, content: str):
        ''' Add a diary entry'''
        entry = DiaryEntry(content, self.encryption)
        self.entries.append(entry)
        self._save_entries()
        print("Entry added.")
    
    def delete_entry (self, index: int):
        ''' Delete a diary entry'''
        try:
            del self.entries[index]                     #del an entry accessed thru index
            self._save_entries()                        #run save function
            print("Entry deleted.")
        except IndexError:
            print("Invalid entry index.")

    def change_encryption_key (self, chars, index, new_encryption_key):
        ''' Change the encryption key'''
    #not sure if this works needs testing
        chars = Encryption.alphabet 
        key = chars.copy()
        random.shuffle(key)
        for letter in DiaryEntry.get_content:
            index = chars.index(letter)
            new_encryption_key += chars[index]
        
        print(f"Previous Encryption Key: {DiaryEntry.get_content()}")
        print(f"New Encryption Key: {new_encryption_key}")
        



