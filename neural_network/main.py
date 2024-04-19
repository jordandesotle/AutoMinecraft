import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress INFO level logs

from scripts.train import train_model
from scripts.evaluate import evaluate_model
from scripts.visualize_activations import visualize
from utils.hardware_check import hardware_check
from scripts.predict import live_demo, predict



def main():

    os.system("clear")
    device = hardware_check()

    name_length = len(device)
    dash_length = 50

    os.system("clear")
    if(name_length > dash_length-12):
        dash_length = name_length + 12

    side_len = ((dash_length - 12)-name_length)//2
    total_len = (side_len*2) + name_length + 12


    print(f"┌{'─'*(total_len-2)}┐")
    print(f"│{' '*side_len} Device: {device} {' '*side_len}│")
    print(f"└{'─'*(total_len-2)}┘")
    print("Minecraft Convolutional Neural Network:")
    print("Select an action:")
    print("1. Train Model")
    print("2. Evaluate Model")
    print("3. Visualize Activations")
    print("4. Predict")
    print("5. Live Demo")
    print("6. Exit")
    action = input("Enter the action number: ")

    os.system("clear")

    if action == '1':
        train_model()
    elif action == '2':
        evaluate_model()
    elif action == '3':
        visualize()
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
