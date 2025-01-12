class SemanticNetwork:
    def __init__(self):
        self.network = {}

    def add_relation(self, node1, relation, node2):
        if node1 not in self.network:
            self.network[node1] = []
        self.network[node1].append((relation, node2))

    def print_network(self):
        for node, edges in self.network.items():
            print(f"{node}:")
            for relation, target in edges:
                print(f"  -> {relation} {target}")

    def print_node_info(self, node):
        if node in self.network:
            print(f"Информация об узле '{node}':")
            for relation, target in self.network[node]:
                print(f"  {relation} -> {target}")
        else:
            print(f"Узел '{node}' не найден в сети.")

    def answer_question(self, relation, node):
        if node in self.network:
            found = False
            for rel, target in self.network[node]:
                if rel == relation:
                    print(f"{node} {relation} {target}")
                    found = True
            if not found:
                print(f"Нет информации о том, что {node} {relation}.")
        else:
            print(f"Узел '{node}' не найден в сети.")

semantic_network = SemanticNetwork()
semantic_network.add_relation("интернет-кафе", "имеет", "Адрес")
semantic_network.add_relation("Адрес", "например", "Фрунзе 33")
semantic_network.add_relation("интернет-кафе", "например", "Тул-Бар")
semantic_network.add_relation("Тул-Бар", "работает", "Антон")
semantic_network.add_relation("Тул-Бар", "работает", "Мария")
semantic_network.add_relation("человек", "наследник", "сотрудник")
semantic_network.add_relation("человек", "наследник", "клиент")
semantic_network.add_relation("сотрудник", "например", "Антон")
semantic_network.add_relation("сотрудник", "например", "Мария")
semantic_network.add_relation("клиент", "например", "Андрей")
semantic_network.add_relation("Андрей", "заказал", "услуга для Андрея")
semantic_network.add_relation("услуга для Андрея", "принял", "Мария")
semantic_network.add_relation("услуга", "например", "игра на ПК")
semantic_network.add_relation("игра на ПК", "имеет", "цена")
semantic_network.add_relation("цена", "например", "20 р")
semantic_network.add_relation("игра на ПК", "имеет", "время")
semantic_network.add_relation("время", "например", "2 ч.")
semantic_network.add_relation("услуга для Андрея", "стоит", "20 р")
semantic_network.add_relation("услуга для Андрея", "длится", "2 ч.")

def search_node_info(semantic_network, node):
    if node in semantic_network.network:
        semantic_network.print_node_info(node)
    else:
        print(f"Узел '{node}' не найден в сети.")



semantic_network.answer_question("работает", "Тул-Бар")

semantic_network.print_network()
