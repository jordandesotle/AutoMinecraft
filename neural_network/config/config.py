# config.py
import os

class Config:

    # Neural Network Path
    # Change this to match the location of the "neural_network" directory within your "AutoMinecraft" root folder
    ABS_PATH = '/home/jordan/Documents/AutoMinecraft_Root/neural_network/'

    # Model Configuration
    INPUT_SHAPE = (250, 459, 3)
    NUM_CLASSES = 6

    # Training Configuration
    BATCH_SIZE = 16
    NUM_EPOCHS = 10
    LEARNING_RATE = 0.001

    # Data paths
    TRAIN_DATA_DIR = ABS_PATH + 'data/train/'
    VAL_DATA_DIR = ABS_PATH + 'data/validation/'

    # Output directory
    OUTPUT_DIR = ABS_PATH + 'output/'

    INPUT_PATH = ABS_PATH + 'data/input'

    VISUALIZE_ACTIVATIONS_OUTPUT_PATH = ABS_PATH + 'visualizations/'
    VISUALIZE_LAYER = 'conv2d_2'

    # Model output files
    MODEL_CHECKPOINT_PATH = OUTPUT_DIR + 'model_weights.keras'
    MODEL_OUTPUT_PATH = OUTPUT_DIR + 'trained_model.keras'

    EARLY_STOPPING_PATIENCE = 3

if __name__ == "__main__":
    
    print(Config.INPUT_SHAPE)
    print(Config.BATCH_SIZE)
