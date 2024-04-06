from .augment_director import (
    DirectorGeneral, GeometricAugmentationDirector,
    QualityAugmentationDirector, NoiseAugmentationDirector,
    AdvancedAugmentationDirector, BasicAugmentationDirector,
    BackgroundChangeDirector
)


from .augment_image_builder import ConcreteBuilder



class AugmentClient:

    def __init__(self,):
        self._builder = None
        self._directors = []
        self._results = []

    def set_directors(self):
        if self._builder is None:
            raise Exception('Client must have a concrete builder')

        self._directors.append(DirectorGeneral(self._builder))
        self._directors.append(GeometricAugmentationDirector(self._builder))
        self._directors.append(QualityAugmentationDirector(self._builder))
        self._directors.append(NoiseAugmentationDirector(self._builder))
        self._directors.append(AdvancedAugmentationDirector(self._builder))
        self._directors.append(BasicAugmentationDirector(self._builder))
        self._directors.append(BackgroundChangeDirector(self._builder))

    def set_builder(self, builder: ConcreteBuilder):
        self._builder = builder

    def execute_directors(self):
        self._results = []

        for director in self._directors:
            director.construct()
            self._results.append((director.__class__.__name__, director.get_result()))

    def get_results(self):
        return self._results


















