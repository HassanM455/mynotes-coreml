import os

# Base directory where 'upper' and 'lower' directories will be created
parent_directory = '/Users/hassanmahmood/repos/mynotes-coreml/data/augmented_images/letters'

# Directories for uppercase and lowercase letters
upper_dir = os.path.join(parent_directory, 'upper')
lower_dir = os.path.join(parent_directory, 'lower')

# Create 'upper' and 'lower' directories
os.makedirs(upper_dir, exist_ok=True)
os.makedirs(lower_dir, exist_ok=True)

# Alphabet arrays for uppercase and lowercase
upper_alphabet = [chr(i) for i in range(65, 91)]  # Uppercase A-Z
lower_alphabet = [chr(i) for i in range(97, 123)]  # Lowercase a-z

# Create directories within 'upper'
for letter in upper_alphabet:
    os.makedirs(os.path.join(upper_dir, letter), exist_ok=True)

# Create directories within 'lower'
for letter in lower_alphabet:
    os.makedirs(os.path.join(lower_dir, letter), exist_ok=True)

print("Created 'upper' and 'lower' directories with individual letter directories inside.")

