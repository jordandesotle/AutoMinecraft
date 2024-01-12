# model_evaluation.py

from tensorflow.keras.models import load_model
from utils.data_preprocessing import get_data_generators

def evaluate_model(model_path="trained_model.h5"):
    # Define constants
    input_shape = (150, 150, 3)  # Adjust based on your image dimensions
    num_classes = 1  # Change if you have more than two classes
    batch_size = 32

    # Load the trained model
    model = load_model(model_path)

    # Set up the data generator for evaluation
    _, test_generator = get_data_generators(batch_size=batch_size, input_shape=input_shape)

    # Evaluate the model on the test set
    evaluation_results = model.evaluate(test_generator, steps=test_generator.samples // batch_size)

    # Print evaluation results
    print("Test Loss:", evaluation_results[0])
    print("Test Accuracy:", evaluation_results[1])

if __name__ == "__main__":
    evaluate_model()

