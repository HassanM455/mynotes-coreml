
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

height = 256
width = 256
channels = 3

model = Sequential()
# First conv layer
model.add(Conv2D(1024, (5, 5), activation='relu', input_shape=(height, width, channels)))
model.add(MaxPooling2D(pool_size=(2, 2)))
# Second conv layer
model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# Third conv layer
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# Dropout layer
model.add(Dropout(0.5))
# Flatten layer
model.add(Flatten())
# Fully connected layers
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
# Output layer
model.add(Dense(47, activation='softmax'))# Output layer
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


upper_alphabet = [chr(i) for i in range(65, 91)]  # Uppercase A-Z
lower_alphabet = [chr(i) for i in range(97, 123)]  #

