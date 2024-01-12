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
        class_mode='binary',  # 'categorical' if you have more than two classes
        shuffle=True
    )

    val_generator = val_datagen.flow_from_directory(
        Config.VAL_DATA_DIR,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='binary',  # 'categorical' if you have more than two classes
        shuffle=False  # Do not shuffle for validation
    )

    return train_generator, val_generator

if __name__ == "__main__":
    # Example usage
    # - Uncomment and modify the lines below based on your needs

    # # Example: Get data generators
    batch_size = 32
    input_shape = (150, 150, 3)  # Adjust based on your image dimensions
    train_generator, val_generator = get_data_generators(batch_size, input_shape)

    # # Example: Visualize a batch of augmented images
    import matplotlib.pyplot as plt
    images, labels = train_generator.next()
    for i in range(len(images)):
        plt.imshow(images[i])
        plt.title(f"Label: {labels[i]}")
        plt.show()
