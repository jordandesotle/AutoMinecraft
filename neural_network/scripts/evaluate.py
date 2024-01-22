# evaluate.py

from tensorflow.keras.models import load_model
from utils.data_preprocessing import get_data_generators
from config.config import Config

def evaluate_model(model_path=Config.MODEL_OUTPUT_PATH):
    # Load the trained model
    model = load_model(model_path)

    # Set up the data generator for evaluation
    _, test_generator = get_data_generators(batch_size=Config.BATCH_SIZE, input_shape=Config.INPUT_SHAPE)

    # Evaluate the model on the test set
    evaluation_results = model.evaluate(test_generator, steps=test_generator.samples // Config.BATCH_SIZE)

    # Print evaluation results
    print("Test Loss:", evaluation_results[0])
    print("Test Accuracy:", evaluation_results[1])

if __name__ == "__main__":
    evaluate_model()
