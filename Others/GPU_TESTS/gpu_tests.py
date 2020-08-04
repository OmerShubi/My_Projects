import numpy as np
from timeit import default_timer as timer
from numba import vectorize
import fractals


def pow_cpu_only(a, b, c):
    for i in range(a.size):
        c[i] = a[i] ** b[i]


def cpu_only(vector_size):
    print("Running test on CPU only...")
    vec_size = vector_size

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    pow_cpu_only(a, b, c)
    duration = timer() - start

    print("Time Taken: ", "{0:.5f}".format(duration), "seconds")


@vectorize(['float32(float32, float32)'], target='cuda')
def pow_cpu_and_gpu(a, b):
    return a ** b


def cpu_and_gpu(vector_size):
    print("Running test on CPU+GPU only...")
    vec_size = vector_size

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    c = pow_cpu_and_gpu(a, b)
    duration = timer() - start

    print("Time Taken: ", "{0:.5f}".format(duration), "seconds")


def add_test(cuda_or_cpu):
    print("Running test on ", cuda_or_cpu)
    start = timer()

    @vectorize(['float32(float32, float32)'], target=cuda_or_cpu)
    def add(x, y):
        return x + y

    # Initialize arrays
    n = 100000000
    a = np.ones(n, dtype=np.float32)
    b = np.ones(a.shape, dtype=a.dtype)
    C = np.empty_like(a, dtype=a.dtype)

    # Add arrays on GPU
    C = add(a, b)
    duration = timer() - start

    print("Time Taken: ", "{0:.5f}".format(duration), "seconds")


# GPU and CUDA need to be present
def main():
    test_size = 100000000

    print("Test #1 - Vectors:\n"
          "Creates two vectors, each with 100 Million elements, all filled with random values.\n"
          "Then, creates a third vector which consists of each element in first vector\n"
          "raised to the power of the corresponding element in the the second vector.\n")
    cpu_only(test_size)
    cpu_and_gpu(test_size)
    print("\n\n"
          "Test #2 - Fractals\n")
    fractals.main()


if __name__ == '__main__':
    main()
