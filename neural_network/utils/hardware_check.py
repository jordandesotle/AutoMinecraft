import tensorflow as tf
from tensorflow.python.framework.config import set_memory_growth
import os
from config.config import Config

import numpy as np

def hardware_check():

	print(f"{'─'*50}")
	print("Please select an option:")
	print("1. Use GPU")
	print("2. Use CPU")

	action = input("Enter the option number: ")

	if action == '1':
		name = use_gpu()
	elif action == '2':
		name = use_cpu()
	else:
		print("Invalid action. Please enter a valid action number.")

	return name
	

def use_gpu():

	gpus = tf.config.list_physical_devices('GPU')

	print(f"{'─'*50}")
	print("Num GPUs Available: ", len(gpus))

	for i, gpu in enumerate(gpus, start=1):
		# print(f"GPU name: {gpu.name}")
		gpu_device = tf.config.experimental.get_device_details(gpu)
		gpu_name = gpu_device["device_name"]

		print(f'{i}: {gpu_name}')

	selected = int(input("Select a GPU to use: "))
	
	gpu = gpus[selected-1]

	gpu_device = tf.config.experimental.get_device_details(gpu)
	gpu_name = gpu_device["device_name"]

	print(f"Selected GPU: {gpu_name}")

	tf.config.experimental.set_memory_growth(gpu, True)


	# Set GPU usage
	gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.75)
	config = tf.compat.v1.ConfigProto(gpu_options=gpu_options)
	session = tf.compat.v1.Session(config=config)

	return gpu_name


def use_cpu():
	os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

	return "CPU"


if __name__ == "__main__":
	hardware_check()