import numpy

# Write a function that, given two integers m and n, returns an m by n matrix where the element in the i-th row and j-th column is equal to i*j.
# The function should return a numpy array of type float64.
def funA (m, n):
   i = numpy.arange(m, dtype=numpy.float64).reshape(m, 1) # column vector whose length is equal to m
   j = numpy.arange(n, dtype=numpy.float64).reshape(1, n)  # row vector whose length is equal to n
   return i * j

# Write a function that, given a matrix, returns a new matrix where each element is the original element divided by the sum of its column.
def funB (matrix):
   # axis=0 calculates the sum of each column
   column_sums = matrix.sum(axis=0) # this is a row vector whose dimensions are (columns,). We will need to reshape it to (1, columns) to perform the division correctly.

   # Broadcasting will automatically reshape the 1D vector into a 2D vector of shape (1, columns) when performing the division
   # After that, a comparison between the shape of the original matrix (rows, columns) and the reshaped column_sums (1, columns) will be made
   # The reshaped column_sums will be stretched along the rows reaching (rows, columns) size to match the shape of the original matrix, allowing for element-wise division to be performed correctly
   return matrix/column_sums


# Write a function that, given a matrix, returns a new matrix where each element is the original element divided by the sum of its row.
def funC(matrix):
    # axis=1 calculates the sum of each row
    # keepdims=True ensures the result is (rows, 1) instead of (rows,)
    row_sums = matrix.sum(axis=1, keepdims=True)

    # Similar to funB, broadcasting will automatically reshape the 1D vector into a 2D vector of shape (rows, 1) when performing the division
    # After that, a comparison between the shape of the original matrix (rows, columns) and the reshaped row_sums (rows, 1) will be made
    # The reshaped row_sums will be stretched along the columns reaching (rows, columns) size to match the shape of the original matrix, allowing for element-wise division to be performed correctly   
    return matrix / row_sums


# Write a function that, given a numpy array of any shape, returns an array with the same shape but all negative elements set to 0. The function should not modify the original array.
def funD (matrix):
   return numpy.maximum(matrix, 0)


# Write a function that computes the sum of the elements of a product of two matrices
def funE (matrixA, matrixB):
    # Compute the product of the two matrices
    product = numpy.dot(matrixA, matrixB)

    # Compute the sum of the elements in the product matrix
    return numpy.sum(product)



if __name__ == "__main__":
   print("--- Testing Exercise 7 ---")

   # --- Test funA ---
   m, n = 3, 4
   matrix_a = funA(m, n)
   print(f"\n1. funA({m}, {n}) Result:\n{matrix_a}")
   print("Expected: 3x4 matrix where element [i][j] = i*j")

   # --- Test funB ---
   # We add 1.0 to avoid division by zero
   test_matrix = matrix_a + 1.0 
   col_norm = funB(test_matrix)
   print(f"\n2. funB (Column Normalization) Result:\n{col_norm}")
   print(f"Verification (Column Sums): {numpy.sum(col_norm, axis=0)}")
   print("Expected: Each column should sum to 1.0")

   # --- Test funC ---
   row_norm = funC(test_matrix)
   print(f"\n3. funC (Row Normalization) Result:\n{row_norm}")
   print(f"Verification (Row Sums): {numpy.sum(row_norm, axis=1)}")
   print("Expected: Each row should sum to 1.0")

   # --- Test funD ---
   neg_matrix = numpy.array([[1, -2, 3], [-4, 5, -6]])
   zero_neg = funD(neg_matrix)
   print(f"\n4. funD (Negative to Zero) Result:\n{zero_neg}")
   print("Expected: [[1, 0, 3], [0, 5, 0]]")

   # --- Test funE ---
   # Matrix A (2x3) and Matrix B (3x2)
   mat1 = numpy.array([[1, 2, 3], [4, 5, 6]])
   mat2 = numpy.array([[1, 0], [0, 1], [1, 1]])
   sum_prod = funE(mat1, mat2)
   # Product is [[4, 5], [10, 11]], sum is 30
   print(f"\n5. funE (Sum of Matrix Product) Result: {sum_prod}")
   print("Expected: 30.0")
