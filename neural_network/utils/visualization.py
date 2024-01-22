# visualization.py

import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from models.model_architecture import build_model
from utils.data_preprocessing import get_data_generators

def plot_training_history(history):
    # Plot training and validation accuracy
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    # Plot training and validation loss
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

def visualize_activations(model_path="trained_model.h5", img_path="path/to/example_image.jpg"):
    # Load the trained model
    model = load_model(model_path)

    # Load an example image
    img = image.load_img(img_path, target_size=(1834, 1000))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Get activations for a specific layer
    layer_name = 'conv2d_2'  # Adjust based on your model architecture
    intermediate_layer_model = build_intermediate_model(model, layer_name)
    activations = intermediate_layer_model.predict(img_array)

    # Plot the activations
    plot_activations(activations, layer_name)

def build_intermediate_model(model, layer_name):
    # Build a model that outputs the activations of the specified layer
    intermediate_layer_model = Model(inputs=model.input, outputs=model.get_layer(layer_name).output)
    return intermediate_layer_model

def plot_activations(activations, layer_name):
    # Plot the activations
    plt.figure(figsize=(8, 8))
    for i in range(activations.shape[-1]):
        plt.subplot(8, 8, i + 1)
        plt.imshow(activations[0, :, :, i], cmap='viridis')
        plt.axis('off')
    plt.suptitle(f'Activations of Layer: {layer_name}')
    plt.show()

if __name__ == "__main__":
    # Example usage
    # - Uncomment and modify the lines below based on your needs

    # # Example 1: Visualize training history
    # history = ...  # Load the training history from the training script
    # plot_training_history(history)

    # # Example 2: Visualize activations
    # visualize_activations(model_path="trained_model.h5", img_path="path/to/example_image.jpg")
