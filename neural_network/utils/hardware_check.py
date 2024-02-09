import tensorflow as tf
from tensorflow.python.framework.config import set_memory_growth
import os

import psutil
import GPUtil


def hardware_check():
	# Get the list of all visible devices
	# local_device_protos = tf.config.list_logical_devices()

	print("———————————————————————————————————————————————")
	print("Please select an option:")
	print("1. Use GPU")
	print("2. Use CPU")
	# print("3. Use Both")
	action = input("Enter the option number: ")

	if action == '1':
		use_gpu()
	elif action == '2':
		use_cpu()
	else:
		print("Invalid action. Please enter a valid action number.")



	# Print device information
	

def use_gpu():
	gpus = tf.config.list_physical_devices('GPU')

	print("———————————————————————————————————————————————")
	print("Num GPUs Available: ", len(gpus))

	for i, gpu in enumerate(gpus, start=1):
		# print(f"GPU name: {gpu.name}")
		gpu_device = tf.config.experimental.get_device_details(gpu)

		print(f'{i}: {gpu_device["device_name"]}')

	selected = int(input("Select a GPU to use: "))
	
	gpu = gpus[selected -1]
	gpu_details = tf.config.experimental.get_device_details(gpu)
	
	set_memory_growth(gpu, True)

	tf.config.experimental.set_virtual_device_configuration(
            gpu,
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2048 * 2)])


	print(tf.config.experimental.get_device_details(gpu)["device_name"])
	tf.config.experimental.set_visible_devices(gpu, 'GPU')

	print("———————————————————————————————————————————————")


def use_cpu():
	print("Using CPU")
	os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

def cpu_usage():

	# Print information about each device
	for device in local_device_protos:
		print(f"Device name: {device.name}, Device type: {device.device_type}")\

	# Print CPU usage before each action
	print(f"CPU Usage: {psutil.cpu_percent()}%")

def gpu_usage():
	try:
		gpus = GPUtil.getGPUs()
		print(f"GPU Usage: {gpus[0].load * 100}%")
	except Exception as e:
		print(f"Error getting GPU usage: {e}")


if __name__ == "__main__":
	hardware_check()