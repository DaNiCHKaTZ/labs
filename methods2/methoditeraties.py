import numpy as np

def simple_iteration_method(C, d, epsilon=0.001, max_iterations=1000):
    x = np.zeros_like(d)  # начальное приближение
    iteration = 0
    while iteration < max_iterations:
        x_new = np.dot(C, x) + d  # находим новое приближение
        if np.linalg.norm(x_new - x) < epsilon:  # проверка на достижение точности
            return x_new
        x = x_new
        iteration += 1
        print(iteration)
    
 

# матрицы C и d

C = np.array([[0, 0.06/-0.95, 0.12/-0.95, -0.14/-0.95],
              [-0.04/-1.12, 0, -0.08/-1.12, -0.11/-1.12],
              [-0.34/-1.06, -0.08/-1.06, 0, -0.14/-1.06],
              [-0.11/-1.03, -0.12/-1.03, 0, 0]])

d = np.array([2.17/-0.95, -1.4/-1.12, 2.1/-1.06, 0.8/-1.03])


# решение системы
solution = simple_iteration_method(C, d)
print(solution)
