import random


def weight(solution, weight_matrix):
    return sum(weight_matrix[i][solution[i]] for i in range(len(solution)))


def init(work_size, num_tasks):
    workers = []
    for _ in range(work_size):
        worker = list(range(num_tasks))
        random.shuffle(worker)
        workers.append(worker)
    return workers


def selection(workers, cost_matrix):
    veroytnost = [1 / (weight(ind, cost_matrix) + 1) for ind in workers]
    return random.choices(workers, veroytnost, k=len(workers)//2)


def replication(parent1, parent2):
    size = len(parent1)
    cxpoint = random.randint(0, size - 1)
    child1 = parent1[:cxpoint] + [p for p in parent2 if p not in parent1[:cxpoint]]
    child2 = parent2[:cxpoint] + [p for p in parent1 if p not in parent2[:cxpoint]]
    return child1, child2


def mutate(worker):
    size = len(worker)
    for _ in range(size//10):
        i, j = random.sample(range(size), 2)
        worker[i], worker[j] = worker[j], worker[i]


def genetic_algorithm(cost_matrix, pop_size=100, generations=500):
    num_tasks = len(cost_matrix)
    workers = init(pop_size, num_tasks)

    for _ in range(generations):
        selected = selection(workers, cost_matrix)
        offspring = []
        while len(offspring) < pop_size:
            parent1, parent2 = random.sample(selected, 2)
            child1, child2 = replication(parent1, parent2)
            mutate(child1)
            mutate(child2)
            offspring.extend([child1, child2])

        workers = sorted(offspring, key=lambda ind: weight(ind, cost_matrix))[:pop_size]

    solution = min(workers, key=lambda ind: weight(ind, cost_matrix))
    return solution, weight(solution, cost_matrix)


matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

solution, min_cost = genetic_algorithm(matrix)
print("Лучшее решение:", solution)
print("Стоимость решения:", min_cost)
