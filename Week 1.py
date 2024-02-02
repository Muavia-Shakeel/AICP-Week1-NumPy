import numpy as np

"""
Write a NumPy program to create an array of all even integers from 30 to 70.
"""


def create_even_array(start, end):
    even_array = np.arange(start, end + 1, 2)
    return even_array


# Example usage
even_array = create_even_array(30, 70)
print("Even array:", even_array)

"""
Write a NumPy program to generate an array of 15 random numbers from a standard normal
distribution.
"""


def generate_random_numbers(size):
    random_numbers = np.random.randn(size)
    return random_numbers


# Example usage
random_numbers = generate_random_numbers(15)
print("Random numbers from a standard normal distribution:", random_numbers)

"""
How to compute the cross-product of two matrices in NumPy?
"""


def compute_cross_product(matrix_a, matrix_b):
    cross_product = np.dot(matrix_a, matrix_b)
    return cross_product


# Example matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Compute the cross-product
result = compute_cross_product(matrix_a, matrix_b)
print("Cross-Product of the two matrices is:\n", result)

"""
Write a NumPy program to compute the determinant of a given square matrix.
"""


def compute_determinant(matrix):
    determinant = np.linalg.det(matrix)
    return determinant


# Example matrix
matrix = np.array([[4, 7], [2, 6]])

# Compute the determinant
det = compute_determinant(matrix)
print("Determinant of the matrix is:\n", det)

"""
Write a NumPy program to create a 3x3x3 array with random values.
"""


def create_random_3d_array():
    random_3d_array = np.random.random((3, 3, 3))
    return random_3d_array


# Create the 3D array
random_3d_array = create_random_3d_array()
print("3x3x3 Array with random values:\n", random_3d_array)

"""
How to create a 5x5 array with random values and find the minimum and maximum values using
NumPy?
"""


def create_array_and_find_extremes():
    random_array = np.random.random((5, 5))

    min_value = np.min(random_array)

    max_value = np.max(random_array)

    return random_array, min_value, max_value


random_array, min_value, max_value = create_array_and_find_extremes()
print("5x5 Array with random values:\n", random_array)
print("Minimum Value:\n", min_value)
print("Maximum Value:\n", max_value)

"""
How to compute the mean, standard deviation, and variance of a given array along the second axis in
NumPy?
"""


def compute_statistics(array):
    mean = np.mean(array, axis=1)
    std = np.std(array, axis=1)
    variance = np.var(array, axis=1)
    return mean, std, variance


array = np.array([[1, 2, 3], [4, 5, 6], [8, 11, 15]])

mean, std, variance = compute_statistics(array)
print("Mean:\n", mean)
print("Standard deviation:\n", std)
print("Variance:\n", variance)
