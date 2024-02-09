
# from config.config import Config
import os

def get_num_classes():
	total_classes = 0

	# dir_path = Config.TRAIN_DATA_DIR

	# Count "walking" subdirectories
	walking_subdirs = os.listdir('data/train/walking')
	total_classes += len(walking_subdirs)

	# Count "mine_tree" subdirectories
	mine_tree_subdirs = os.listdir('data/train/mine_tree')
	total_classes += len(mine_tree_subdirs)

	# Count sets in each "walking" subdirectory
	for subdir in walking_subdirs:
		sets_path = os.path.join('data/train/walking', subdir)
		sets_count = len(os.listdir(sets_path))
		total_classes += sets_count

	# Count sets in each "mine_tree" subdirectory
	for subdir in mine_tree_subdirs:
		sets_path = os.path.join('data/train/mine_tree', subdir)
		sets_count = len(os.listdir(sets_path))
		total_classes += sets_count

	print("Total number of classes:", total_classes)
	return total_classes



if __name__ == '__main__':
	get_num_classes()