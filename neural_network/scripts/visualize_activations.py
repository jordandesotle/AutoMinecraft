# visualize_activations.py

import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing import image
from models.model_architecture import build_model
from config.config import Config

def visualize_activations(model_path="trained_model.h5", img_path=Config.VISUALIZATION_EXAMPLE_IMAGE_PATH, layer_name='conv2d_2'):
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

    # Plot the activations
    plot_activations(activations, layer_name)

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
    visualize_activations()

