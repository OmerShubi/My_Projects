import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def helper_best_rank_k_approximation(input_matrix, k, print_result=False):
    """
    Helper function for best_rank_k_approximation.
    Performs SVD on a given matrix and creates lower (k) dim matrix.

    Args:
    input_matrix (np.ndarray): a matrix representing one of r/g/b image
    k (int): the desired rank of out_matrix
    print_result (bool): default False

    Returns:
        out_matrix
    """
    matrix = np.array(input_matrix)
    u, singular_values, v = np.linalg.svd(matrix, full_matrices=False)
    rows = np.ma.size(matrix, 0)
    columns = np.ma.size(matrix, 1)
    out_matrix = np.zeros((rows, columns))

    for i in range(k):
        temp = (singular_values[i]*u[:, i:i+1])
        out_matrix += (np.matmul(temp, v[i:i+1, :]))

    singular_values_squared = singular_values*singular_values
    calculated_rate = sum(singular_values_squared[k:]) / sum(singular_values_squared)

    if print_result:
        print("When k is ", k, ", error of red matrix is ", calculated_rate)

    return out_matrix, calculated_rate


def best_rank_k_approximation(image_name, k_list):
    """
    Creates 'compressed' images of lower resolution from a given image.
    Each k value in k_list will create a save a new image with corresponding name.
    Args:
    image_name (str): file location, assumes location same folder.
    k_list (list): the desired k values to be used.
    """
    image = Image.open(image_name)
    b, g, r = image.split()
    rates_b = []
    rates_r = []
    rates_g = []

    for k_value in k_list:
        r_new, rate_r = helper_best_rank_k_approximation(r, k_value, print_result=True)
        g_new, rate_g = helper_best_rank_k_approximation(g, k_value)
        b_new, rate_b = helper_best_rank_k_approximation(b, k_value)
        image_r_new = Image.fromarray(r_new.clip(0, 255).astype('uint8'))
        image_g_new = Image.fromarray(g_new.clip(0, 255).astype('uint8'))
        image_b_new = Image.fromarray(b_new.clip(0, 255).astype('uint8'))
        image_new = Image.merge("RGB", (image_b_new, image_g_new, image_r_new))
        image_new.save(str(k_value)+"_approximation_"+image_name)
        rates_b.append(rate_b*100)
        rates_g.append(rate_g*100)
        rates_r.append(rate_r*100)

    plt.plot(k_list, rates_b, 'b', k_list, rates_r, 'r', k_list, rates_g, 'g')
    plt.xlabel('k (values)')
    plt.ylabel('Error Rate (percentage)')
    plt.title('Best Rank K Approximation')
    plt.show()


def main():
    k = list(range(5, 165, 5))
    best_rank_k_approximation("cute_dog.jpg", k)


main()
