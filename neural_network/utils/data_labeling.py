import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def label_data():
	ABS_PATH = '/home/jordan/Documents/AutoMinecraft_Root/neural_network/data/validation'
	folder_path = 'walking_in_tundra'
	path = os.path.join(ABS_PATH, folder_path)

	print("Absolute path:", path)

	subfolders = [os.path.join(path, f.name) for f in os.scandir(path) if f.is_dir()]

	# Sort subfolders numerically if they are numbered, otherwise sort alphabetically
	if all(f.name.isdigit() for f in os.scandir(path)):
	    subfolders = sorted(subfolders, key=lambda x: int(os.path.basename(x)))
	else:
	    subfolders.sort()

	index = 1
	print("\nSubfolders:")
	for i, subfolder in enumerate(subfolders, start=1):
		print(f"{i}. {subfolder}")

		# Renaming files in each subfolder
		file_list = [f for f in os.listdir(subfolder) if os.path.isfile(os.path.join(subfolder, f))]
		file_list.sort(key=natural_sort_key)


		for file in file_list:
			file_extension = os.path.splitext(file)[1]
			new_file_name = f"screenshot_{index}{file_extension}"

			old_file_path = os.path.join(subfolder, file)
			new_file_path = os.path.join(path, new_file_name)
			# os.rename(old_file_path, new_file_path)

			print(f"{index}: {file} {file_extension} -> {new_file_name}\n\t{old_file_path}\n\t{new_file_path}")

			index +=1

if __name__ == '__main__':
    label_data()