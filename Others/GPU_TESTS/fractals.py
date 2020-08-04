import numpy as np
from timeit import default_timer as timer
from numba import cuda
from numba import *
from pylab import imshow, show


@cuda.jit(device=True)
def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i
    return max_iters


# mandel_gpu = cuda.jit(device=True)(mandel)


@cuda.jit
def mandel_kernel(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    startX, startY = cuda.grid(2)
    gridX = cuda.gridDim.x * cuda.blockDim.x;
    gridY = cuda.gridDim.y * cuda.blockDim.y;

    for x in range(startX, width, gridX):
        real = min_x + x * pixel_size_x
        for y in range(startY, height, gridY):
            imag = min_y + y * pixel_size_y
            image[y, x] = mandel(real, imag, iters)


def cpu_mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i
    return max_iters


def cpu_and_gpu_upgraded():
    gimage = np.zeros((1024, 1536), dtype=np.uint8)
    blockdim = (32, 8)
    griddim = (32, 16)

    start = timer()
    d_image = cuda.to_device(gimage)
    mandel_kernel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, d_image, 20)
    d_image.to_host()
    dt = timer() - start

    print("(CPU+GPU Upgraded) Mandelbrot created in %f s" % dt)

    imshow(gimage)
    show()


def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            image[y, x] = cpu_mandel(real, imag, iters)


def cpu_only():
    image = np.zeros((1024, 1536), dtype=np.uint8)
    start = timer()
    create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20)
    dt = timer() - start

    print("(CPU Only) Mandelbrot 1 created in %f s" % dt)
    imshow(image)
    show()

    start = timer()

    create_fractal(-2.0, -1.7, -0.1, 0.1, image, 20)
    dt = timer() - start
    imshow(image)
    show()

    print("(CPU Only) Mandelbrot 2 created in %f s" % dt)


def cpu_and_gpu():
    @cuda.jit
    def basic_mandel_kernel(min_x, max_x, min_y, max_y, image, iters):
        height = image.shape[0]
        width = image.shape[1]

        pixel_size_x = (max_x - min_x) / width
        pixel_size_y = (max_y - min_y) / height

        startX = cuda.blockDim.x * cuda.blockIdx.x + cuda.threadIdx.x
        startY = cuda.blockDim.y * cuda.blockIdx.y + cuda.threadIdx.y
        gridX = cuda.gridDim.x * cuda.blockDim.x
        gridY = cuda.gridDim.y * cuda.blockDim.y

        for x in range(startX, width, gridX):
            real = min_x + x * pixel_size_x
            for y in range(startY, height, gridY):
                imag = min_y + y * pixel_size_y
                image[y, x] = mandel(real, imag, iters)

    gimage = np.zeros((1024, 1536), dtype=np.uint8)
    blockdim = (32, 8)
    griddim = (32, 16)

    start = timer()
    d_image = cuda.to_device(gimage)
    basic_mandel_kernel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, d_image, 20)
    d_image.to_host()
    dt = timer() - start

    print("(CPU+GPU) Mandelbrot created in %f s" % dt)

    imshow(gimage)
    show()


# GPU and CUDA need to be present
def main():
    cpu_only()
    cpu_and_gpu()
    cpu_and_gpu_upgraded()
    cpu_and_gpu_upgraded()


if __name__ == '__main__':
    main()
