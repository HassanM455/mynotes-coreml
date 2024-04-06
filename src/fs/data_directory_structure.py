import os

class DirectoryPaths:

    project_dir = '/Users/hassanmahmood/repos/mynotes-coreml/data'
    lower_letters_dir = 'letters/lower'
    upper_letters_dir = 'letters/upper'
    upper_alphabet = [chr(i) for i in range(65, 91)]  # Uppercase A-Z
    lower_alphabet = [chr(i) for i in range(97, 123)]  #
    
    def __init__(self, main_dir):
        self.main_dir = os.path.join(self.project_dir, main_dir)
        
        self.main_lc_dir = os.path.join(self.main_dir, self.lower_letters_dir)
        self.main_uc_dir = os.path.join(self.main_dir, self.upper_letters_dir)
        
        self.lc_dirs = [os.path.join(self.main_lc_dir, letter) for letter in self.lower_alphabet]
        self.uc_dirs = [os.path.join(self.main_uc_dir, letter) for letter in self.upper_alphabet]

