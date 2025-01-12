from typing import Dict

class Rule:
    def __init__(self, id: int, condition: Dict[str, str], conclusion: Dict[str, str]):
        self.id = id
        self.condition = condition
        self.conclusion = conclusion

class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}
        self.user_inputs = {}

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def set_rules(self):
        self.add_rule(Rule(1, {"СТ": "не включается"}, {"ЗП": "отсутствует звук"}))
        self.add_rule(Rule(2, {"ЗП": "отсутствует звук", "ПИ": "не горят индикаторы"}, {"Д": "неисправность питания"}))
        self.add_rule(Rule(3, {"ОС": "не загружается", "ПИ": "горят индикаторы"}, {"Д": "повреждение жесткого диска"}))
        self.add_rule(Rule(4, {"УТ": "высокая", "ВЛ": "отсутствует изображение"}, {"Д": "перегрев"}))
        self.add_rule(Rule(5, {"ПИ": "горят индикаторы", "СТ": "не включается"}, {"Д": "проблема с материнской платой"}))
        self.add_rule(Rule(6, {"ВЛ": "искаженное изображение", "ВР": "неплотное соединение"}, {"Д": "проблема с разъемом"}))
        self.add_rule(Rule(7, {"ПО": "не включается"}, {"ПИ": "не горят индикаторы"}))
        self.add_rule(Rule(8, {"СТЖ": "поврежден", "УТ": "высокая"}, {"Д": "неисправность жесткого диска"}))
        self.add_rule(Rule(9, {"СТМ": "повреждена"}, {"ОС": "не загружается"}))
        self.add_rule(Rule(10, {"ОС": "не загружается", "ПИ": "горят индикаторы", "ПО": "включено"}, {"Д": "неисправность операционной системы"}))
        self.add_rule(Rule(11, {"УТ": "нормальная", "СТМ": "повреждена"}, {"Д": "неисправность материнской платы"}))

    def query_user(self, variable: str) -> str:
        if variable in self.user_inputs:
            return self.user_inputs[variable]
        value = input(f"Введите значение для {variable}: ")
        self.user_inputs[variable] = value
        return value

    def resolve_variable(self, variable: str) -> str:
        if variable in self.facts:
            return self.facts[variable]
        for rule in self.rules:
            if variable in rule.conclusion:
                if self.process_rule(rule):
                    return self.facts[variable]
        return self.query_user(variable)

    def process_rule(self, rule: Rule) -> bool:
        for cond, expected_value in rule.condition.items():
            if cond not in self.facts:
                self.facts[cond] = self.resolve_variable(cond)
            if self.facts[cond] != expected_value:
                self.rules.remove(rule)
                return False
        for conclusion_var, conclusion_value in rule.conclusion.items():
            self.facts[conclusion_var] = conclusion_value
        print(f"Правило {rule.id} сработало: {rule.conclusion}")
        self.rules.remove(rule)
        return True

    def backward_chaining(self, goal: str) -> bool:
        if goal in self.facts:
            return True
        for rule in self.rules:
            if goal in rule.conclusion:
                if self.process_rule(rule):
                    return True
        return False

def main():
    es = ExpertSystem()
    es.set_rules()
    es.facts = {
        "СТ": "не включается"
    }
    goal = "Д"
    if es.backward_chaining(goal):
        print(f"Цель достигнута: {goal} = {es.facts[goal]}")
    else:
        print(f"Цель не достигнута: {goal}")

if __name__ == "__main__":
    main()
