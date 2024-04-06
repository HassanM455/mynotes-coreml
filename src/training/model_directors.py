
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout




class AbsCNNModelDirector:
    def __init__(self, height, width, channels, num_of_outputs):
        self.height = height
        self.width = width
        self.channels = channels
        self.num_of_outputs = num_of_outputs
        self._model = None

    def set_model(self, model):
        self._model = model


    def construct(self):
        pass

    def get_result(self):
        return self._model


class SimpleCNNModelDirector(AbsCNNModelDirector):

    def construct(self):
        if self._model is None:
            raise Exception("Need to set the `model` attribute using the `set_model` setter.")

        model = self._model 
        input_shape = (self.height, self.width, self.channels)

        model\
            .add(Conv2D(3, (5,5), activation=None, input_shape=input_shape))\
            .add(MaxPooling2D(pool_size=(2,2)))\
            .add(Flatten())\
            .add(Dense(5))\
            .add(Dense(self.num_of_outputs))\
            .compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        self._model = model


class ComplexCNNModelDirector(AbsCNNModelDirector):


    def construct(self):

        if self._model is None:
            raise Exception("Need to set the `model` attribute using the `set_model` setter.")

        model = self._model 
        input_shape = (self.height, self.width, self.channels)

        # First conv layer
        model\
            .add(Conv2D(1024, (5, 5), activation='relu', input_shape=input_shape))\
            .add(MaxPooling2D(pool_size=(2, 2)))\
            .add(Conv2D(512, (3, 3), activation='relu'))\
            .add(MaxPooling2D(pool_size=(2, 2)))\
            .add(Conv2D(256, (3, 3), activation='relu'))\
            .add(MaxPooling2D(pool_size=(2, 2)))\
            .add(Dropout(0.5))\
            .add(Flatten())\
            .add(Dense(256, activation='relu'))\
            .add(Dense(128, activation='relu'))\
            .add(Dense(47, activation='softmax'))\
            .add(Dense(self.num_of_outputs, activation='sigmoid'))\
            .compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        self._model = model


