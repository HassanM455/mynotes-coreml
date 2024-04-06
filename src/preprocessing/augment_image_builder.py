
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageChops
import numpy as np
import random

class ConcreteBuilder:
    def __init__(self, image):
        self.image = image

    def change_background_color(self):
        """Change the white background of an image to a random color."""
        background_colors = ['gray', 'yellow', 'lightblue', 'pink', 'lightgreen']  # Example colors
        chosen_color = random.choice(background_colors)  # Choose a random color
        
        # Assuming white background, create an image with the new background color
        new_background = Image.new('RGB', self.image.size, chosen_color)
        diff = ImageChops.difference(self.image, ImageChops.invert(new_background))
        self.image = ImageChops.add(self.image, diff)

        return self
    
    def rotate_image(self, max_angle=25):
        angle = random.uniform(-max_angle, max_angle)
        self.image = self.image.rotate(angle, fillcolor=(255, 255, 255), expand=True)
        return self

    def add_noise(self, mean=0, std=1):
        np_image = np.array(self.image)
        noise = np.random.normal(mean, std, np_image.shape).astype(np.uint8)
        np_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
        self.image = Image.fromarray(np_image)
        return self

    def resize_image(self, base_width=150):
        w_percent = (base_width / float(self.image.size[0]))
        h_size = int((float(self.image.size[1]) * float(w_percent)))
        self.image = self.image.resize((base_width, h_size), Image.Resampling.LANCZOS)
        return self

    def flip_image_horizontal(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        return self

    def flip_image_vertical(self):
        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        return self

    def change_brightness(self, factor=1.5):
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)
        return self

    def change_contrast(self, factor=1.5):
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(factor)
        return self

    def apply_gaussian_blur(self, radius=2):
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius))
        return self

    def random_crop(self, crop_size=(100, 100)):
        max_x = self.image.width - crop_size[0]
        max_y = self.image.height - crop_size[1]
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        self.image = self.image.crop((x, y, x + crop_size[0], y + crop_size[1]))
        return self

    def add_color_jitter(self, factor=0.5):
        enhancer = ImageEnhance.Color(self.image)
        factor = random.uniform(1 - factor, 1 + factor)
        self.image = enhancer.enhance(factor)
        return self

    def sharpen_image(self, factor=2.0):
        enhancer = ImageEnhance.Sharpness(self.image)
        self.image = enhancer.enhance(factor)
        return self

    def edge_enhancement(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        return self

    def add_salt_and_pepper_noise(self, salt_vs_pepper=0.5, amount=0.004):
        np_image = np.array(self.image)
        num_salt = np.ceil(amount * np_image.size * salt_vs_pepper)
        num_pepper = np.ceil(amount * np_image.size * (1.0 - salt_vs_pepper))

        # Add Salt
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in np_image.shape]
        np_image[coords[0], coords[1]] = 1

        # Add Pepper
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in np_image.shape]
        np_image[coords[0], coords[1]] = 0

        self.image = Image.fromarray(np_image)
        return self

    def random_rotate_image(self, max_angle=180):
        angle = random.uniform(-max_angle, max_angle)
        self.image = self.image.rotate(angle, fillcolor=(255, 255, 255), expand=True)
        return self

    def get_result(self):
        """Returns the augmented image."""
        return self.image


