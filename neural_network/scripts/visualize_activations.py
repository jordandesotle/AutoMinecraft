# visualize_activations.py
import tensorflow as tf

import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing import image
from models.model_architecture import build_model
from config.config import Config

from os import walk
import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def visualize():

    def select_layer():
        print(f"{'─'*50}")
        print("Select a layer for visualization: ")
        print("1. Layer 1 (conv2d)")
        print("2. Layer 2 (conv2d_1)")
        print("3. Layer 3 (conv2d_2)")
        layer = input("Enter a number: ")

        if layer == '1':
            return "conv2d"
        elif layer == '2':
            return "conv2d_1"
        elif layer == '3':
            return "conv2d_2"
        else:
            print("Not a valid input")
            return None




    def visualize_activations(img_path, layer_name, num, model_path=Config.MODEL_OUTPUT_PATH):

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
        plot_activations(activations, layer_name, num)



    def plot_activations(activations, layer_name, figure_num, output_dir=Config.VISUALIZE_ACTIVATIONS_OUTPUT_PATH):
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

        output_file = f'{output_dir}activations_layer_{layer_name}_figure_{figure_num + 1}.png'

        # Save the figure to an image file
        plt.savefig(output_file)
        plt.close()

        print(f"Visualization saved as: {output_file}")
        input("Press ENTER to continue")


    def select_image():

        dir_path = Config.VAL_DATA_DIR
        print(dir_path)

        f = os.listdir(dir_path)
        f.sort()

        os.system("clear")
        print(f"{'─'*50}")
        print("Select a folder: ")
        for i, folder in enumerate(f, start=1):
            print(f"{i}: {folder}")

        choice = int(input("Enter a number: "))
        selection = f[choice-1]

        print(selection)

        new_dir = os.path.join(dir_path, selection)

        images = os.listdir(new_dir)
        images.sort(key=natural_sort_key)

        os.system("clear")
        print(f"{'─'*50}")
        print("Select an Image to compute: ")
        for i, image in enumerate(images, start=1):
            print(f"{i}: {image}")

        choice = int(input("Enter a number: "))
        selection = images[choice-1]

        print(selection)

        file_path = os.path.join(new_dir, selection)

        return file_path



    def main():
        num = 0
        os.system("clear")
        while True:

            image_path = select_image()
            if image_path is None:
                break
            layer = select_layer()
            if layer is None:
                break
            visualize_activations(image_path, layer, num)
            num += 1

            os.system('clear')
            print(f"{'─'*50}")
            print("1. Visualize Activation")
            print("2. Exit")
            action = input("Enter a number: ")

            if action == '2':
                break

    main()


if __name__ == "__main__":

    pass


    # visualize_activations()

