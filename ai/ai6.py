class Insect:
    class Family:
        class Type:
            class Subtype:
                def __init__(self, name, characteristics):
                    self.name = name
                    self.characteristics = characteristics
                    self.examples = []  

            def __init__(self, name, habitat):
                self.name = name
                self.habitat = habitat 
                self.subtypes = []

            def add_subtype(self, name, characteristics):
                subtype = self.Subtype(name, characteristics)
                self.subtypes.append(subtype)

        def __init__(self, family_name, number_of_species):
            self.family_name = family_name
            self.number_of_species = number_of_species  
            self.types = []

        def add_type(self, name, habitat):
            insect_type = self.Type(name, habitat)
            self.types.append(insect_type)
            return insect_type

    def __init__(self, insect_name, region):
        self.insect_name = insect_name
        self.region = region  
        self.families = []

    def add_family(self, family_name, number_of_species):
        family = self.Family(family_name, number_of_species)
        self.families.append(family)
        return family

    def check(self, subtype_name, characteristic_key, characteristic_value):
        for family in self.families:
            for type_obj in family.types:
                for subtype in type_obj.subtypes:
                    if subtype.name.lower() == subtype_name.lower():
                        if subtype.characteristics.get(characteristic_key.lower()) == characteristic_value:
                            return "Да"
                        else:
                            return "Нет"
        return "Нет"

insects = Insect("Насекомые", "Весь мир")

beetles_family = insects.add_family("Жуки", 350000)
ladybug_type = beetles_family.add_type("Божья коровка", "Луга и леса")
ladybug_type.add_subtype("Семиточечная", {"цвет": "красный", "пятна": 7, "размер": "5-8 мм"})

butterflies_family = insects.add_family("Бабочки", 180000)
swallowtail_type = butterflies_family.add_type("Махаоны", "Луга и сады")
swallowtail_type.add_subtype("Махаон обыкновенный", {"размах крыльев": "70-90 мм", "цвет": "желто-черный", "миграция": "осенняя и весенняя"})

mosquit_family = insects.add_family("Комары", 3500)
anopheles_type = mosquit_family.add_type("Анофелесы", "Тропические регионы")
anopheles_type.add_subtype("Анофелес гамбии", {"место обитания": "тропики", "болезнь": "малярия", "размер": "3-4 мм"})

def print_details(insect):
    print(f"Насекомое: {insect.insect_name}, Регион: {insect.region}")
    for family in insect.families:
        print(f"  Семейство: {family.family_name}, Количество видов: {family.number_of_species}")
        for type_obj in family.types:
            print(f"    Тип: {type_obj.name}, Место обитания: {type_obj.habitat}")
            for subtype in type_obj.subtypes:
                print(f"      Подтип: {subtype.name}")
                for key, value in subtype.characteristics.items():
                    print(f"        {key.capitalize()}: {value}")

print_details(insects)



print(insects.check("V", "цвет", "черный"))
