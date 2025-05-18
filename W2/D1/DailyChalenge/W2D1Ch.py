# Daily challenge: Old MacDonald’s Farm
class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals.update({animal_type: count})

    def get_info(self):
        a = max(len(animal) for animal in self.animals.keys())
        output_string = self.name + " farm\n"
        for animal, amount in self.animals.items():
            output_string += animal + ' ' * (a - len(animal) + 1) + ': ' + str(amount) + '\n'
        output_string += f"\n{'E-I-E-I-0!':>15}"
        return output_string

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        list_animals_for_string = []
        for name in self.get_animal_types():
            if self.animals[name] == 1:
                list_animals_for_string.append(name)
            else:
                list_animals_for_string.append(name + 's')
        string_farm_info = f"{self.name} farm has {', '.join(list_animals_for_string)}."
        return string_farm_info


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
