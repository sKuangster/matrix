import numpy as np

# Define the matrix
B = np.array([[1, 3, 2, -1],
              [1, 1, 1, 1],
              [2, -2, 1, -1],
              [1, -3, -1, 2]])

# Calculate the inverse of the matrix
def calculate_inverse(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return None  # Inverse does not exist if matrix is singular

# Get the inverse of the matrix
inverse_matrix = calculate_inverse(B)
print(inverse_matrix)