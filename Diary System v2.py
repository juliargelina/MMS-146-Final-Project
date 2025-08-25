from DiaryEntry import DiaryEntry

class DiarySystem:
    '''Represents the system of the diary, includes entries and encryption key'''
    
    def __init__(self, entries, encryption_key):
        '''Initializes the Diary System class

        Parameters:
        entries: The list of diary entries.
        encryption_key: The encryption keys used to encrypt the diary
        '''
        self.entries = entries
        self.encryption_key = encryption_key

    def load_entry(self):
        ''' Displays a diary entry '''
        return self.entries
        # entries = {}
        # entry_id = entries.keys()
        # entries.get({entries.values()})
        #need to get content for each entry
        
    def save_entry (self):
        ''' Save a diary entry'''
        

    def update_entry (self, updated_entry):
        ''' Update a diary entry'''
        self.entries = updated_entry
    
    def add_entry (self):
        ''' Add a diary entry'''
    
    def delete_entry (self):
        ''' Delete a diary entry'''

    def change_encryption_key (self):
        ''' Change the encryption key'''



#testing eme

ds1 = DiarySystem(entries= "Slay", encryption_key="fesdmklvdsjlg")

print("My entry: ", ds1.load_entry())

ds1.update_entry("Not groovy")

print("My entry: ", ds1.load_entry())