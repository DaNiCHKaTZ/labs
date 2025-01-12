import numpy as np
V = np.array([[-1.45, -0.128, 0.733, 1], [-0.124, 0.808, -1.467, 1], [0.618, -2.054, -0.502, 1], [1.1, 0.594, 0.916, 1]])
A = np.array([[2, 1.5, 4.5, 5.5], [1.5, 3, 2, 1.6], [4.5, 2, 3, 1.7], [5.5, 1.6, 1.7, 3]])
M1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [-3.235,-0.941,0.588,-1.764], [0, 0, 0, 1]])
M_1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [5.5,1.6,1.7,3], [0, 0, 0, 1]])
A1 = np.array([[-12.55, -2.73, 2.64, -2.44], [-4.97, 1.11, 1.17, -1.92], [-85.87,-14.65,22.44,-22.62], [0, 0, 1, 0]])
M2 = np.array([[1, 0, 0, 0], [-5.85,-0.06,1.53,-1.54], [0,0,1,0], [0, 0, 0, 1]])
M_2 = np.array([[1, 0, 0, 0],  [-85.87,-14.65,22.44,-22.62], [0,0,1,0], [0, 0, 0, 1]])
A2=np.array([[3.46,0.186,-1.54,1.78], [-129.051, 7.531, 67.40,-99.397], [0, 1, 0, 0], [0, 0, 1, 0]])
M3 = np.array([[-0.007,0.058,0.52,-0.7702], [0, 1, 0, 0], [0,0,1,0], [0, 0, 0, 1]])
M_3 = np.array([[-129.051, 7.531, 67.40,-99.397], [0, 1, 0, 0], [0,0,1,0], [0, 0, 0, 1]])
A3=np.array([[11, 17.2, -134.3, 114.917], [1, 0, 0, 0], [0,1,0,0], [0, 0, 1, 0]])
def danilevsky_method(matrix):
    n = len(matrix)
    frobenius_matrix = matrix.copy()
 
    for k in range(n - 1, 0, -1):
        M = np.eye(n)
        M_inv = np.eye(n)
        for i in range(n):
            M[i, k] = -frobenius_matrix[i, k] / frobenius_matrix[k, k]
            M_inv[i, k] = frobenius_matrix[i, k] / frobenius_matrix[k, k]
            print(M[i,k])
            print(M_inv[i, k])
        frobenius_matrix = M_inv @ frobenius_matrix @ M
        print(frobenius_matrix)

    char_poly = np.zeros(n + 1, dtype=complex)
    char_poly[0] = (-1) ** n
    char_poly[1:] = -frobenius_matrix[-1, :]

    eigenvalues = np.roots(char_poly)
    eigenvectors = np.zeros((n, n), dtype=complex)

    for i in range(n):
        eigenvectors[:, i] = np.linalg.solve(matrix - eigenvalues[i] * np.eye(n), np.zeros(n, dtype=complex))

    return eigenvalues, eigenvectors





print(M1)
print(M_1)
print(A1)
print(M2)
print(M_2)
print(A2)
print(M3)
print(M_3)
print(A3)


eigenvalues, eigenvectors = np.linalg.eig(A)

print("Собственные значения:")
print(sorted(eigenvalues))

print("\nСобственные векторы:")
print(V)

