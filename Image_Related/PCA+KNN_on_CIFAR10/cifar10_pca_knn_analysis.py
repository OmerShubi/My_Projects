import pickle
import math
import numpy as np
from PIL import Image
import datetime


def unpickle(file):
	with open(file, 'rb') as fo:
		data = pickle.load(fo, encoding='bytes')
	return data


def merge_and_extract(file_prefix, batches, test=False):
	"""
	Merges 'batches' number of given batches from the cifar-10 data set,
	extracts and returns the images as an array 'ready_images' of flat gray scale images
	and the labels 'set_labels'.

	"""
	print("extracting data and merging batches...")
	set_labels = []
	set_images = []

	for batch in range(1, batches + 1):
		if test:
			file = file_prefix
		else:
			file = file_prefix + str(batch)
		my_dict = unpickle(file)
		set_labels.extend(my_dict[b'labels'])
		set_images.extend(my_dict[b'data'])

	ready_images = np.zeros((np.ma.size(set_images, 0), 1024))
	for i in range(len(set_images)):
		ready_images[i] = turn_image_to_flat_gray_scale(set_images[i])
	return ready_images, set_labels


def turn_image_to_flat_gray_scale(color_image):
	"""
	Converts a 'color_image' to a flat (1 by 1024) gray scale array 'flat_array' which is returned.
	"""
	single_img = np.array(color_image)
	single_img_reshaped = np.transpose(np.reshape(single_img, (3, 32, 32)), (1, 2, 0))
	image = Image.fromarray(single_img_reshaped.astype('uint8'))
	image = image.convert("L")
	my_array = np.array(image)
	flat_array = my_array.reshape((1, 1024))
	return flat_array


def euclidean_distance(instance1, instance2, length):
	""" Function to find the euclidean distance between two vectors """
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


def k_nearest_neighbors(training_set, test_instance, training_labels, k):
	"""
	kNN algorithm. Returns proposed label of a given test image 'test_instance', by finding the
	'k' similar neighbors (euclidean distance) for 'training_set' set of images.
	"""
	closest_neighbors_labels = []
	distances = []
	length = len(test_instance)-1
	for x in range(np.ma.size(training_set, 1)):
		dist = euclidean_distance(training_set[:, x].tolist(), test_instance, length)
		distances.append(dist)

	distances = np.array(distances, dtype=float)

	for neighbor in range(k):
		closest_neighbor = np.argmin(distances)
		closest_neighbors_labels.append(training_labels[closest_neighbor])
		distances[closest_neighbor] = distances.max()

	return closest_neighbors_labels


def best_neighbor_match_check(k_neighbors_labels):
	"""	Returns the value with the most repetitions in `k_neighbors`. """
	k_neighbors_labels.sort()
	longest_repeats = current_repeats = 0
	current_value = best_match_value = k_neighbors_labels[0]
	for value in k_neighbors_labels:
		if value == current_value:
			current_repeats += 1
		else:
			current_repeats = 1
			current_value = value
		if longest_repeats < current_repeats:
			longest_repeats = current_repeats
			best_match_value = current_value

	return best_match_value


def test_run(training_matrix, test_matrix, training_labels, test_labels, k_list, s=0):
	"""
	Applies kNN algorithm to 'training_matrix' and to each image in 'test_matrix'.
	Checks label match accuracy according to 'training_labels' and 'test_labels'.
	Sends to 'k_nearest_neighbors' function the highest k value.
	Then iterates on each k from 'k_list' closest neighbors, and finds the best match by calling
	'best_neighbor_match_check' function, instead of the full kNN!.
	"""
	nearest_list = []
	for img in range(np.ma.size(test_matrix, 1)):
		nearest_list.append(k_nearest_neighbors(training_matrix, test_matrix[:, img].tolist(), training_labels, max(k_list)))

	for k in k_list:
		count = 0
		for img in range(np.ma.size(test_matrix, 1)):
			nearest_one = best_neighbor_match_check(nearest_list[img][:k])
			if nearest_one != test_labels[img]:
				count += 1
		error_rate = count / np.ma.size(test_matrix, 1)
		if s == 0:
			print("For s =", s, " and k = ", k, " the error rate is: ", error_rate)
		else:
			print("For k = ", k, " the error rate is: ", error_rate)


def pca(matrix):
	"""
	Performs SVD and returns the left eigenvectors.
	All values are returned and then sliced according to given 's' before applying kNN algorithm.
	"""
	print("Applying PCA...")
	u, singular_values, v = np.linalg.svd(matrix.T, full_matrices=False)
	return u


def main():
	"""
	Program to identify class (label) of test images, given a training set of images
	utilizing Principal Component Analysis (PCA) and k nearest neighbors algorithm (kNN).
	"""
	training_set = "./cifar-10-python/cifar-10-batches-py/data_batch_"
	training_images, training_labels = merge_and_extract(training_set, 5, False)
	test_set = "./cifar-10-python/cifar-10-batches-py/test_batch"
	test_images, test_labels = merge_and_extract(test_set, 1, True)

	pca_result = np.array(pca(training_images))
	print("Starting runs!")

	k_list = [5, 10, 20, 40, 80, 160]

	for s in (1, 5, 10, 20, 40, 80):
		training_matrix = np.matmul(pca_result[:s], training_images.T)
		test_matrix = np.matmul(pca_result[:s], test_images.T)

		now = datetime.datetime.now()
		print(now.strftime("%Y-%m-%d %H:%M:%S"), "Running PCA + kNN test with s =", s, "and k = ", k_list, "...")
		test_run(training_matrix, test_matrix, training_labels, test_labels, k_list, s)

	now = datetime.datetime.now()
	print(now.strftime("%Y-%m-%d %H:%M:%S"), "Running kNN test with k = ", k_list, "...")
	test_run(training_images, test_images, training_labels, test_labels, k_list)

	print("Test complete!")


main()
