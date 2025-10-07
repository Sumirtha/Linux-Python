def add_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices dimensions do not match for addition.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result
def subtract_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices dimensions do not match for subtraction.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result
A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8, 9],
    [1, 2, 3]
]
print("Matrix Addition:")
for row in add_matrices(A, B):
    print(row)

print("\nMatrix Subtraction:")
for row in subtract_matrices(A, B):
    print(row)
#addition and subtraction are not defined
C = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print("\nTrying to add matrices of different sizes:")
print(add_matrices(A, C))

