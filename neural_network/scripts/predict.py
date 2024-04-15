import os
import re
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from config.config import Config  # Import the Config class from config.py
from PIL import Image
import socket


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]



def live_demo():

	print("Loading model... one moment")
	model = tf.keras.models.load_model(Config.MODEL_OUTPUT_PATH)
	inputDir = Config.INPUT_PATH

	HOST = 'localhost'  # Server IP address
	PORT = 12345        # Server port
	global client_socket
	client_socket = None

	def initialize_client_socket():
		global client_socket
		if client_socket is None:
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client_socket.connect((HOST, PORT))
			print("Connected to server")


	def close_client_socket():
		global client_socket
		if client_socket:
			client_socket.close()
			print("Client socket closed")
			client_socket = None

	# Function to preprocess the input image
	def preprocess_image(image_path):
		img = tf.keras.preprocessing.image.load_img(image_path, target_size=Config.INPUT_SHAPE[:2])
		img_array = tf.keras.preprocessing.image.img_to_array(img)
		img_array = tf.expand_dims(img_array, 0)  # Create batch axis
		return img_array
	
	# Function to make predictions
	def make_prediction(image_path):
		input_data = preprocess_image(image_path)
		predictions = model.predict(input_data)
		predicted_class = np.argmax(predictions, axis=1)[0]
		return predicted_class

	def process_image():
		try:
			initialize_client_socket()

			# Receive and process messages continuously
			while True:
				data = client_socket.recv(1024)
				message = data.decode('utf-8').strip()
				if message:

					if message == 'You are connected':
						print("Received message from server:", message)
					else:
						if(os.path.exists(message)):
							print(f"Image taken: {message}")
							# preprocess_image(message)
							predicted_class = make_prediction(message)

							class_names = {
								0: "breaking_block",
								1: "mining_tree",
								2: "walking_in_desert",
								3: "walking_in_forest",
								4: "walking_in_plain",
								5: "walking_in_tundra"
							}

							predicted_class_name = class_names[predicted_class]
							print("Predicted class:", predicted_class_name)

						else:
							print(f"Message: {message}")


		except Exception as e:
			print("Error:", e)
			close_client_socket()

	def create_folder():
		if(os.path.exists(inputDir)):
			print(f"Deleting Folder: {inputDir}")
			os.rmdir(inputDir)

		print(f"Creating Folder: {inputDir}")
		os.makedir(inputDir)

		

	def main():
		# create_folder()
		try:
			process_image()
		finally:
			close_client_socket()

	
	main()













def predict():

	model = tf.keras.models.load_model(Config.MODEL_OUTPUT_PATH)

	def select_image():
		dir_path = Config.VAL_DATA_DIR
		print(dir_path)

		f = os.listdir(dir_path)
		f.sort()

		os.system("clear")
		print("———————————————————————————————————————————————")
		print("Select a folder:")
		for i, folder in enumerate(f, start=1):
			print(f"{i}: {folder}")

		choice = int(input("Enter a number: "))
		selection = f[choice-1]

		print(selection)

		new_dir = os.path.join(dir_path, selection)

		images = os.listdir(new_dir)
		images.sort(key=natural_sort_key)

		os.system("clear")
		print("———————————————————————————————————————————————")
		print("Select an Image to compute:")
		for i, image in enumerate(images, start=1):
			print(f"{i}: {image}")

		choice = int(input("Enter a number: "))
		selection = images[choice-1]

		print(selection)

		file_path = os.path.join(new_dir, selection)

		return file_path

	# Function to preprocess the input image
	def preprocess_image(image_path):
		img = tf.keras.preprocessing.image.load_img(image_path, target_size=Config.INPUT_SHAPE[:2])
		img_array = tf.keras.preprocessing.image.img_to_array(img)
		img_array = tf.expand_dims(img_array, 0)  # Create batch axis
		return img_array
	
	# Function to make predictions
	def make_prediction(image_path):
		input_data = preprocess_image(image_path)
		predictions = model.predict(input_data)
		predicted_class = np.argmax(predictions, axis=1)[0]
		return predicted_class

	def main():
		# Select an image and make prediction
		image_path = select_image()
		print(image_path)

		image = Image.open(image_path)
		image.show()

		predicted_class = make_prediction(image_path)

		class_names = {
			0: "breaking_block",
			1: "mining_tree",
			2: "walking_in_desert",
			3: "walking_in_forest",
			4: "walking_in_plain",
			5: "walking_in_tundra"
		}

		predicted_class_name = class_names[predicted_class]
		print("Predicted class:", predicted_class_name)
		input("Press ENTER to predict another image")
		image.close()
		main()

	main()

