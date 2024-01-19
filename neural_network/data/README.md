# Data Directory Structure

The `data` directory is organized to store images related to in-game actions for training and validation of the Minecraft Convolutional Neural Network.

## Directory Hierarchy

- **game_output**: Contains raw images captured directly from the game, organized by specific actions.
  - **mine_tree**: Captures the process of mining a tree.
    - **align_with_tree**: Aligning with the tree before mining.
      - **set1**: Set of images capturing the alignment process.
        - frame1.jpg
        - frame2.jpg
        - ...
      - **set2**: Another set of images capturing the alignment process.
      - ...
    - **move_to_tree**: Moving to the tree before mining.
      - **set1**: Set of images capturing the movement process.
      - ...
    - **break_tree**: Capturing the actual process of breaking the tree.
      - **set1**: Set of images capturing the tree-breaking process.
      - ...
    - **success**: Images indicating the successful completion of the action.
      - **set1**: Set of images indicating success.
      - ...
    - ...

- **train**: Contains a cleaned set of images for training the neural network.
  - **mine_tree**: Contains images related to mining a tree.
    - **align_with_tree**: Images for aligning with the tree.
      - frame1.jpg
      - frame2.jpg
      - ...
    - **move_to_tree**: Images for moving to the tree.
    - ...

- **validation**: Contains a set of images reserved for model validation.
  - **mine_tree**: Contains validation images related to mining a tree.
    - **align_with_tree**: Validation images for aligning with the tree.
      - frame1.jpg
      - frame2.jpg
      - ...
    - **move_to_tree**: Validation images for moving to the tree.
    - ...
  - ...

