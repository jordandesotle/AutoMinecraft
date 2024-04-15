# Neural Network Directory

The `neural_network` directory contains scripts, models, and data for developing and training the Minecraft Convolutional Neural Network.

## Directory Structure

- **config**: Contains configuration files for the neural network.
  - `config.py`: Configuration parameters for the model, training, and data.
  - `hyperparameters.py`: Hyperparameters for the training the model

- **data**: Directory for organizing training and validation data. See `data/README.md` for more details on the structure of the data.

- **models**: Directory for storing the neural network model architecture.
  - `model_architecture.py`: Script defining the architecture of the neural network.

- **scripts**: Contains Python scripts for different actions related to the neural network.
  - `train.py`: Script for training the neural network.
  - `predict.py`: Script to make predictions with a trained model.
  - `evaluate.py`: Script for evaluating the performance of the trained model.
  - `visualize_activations.py`: Script for visualizing activations in the neural network.

- **utils**: Utility scripts for data preprocessing and other functions.
  - `data_preprocessing.py`: Script for generating data generators.
  - `data_labeling.py`: Utility script to rename files in a directory and combine them. Used when remodeling the structure of the training and validation data
  - `hardware_check.py`: Experimental script to enable GPU exceleration

- `venv`: Virtual environment for managing Python dependencies.

- `main.py`: Main script to interact with the neural network (train, evaluate, visualize, predict).

- `README.md`: Documentation providing an overview of the neural network directory structure and usage.

- `requirements.txt`: File specifying Python dependencies required for the project.

- `.gitignore`: File specifying patterns to be ignored by version control.

- ...

