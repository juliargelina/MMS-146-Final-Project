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

    def load_entry(self, entries):
        ''' Displays a diary entry '''
        # entries = {
        #     'Entry no.': int(),
        #     'Date': DiaryEntry.get_entry_date,
        #     'My Entry': DiaryEntry.get_content
        # }

        # for key, value in entries.items():
        #     print(f'{key}: {value}')
        # #prints all keys for every value
        # #find a way to use get() pag isa-isa

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

# ds1 = DiarySystem(entries= "Slay", encryption_key="fesdmklvdsjlg")


