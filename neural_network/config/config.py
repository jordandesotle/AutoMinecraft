# config.py
import os

from utils.get_num_classes import get_num_classes

class Config:

    # Model Configuration
    INPUT_SHAPE = (500, 917, 3)
    NUM_CLASSES = 6

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

    INPUT_PATH = ABS_PATH + 'data/input'

    # Model output files
    MODEL_CHECKPOINT_PATH = OUTPUT_DIR + 'model_weights.keras'
    MODEL_OUTPUT_PATH = OUTPUT_DIR + 'trained_model.keras'

    EARLY_STOPPING_PATIENCE = 3

if __name__ == "__main__":
    # Example usage
    # - Uncomment and modify the lines below based on your needs


    # # Example: Access configuration parameters
    print(Config.INPUT_SHAPE)
    print(Config.BATCH_SIZE)
