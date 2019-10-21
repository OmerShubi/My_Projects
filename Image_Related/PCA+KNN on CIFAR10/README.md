Q. Do you think that PCA is effective for kNN? 

A. Yes! With a very small PCA value the error rate is very similar to performing kNN algorithm with the full data.

Q. Can you identify a value s << n for which the classification error with s-PCA is similar to the classification error on the original data?

A. At s = 20 the classification error is less than 5% away from the classification error on the full images (equal to s = 1024). The drop is substantial from s = 1 (0.9 error = random...) till s = 20. Afterwards remaining error rate difference gradually nears the non-PCA result.

Q. Is the value of this s related to the number of neighbors k or is it independent of it?

A. The value of s is independent of the number of neighbors. Increasing k definitely improves the result, but doesn’t seem to effect the ideal s value.

![graph](/Image_Related/PCA+KNN on CIFAR10/error_rate_as_a_function_of_s_for_each_k.png)
![table](/Image_Related/PCA+KNN on CIFAR10/error_rates_raw.png)