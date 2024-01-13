# config.py
import os

class Config:

    # Neural Network Path
    ABS_PATH = '/home/jordan/Documents/AutoMinecraft_Root/neural_network/'

    # Model Configuration
    INPUT_SHAPE = (150, 150, 3)  # Adjust based on your image dimensions
    NUM_CLASSES = 1  # Change if you have more than two classes

    # Training Configuration
    BATCH_SIZE = 32
    NUM_EPOCHS = 10
    LEARNING_RATE = 0.001

    # Data Configuration
    # TRAIN_DATA_DIR = 'data/game_output/session'
    TRAIN_DATA_DIR = ABS_PATH + 'data/game_output/'
    VAL_DATA_DIR = ABS_PATH + 'data/game_output/'

    # Callbacks Configuration
    MODEL_CHECKPOINT_PATH = 'model_weights.h5'
    EARLY_STOPPING_PATIENCE = 3


    # Visualization Configuration
    VISUALIZATION_EXAMPLE_IMAGE_PATH = ABS_PATH + 'data/game_output/mine_tree/move_to_tree/set2/screenshot_10.png'

if __name__ == "__main__":
    # Example usage
    # - Uncomment and modify the lines below based on your needs


    # # Example: Access configuration parameters
    print(Config.INPUT_SHAPE)
    print(Config.BATCH_SIZE)
