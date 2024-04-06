import os
from src.fs.data_directory_structure import DirectoryPaths
from PIL import Image



source_dir_paths = DirectoryPaths('images')
cropped_dir_paths = DirectoryPaths('cropped_images')

remove_pixels = 300

def crop_letters(
        input_dir_path_obj: DirectoryPaths,
        output_dir_path_obj: DirectoryPaths,
        letter_type: str
) -> None: 
    
    if letter_type == 'lower':
        input_dir = input_dir_path_obj.lc_dirs
        output_dir = output_dir_path_obj.lc_dirs
    elif letter_type == 'upper':
        input_dir = input_dir_path_obj.uc_dirs
        output_dir = output_dir_path_obj.uc_dirs
    else:
        raise Exception("Unknown letter case type with value {}".format(letter_type))

    for input_loc, output_loc in zip(input_dir, output_dir):

        for sf in os.listdir(input_loc):
            
            input_path = os.path.join(input_loc, sf)
            output_path = os.path.join(output_loc, sf)
            image = Image.open(input_path)
            crop_rectangle = (0, remove_pixels, image.width, image.height - remove_pixels - 40)
            cropped_image = image.crop(crop_rectangle)
            cropped_image.save(output_path)


if __name__ == '__main__':
    crop_letters(source_dir_paths, cropped_dir_paths, 'lower')
    crop_letters(source_dir_paths, cropped_dir_paths, 'upper')






