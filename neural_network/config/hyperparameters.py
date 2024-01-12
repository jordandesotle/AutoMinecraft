# hyperparameters.py

class Hyperparameters:
    # Model Hyperparameters
    CONV1_FILTERS = 32
    CONV2_FILTERS = 64
    CONV3_FILTERS = 128
    DENSE_UNITS = 128

    # Training Hyperparameters
    BATCH_SIZE = 32
    NUM_EPOCHS = 10
    LEARNING_RATE = 0.001

    # Data Hyperparameters
    INPUT_SHAPE = (150, 150, 3)  # Adjust based on your image dimensions
    NUM_CLASSES = 1  # Change if you have more than two classes

    # Callbacks Hyperparameters
    MODEL_CHECKPOINT_PATH = 'model_weights.h5'
    EARLY_STOPPING_PATIENCE = 3

    # Visualization Hyperparameters
    VISUALIZATION_EXAMPLE_IMAGE_PATH = 'path/to/example_image.jpg'

if __name__ == "__main__":
    # Example usage
    # - Uncomment and modify the lines below based on your needs

    # # Example: Access hyperparameters
    # print(Hyperparameters.CONV1_FILTERS)
    # print(Hyperparameters.BATCH_SIZE)
