# GPU Tests

To run one needs a GPU to be available.

## Test #1 - Vectors

Creates two vectors, each with 100 Million elements, all filled with random values.
Then, creates a third vector which consists of each element in first vector
raised to the power of the corresponding element in the the second vector.

`Running test on CPU only...
Time Taken:  53.50766 seconds`

`Running test on CPU+GPU only...
Time Taken:  0.46353 seconds`


## Test #2 - Fractals

Create Fractal Images

```
(CPU Only) Mandelbrot 1 created in 5.304309 s
(CPU Only) Mandelbrot 2 created in 4.168567 s
(CPU+GPU) Mandelbrot created in 0.204925 s
(CPU+GPU Upgraded) Mandelbrot created in 0.181051 s
(CPU+GPU Upgraded) Mandelbrot created in 0.006650 s
```

![Mandelbrot_1](/results/Mandelbrot_1.png)

![Mandelbrot_2](/results/Mandelbrot_2.png)


Run `python gpu_tests.py` to reproduce the results.

Creating a conda environment:

`conda create -n gpu_tests numba numpy matplotlib cudatoolkit`