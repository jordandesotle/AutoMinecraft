# Data Directory Structure

The `data` directory is organized to store images related to in-game actions for training and validation of the Minecraft Convolutional Neural Network.

## Directory Hierarchy

- **train**: Contains raw images captured directly from the game, organized by specific actions.
  - **breaking_block**: Folder that stores training images of the player breaking blocks
  - **mining_tree**: Folder that stores training images of the player mining_trees
  - **walking_in_desert**: Folder that stores training images of the player walking in the desert
  - **walking_in_forest**: Folder that stores training images of the player walking in the forest
  - **walking_in_plain**: Folder that stores training images of the player walking in a plain
  - **walking_in_tundra**: Folder that stores training images of the player walking in a tundra


- **validation**: Contains a set of images reserved for model validation.
  - **breaking_block**: Folder that stores validation images of the player breaking blocks
  - **mining_tree**: Folder that stores validation images of the player mining_trees
  - **walking_in_desert**: Folder that stores validation images of the player walking in the desert
  - **walking_in_forest**: Folder that stores validation images of the player walking in the forest
  - **walking_in_plain**: Folder that stores validation images of the player walking in a plain
  - **walking_in_tundra**: Folder that stores validation images of the player walking in a tundra
