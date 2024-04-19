# model_architecture.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from config.config import Config
from config.hyperparameters import Hyperparameters

def build_model(input_shape=Config.INPUT_SHAPE, num_classes=Config.NUM_CLASSES):
    model = Sequential()

    # Convolutional layers
    model.add(Conv2D(Hyperparameters.CONV1_FILTERS, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(Hyperparameters.CONV2_FILTERS, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(Hyperparameters.CONV3_FILTERS, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    # Flatten layer to transition from convolutional to fully connected layers
    model.add(Flatten())

    # Fully connected layers
    model.add(Dense(Hyperparameters.DENSE_UNITS, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    return model

if __name__ == "__main__":
    
    # Print a summary of the model architecture
    model = build_model()
    model.summary()
