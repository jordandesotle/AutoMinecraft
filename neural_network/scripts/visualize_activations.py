# visualize_activations.py

import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing import image
from models.model_architecture import build_model
from config.config import Config

from os import walk
import os

def visualize_activations(img_path, model_path=Config.MODEL_OUTPUT_PATH, layer_name='conv2d_2'):
    # Load the trained model
    model = load_model(model_path)

    # Load an example image
    img = image.load_img(img_path, target_size=Config.INPUT_SHAPE[:2])
    img_array = image.img_to_array(img)
    img_array = img_array.reshape((1,) + img_array.shape)  # Add batch dimension
    img_array /= 255.0

    # Get activations for the specified layer
    intermediate_layer_model = Model(inputs=model.input, outputs=model.get_layer(layer_name).output)
    activations = intermediate_layer_model.predict(img_array)

    # Plot the an                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            /ctivations
    plot_activations(activations, layer_name, figure_num=0)



def plot_activations(activations, layer_name, figure_num):
    num_channels = activations.shape[-1]
    num_rows = 8
    num_cols = min(num_channels, 8)  # Set the maximum number of columns to 8 for better visualization

    # Create a figure
    plt.figure(figsize=(8, 8))

    for i in range(num_rows * num_cols):
        channel_index = figure_num * num_rows * num_cols + i
        if channel_index < num_channels:
            plt.subplot(num_rows, num_cols, i + 1)
            plt.imshow(activations[0, :, :, channel_index], cmap='viridis')
            plt.axis('off')

    plt.suptitle(f'Activations of Layer: {layer_name} (Figure {figure_num + 1})')

    # Save the figure to an image file
    plt.savefig(f'activations_layer_{layer_name}_figure_{figure_num + 1}.png')
    plt.close()


def select_image():

    dir_path = Config.VAL_DATA_DIR
    # dir_path = os.path.dirname(os.path.realpath(__file__))  # current path
    print(dir_path)

    file_not_chosen = True

    new_dir = dir_path
    while(file_not_chosen):
        f = os.listdir(new_dir)
        # print(f)
        count = 0

        for file in f:
            count += 1
            print(f"{count}: {file}")

        choice = int(input("Please enter a number: "))
        name = f[choice-1]
        # print(f"{dir_path}{name}")
        if(os.path.isfile(f"{new_dir}{name}")):
            file_not_chosen = False
            filename = f"{new_dir}{name}"
        else:
            new_dir = f"{new_dir}{name}/"
    
    print(filename)

    visualize_activations(filename)

# def plot_activations(activations, layer_name):
#     # Plot the activations
#     plt.figure(figsize=(8, 8))
#     for i in range(activations.shape[-1]):
#         plt.subplot(8, 8, i + 1)
#         plt.imshow(activations[0, :, :, i], cmap='viridis')
#         plt.axis('off')
#     plt.suptitle(f'Activations of Layer: {layer_name}')
#     plt.show()

if __name__ == "__main__":

    pass


    # visualize_activations()

