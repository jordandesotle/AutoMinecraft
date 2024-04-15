
# AutoMinecraft

## Project Description
This repo contains the source code the development of an AI controlled minecraft bot. The purpose of this project is to be able to capture the players screen while playing, process the image, and determine what the player is doing in the game.

The main components of this project are as follows:
- [Client Mod](https://github.com/jordandesotle/AutoMinecraft/tree/main/mod_dev)
- [Neural Network](https://github.com/jordandesotle/AutoMinecraft/tree/main/neural_network)


## Prerequisites

The following must be installed on your computer before installation:
- [Java 21](https://www.oracle.com/java/technologies/downloads/)
- IDE of your choice (IntelliJ is what I am using and can confirm works)
    - [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/download/?section=windows)
    - [Eclipse](https://www.eclipse.org/downloads/)
    - [Visual Studio](https://visualstudio.microsoft.com/downloads/)

## Installation

### General Installation

To install this project, run the following commands

First, choose a directory for your plugin source code
```bash
cd ~
```
Next, clone the repository into your folder of choice
```bash
git clone https://github.com/jordandesotle/AutoMinecraft.git
```
Now, you should be able to open your project with the IDE of your choice

The next step is to build the model using the training dataset. You may need to modify the config.py file to match the directory of your project.

After the model is trained, you can run the start-up script and run the live demo. You will have to have an instance of Minecraft running with the mod installed.

## Authors

- [@jordandesotle](https://www.github.com/jordandesotle)
