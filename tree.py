class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

    def depth(self, node, key, level=1):
        if node is None:
            return 0
        if node.val == key:
            return level
        downlevel = self.depth(node.left, key, level + 1)
        if downlevel != 0:
            return downlevel
        downlevel = self.depth(node.right, key, level + 1)
        return downlevel

    def delete_leaf(self, key):
        self.root = self._delete_leaf(self.root, key)

    def _delete_leaf(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete_leaf(node.left, key)
        elif key > node.val:
            node.right = self._delete_leaf(node.right, key)
        else:
            if node.left is None and node.right is None:  # Узел является листом
                node = None
            elif node.right is None:  # Узел имеет только левого потомка
                node = node.left
            elif node.left is None:  # Узел имеет только правого потомка
                node = node.right
            else:  # Узел имеет обоих потомков
                temp = self._find_min(node.right)
                node.val = temp.val
                node.right = self._delete_leaf(node.right, temp.val)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


    def print_tree(self, node, level=0, side='R'):
        if node is not None:
            self.print_tree(node.right, level + 1, 'R')
            print(' ' * 4 * level + side + ':', node.val)
            self.print_tree(node.left, level + 1, 'L')
    # Добавить функцию, которая находит путь с минимальной суммой конечных вершин и максимальной длиной


    def min_sum_max_len_path(self, node):
        # Если узел пустой, вернуть ноль, ноль и ноль
        if node is None:
            return 0, 0, 0
        # Если узел является листом, вернуть его значение, единицу и его значение
        if node.left is None and node.right is None:
            return node.val, 1, node.val
        # Рекурсивно найти путь в левом и правом поддеревьях
        left_sum, left_len, left_min = self.min_sum_max_len_path(node.left)
        right_sum, right_len, right_min = self.min_sum_max_len_path(node.right)
        # Вычислить сумму, длину и минимум для текущего узла
        curr_sum = node.val + left_sum + right_sum
        curr_len = max(left_len, right_len) + 1
        curr_min = min(node.val, left_min, right_min)
        # Если левое и правое поддеревья не пустые, сравнить их суммы и длины
        if node.left and node.right:
            # Если сумма левого поддерева меньше суммы правого поддерева, или они равны, но длина левого поддерева больше длины правого поддерева
            if left_sum < right_sum or (left_sum == right_sum and left_len > right_len):
                # Вернуть сумму, длину и минимум левого поддерева
                return left_sum, left_len, left_min
            # Иначе, вернуть сумму, длину и минимум правого поддерева
            else:
                return right_sum, right_len, right_min
        # Если левое поддерево пустое, вернуть сумму, длину и минимум правого поддерева
        elif node.left is None:
            return right_sum, right_len, right_min
        # Если правое поддерево пустое, вернуть сумму, длину и минимум левого поддерева
        else:
            return left_sum, left_len, left_min

    # Добавить функцию, которая делает центральную вершину пути корнем дерева методом поворотов
    def rotate_path(self, node, key):
        # Если узел пустой или равен ключу, вернуть узел
        if node is None or node.val == key:
            return node
        # Если ключ меньше значения узла, искать ключ в левом поддереве
        if key < node.val:
            # Рекурсивно повернуть левое поддерево
            node.left = self.rotate_path(node.left, key)
            # Повернуть узел вправо
            temp = node.left
            node.left = temp.right
            temp.right = node
            # Вернуть новый корень
            return temp
        # Если ключ больше значения узла, искать ключ в правом поддереве
        else:
            # Рекурсивно повернуть правое поддерево
            node.right = self.rotate_path(node.right, key)
            # Повернуть узел влево
            temp = node.right
            node.right = temp.left
            temp.left = node
            # Вернуть новый корень
            return temp

    # Добавить функцию, которая решает задачу
    def solve(self):
        # Найти путь с минимальной суммой конечных вершин и максимальной длиной
        path_sum, path_len, path_min = self.min_sum_max_len_path(self.root)
        # Сделать центральную вершину этого пути корнем дерева методом поворотов
        self.root = self.rotate_path(self.root, path_min)
        # Выполнить прямой (левый) обход полученного дерева
        self.preorder(self.root)





# Создание бинарного поискового дерева
bt = BinaryTree()

# Добавление элементов
bt.insert(8)
bt.insert(3)
bt.insert(10)
bt.insert(1)
bt.insert(6)
bt.insert(14)
bt.insert(4)
bt.insert(7)
bt.insert(13)
bt.print_tree(bt.root)
# Обход дерева
print("Прямой обход:")
bt.preorder(bt.root)
print("\nОбратный обход:")
bt.postorder(bt.root)
print("\nСимметричный обход:")
bt.inorder(bt.root)

# Поиск элемента
print("\nГлубина узла со значением 7:")
print(bt.depth(bt.root, 7))

# # Удаление элемента
# bt.delete_leaf(7)
# print("\nСимметричный обход после удаления узла со значением 7:")
# bt.inorder(bt.root)

bt.solve()
bt.print_tree(bt.root)
