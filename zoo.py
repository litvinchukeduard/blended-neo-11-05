from enum import Enum, StrEnum, auto
# Zoo, Enclosure, Animal

# Zoo <- list[Enclosure]
# Enclosure <- Animal
# Enclosure is limited by animal species

# Tiger, Zebra, Penguin, Lion

# class Species(Enum):
class Species(StrEnum):
    TIGER = auto()
    ZEBRA = auto()
    PENGUIN = auto()
    LION = auto()

# species_one = Species.LION
# print(species_one)
# print(species_one.value)

class Animal:
    def __init__(self, name: str, age: str, species: Species):
        self.name = name
        self.age = age
        if type(species) != Species:
            raise ValueError
        self.species = species



class Enclosure:
    def __init__(self, max_animals) -> None:
        self.animals = []
        self.animal_counter = 0
        self.max_animals = max_animals
        self.species = None

    def add_animal(self, animal: Animal):
        if (self.animal_counter + 1) > self.max_animals:
            raise ValueError
        # for animal in self.animals
        # if self.species is None or self.species == animal.species:
        #     self.animals.append(animal)
        # else:
        #     raise ValueError
        if self.species is not None and self.species != animal.species:
            raise ValueError
        self.species = animal.species
        self.animals.append(animal)


class Zoo:
    def __init__(self, name):
        self.name = name
        self.enclosures = []

    def add_animal(self, animal: Animal):
        for enclosure in self.enclosures:
            try:
                enclosure.add_animal(animal)
                return
            except ValueError:
                print('Can\'t add this animal in this enclosure')
        enclosure = Enclosure(10)
        enclosure.add_animal(animal)
        self.enclosures.append(enclosure)


animal_one = Animal('Marvin', 10, Species.ZEBRA)
animal_two = Animal('Kovalski', 5, Species.PENGUIN)

enclosure = Enclosure(5)

enclosure.add_animal(animal_one)
# enclosure.add_animal(animal_two)

zoo = Zoo('Zoo one')

# for _ in range
        
