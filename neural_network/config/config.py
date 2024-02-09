# config.py
import os

from utils.get_num_classes import get_num_classes

class Config:

    # Model Configuration
    INPUT_SHAPE = (500, 917, 3)  # Adjust based on your image dimensions
    NUM_CLASSES = 1  # Change if you have more than two classes
    # NUM_CLASSES = get_num_classes()

    # Training Configuration
    BATCH_SIZE = 16
    NUM_EPOCHS = 10
    LEARNING_RATE = 0.001


    # Neural Network Path
    ABS_PATH = '/home/jordan/Documents/AutoMinecraft_Root/neural_network/'

    # Data paths
    TRAIN_DATA_DIR = ABS_PATH + 'data/train/'
    VAL_DATA_DIR = ABS_PATH + 'data/validation/'

    # Output directory
    OUTPUT_DIR = ABS_PATH + "output/"

    # Model output files
    MODEL_CHECKPOINT_PATH = OUTPUT_DIR + 'model_weights.h5'
    MODEL_OUTPUT_PATH = OUTPUT_DIR + 'trained_model.h5'

    EARLY_STOPPING_PATIENCE = 3

    # Visualization Configuration
    VISUALIZATION_EXAMPLE_IMAGE_PATH = ABS_PATH + 'data/train/mine_tree/move_to_tree/set2/screenshot_10.png'

if __name__ == "__main__":
    # Example usage
    # - Uncomment and modify the lines below based on your needs


    # # Example: Access configuration parameters
    print(Config.INPUT_SHAPE)
    print(Config.BATCH_SIZE)
