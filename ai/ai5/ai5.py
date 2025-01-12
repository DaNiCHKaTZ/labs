class KnowledgeBase:
    def __init__(self):
        self.facts = {}
        self.user_facts = {}
        self.rules = []
        self.conclusions = []

    def add_fact(self, fact, value, user_defined=True):
        self.facts[fact] = value
        if user_defined:
            self.user_facts[fact] = value

    def add_rule(self, condition, conclusion, rule_number):
        self.rules.append((condition, conclusion, rule_number))

    def evaluate_rules(self):
        while True:
            cycle_continues = False
            for condition, conclusion, rule_number in self.rules:
                if self.evaluate_complex_condition(condition):
                    if conclusion[0] not in self.facts:
                        self.facts[conclusion[0]] = conclusion[1]
                        self.conclusions.append((conclusion, rule_number))
                        self.rules.remove((condition, conclusion, rule_number))
                        cycle_continues = True

            if not cycle_continues:
                break

    def evaluate_complex_condition(self, condition):
        for fact, value in condition.items():
            if value is None and fact in self.facts:
                continue
            if fact not in self.facts:
                if any(self.facts.get(f) == v for f, v in condition.items() if v is not None):
                    user_value = input(f"Введите значение для {fact}: ")
                    self.facts[fact] = user_value
                    self.user_facts[fact] = user_value
            if self.facts.get(fact) != value and value is not None:
                return False
        return True

    def display_conclusions(self):
        print("Факты, определенные пользователем:")
        for fact, value in self.user_facts.items():
            print(f"{fact} = {value}")
        
        print("\nФакты, выведенные из правил:")
        sorted_conclusions = sorted(self.conclusions, key=lambda x: 'Д' not in x[0][0])
        for (fact, value), rule_number in sorted_conclusions:
            print(f"Правило {rule_number}: {fact} = {value}")
        
        print("\nОкончательный логический вывод:")
        for fact, value in self.facts.items():
            if 'Д' in fact:
                print(f"{fact} = {value}")


kb = KnowledgeBase()

kb.add_fact('СТ', 'не включается')
kb.add_fact('СТМ', 'повреждена') 

kb.add_rule({'СТ': 'не включается'}, ('ЗП', 'отсутствует звук'), 1)
kb.add_rule({'ЗП': 'отсутствует звук', 'ПИ': 'не горят индикаторы'}, ('Д', 'неисправность питания'), 2)
kb.add_rule({'ОС': 'не загружается', 'ПИ': 'мигают'}, ('Д', 'повреждение жесткого диска'), 3)
kb.add_rule({'УТ': 'высокая', 'ВЛ': 'отсутствует изображение'}, ('Д', 'перегрев'), 4)
kb.add_rule({'ПИ': 'горят индикаторы', 'СТ': 'не включается'}, ('Д', 'проблема с материнской платой'), 5)
kb.add_rule({'ВЛ': 'искаженное изображение', 'ВР': 'неплотное соединение'}, ('Д', 'проблема с разъемом'), 6)
kb.add_rule({'ПО': 'не включается'}, ('ПИ', 'не горят индикаторы'), 7)
kb.add_rule({'СТЖ': 'поврежден', 'УТ': 'высокая'}, ('Д', 'неисправность жесткого диска'), 8)
kb.add_rule({'СТМ': 'повреждена'}, ('ОС', 'не загружается'), 9)
kb.add_rule({'ОС': 'не загружается', 'ПИ': 'горят индикаторы', 'ПО': 'включено'}, ('Д', 'неисправность операционной системы'), 10)
kb.add_rule({'УТ': 'нормальная', 'СТМ': 'повреждена'}, ('Д', 'неисправность материнской платы'), 11)

kb.evaluate_rules()
kb.display_conclusions()
