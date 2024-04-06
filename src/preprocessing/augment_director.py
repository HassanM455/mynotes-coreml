

class DirectorAbstract:
    def __init__(self, builder):
        self._builder = builder

    def get_result(self):
        """Returns the augmented image."""
        return self._builder.get_result()


class DirectorGeneral(DirectorAbstract):


    def construct_basic_augmentation_pipeline(self):
        """Defines a basic augmentation pipeline."""
        self._builder.rotate_image(15)\
            .add_noise(mean=0, std=5)\
            .change_brightness(factor=1.1)

    def construct(self):
        """Defines an advanced and more complex augmentation pipeline."""
        self._builder.rotate_image(max_angle=10)\
            .add_noise(mean=0, std=2)\
            .change_contrast(factor=1.5)\
            .apply_gaussian_blur(radius=1)\
            .add_color_jitter(factor=0.3)\
            .sharpen_image(factor=2)\
            .edge_enhancement()\


class GeometricAugmentationDirector(DirectorAbstract):

    def construct(self):
        self._builder \
            .rotate_image(max_angle=20) \


class QualityAugmentationDirector(DirectorAbstract):

    def construct(self):
        self._builder \
            .apply_gaussian_blur(radius=2) \
            .add_noise(mean=0, std=3) \
            .change_contrast(factor=0.8)


class NoiseAugmentationDirector(DirectorAbstract):

    def construct(self):
        self._builder\
            .add_noise(mean=0, std=10)\
            .add_salt_and_pepper_noise(amount=0.02)


class AdvancedAugmentationDirector(DirectorAbstract):

    def construct(self):
        self._builder \
            .rotate_image(max_angle=4) \
            .add_noise(mean=0, std=5) \
            .apply_gaussian_blur(radius=1) \
            .add_color_jitter(factor=0.4)


class BasicAugmentationDirector(DirectorAbstract):

    def construct(self):
        self._builder\
            .rotate_image(max_angle=2)\
            .change_brightness(factor=1.1)


class BackgroundChangeDirector(DirectorAbstract):

    def construct(self):
        self._builder.change_background_color()\
            .rotate_image(max_angle=15)\
            .add_noise(mean=0, std=5)
