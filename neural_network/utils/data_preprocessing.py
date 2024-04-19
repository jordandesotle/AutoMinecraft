# data_preprocessing.py

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from config.config import Config

def get_data_generators(batch_size, input_shape):
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

    val_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        Config.TRAIN_DATA_DIR,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='sparse', # sparse from categorical
        shuffle=True
    )

    val_generator = val_datagen.flow_from_directory(
        Config.VAL_DATA_DIR,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='sparse', # sparse from categorical
        shuffle=False  # Do not shuffle for validation
    )

    return train_generator, val_generator
