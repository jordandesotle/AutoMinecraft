# main.py
#!venv/bin/python

from scripts.train import train_model
from scripts.evaluate import evaluate_model
from scripts.visualize_activations import select_image
from utils.hardware_check import hardware_check
from scripts.predict import live_demo, predict

import os

def main():

    os.system("clear")

    hardware_check()

    print("———————————————————————————————————————————————")
    print("Minecraft Convolutional Neural Network:")
    print("Select an action:")
    print("1. Train Model")
    print("2. Evaluate Model")
    print("3. Visualize Activations")
    print("4. Predict")
    print("5. Live Demo")
    print("6. Exit")

    action = input("Enter the action number: ")

    if action == '1':
        train_model()
    elif action == '2':
        evaluate_model()
    elif action == '3':
        select_image()
    elif action == '4':
        predict()
    elif action == '5':
        live_demo()
    elif action == '6':
        print("Exiting the script.")
    else:
        print("Invalid action. Please enter a valid action number.")

if __name__ == "__main__":
    main()
