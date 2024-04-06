import os
import gc

import argparse

from PIL import Image
from src.preprocessing.augment_client import AugmentClient
from src.preprocessing.augment_image_builder import ConcreteBuilder
from src.fs.data_directory_structure import DirectoryPaths


def augment_letter_images(
    letter: str, 
    src_letter_dir: str, 
    trgt_letter_dir: str
) -> None:

    for file_num, input_file in enumerate(os.listdir(src_letter_dir)):
        input_path = os.path.join(src_letter_dir, input_file)
        image = Image.open(input_path)
    
        builder = ConcreteBuilder(image)
        client.set_builder(builder)
        client.set_directors()
        client.execute_directors()
        results = client.get_results()
        image.save(os.path.join(trgt_letter_dir, f"{letter}__{file_num}__original__{input_file}"))
        
        for director_name, res in results:
            output_path = os.path.join(trgt_letter_dir, f"{letter}__{file_num}__{director_name}__{input_file}")
            res.save(output_path)
        
        del image
        del results
        gc.collect()




parser = argparse.ArgumentParser(description='Process a letter.')
parser.add_argument('--letter', type=str, required=True, help='The letter to process')
parser.add_argument('--case', type=str, required=True, help='Case is `upper` or `lower`')
args = parser.parse_args()


cropped_images = DirectoryPaths('cropped_images')
augmented_images = DirectoryPaths('augmented_images')


client = AugmentClient()

if args.case == 'lower':
    letters_and_data_dirs = zip(
        cropped_images.lower_alphabet, 
        cropped_images.lc_dirs,
        augmented_images.lc_dirs
    )

    for letter, c_letter_dir, a_letter_dir in letters_and_data_dirs:
        if letter != args.letter:
            continue

        augment_letter_images(letter, c_letter_dir, a_letter_dir)



if args.case == 'upper':
    letters_and_data_dirs = zip(
        cropped_images.upper_alphabet, 
        cropped_images.uc_dirs,
        augmented_images.uc_dirs
    )

    for letter, c_letter_dir, a_letter_dir in letters_and_data_dirs: 
        if letter != args.letter:
            continue
        
        augment_letter_images(letter, c_letter_dir, a_letter_dir)



