
# Animal, Mammal, Bird, Fish
# walk, say

class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def walk(self):
        print(f'Animal {self.name}: is walking')

    def say(self):
        print(f'Animal {self.name}: is trying to say something')

# animal_one = Animal('Travis', 2)
# animal_two = Animal("John", 3)

# animal_one.walk()
# animal_two.say()

class Mammal(Animal):
    
    def walk(self):
        print(f'Mammal {self.name}: is walking on four legs')

    def say(self):
        print(f'Mammal {self.name}: is trying to say something')


# animal_one = Animal('Travis', 2)
# mammal_one = Mammal('Scot', 1)

# mammal_one.walk()


class Bird(Animal):

    def say(self):
        print(f'Bird {self.name}: is trying to say quack')

    def fly(self):
        print(f'Bird {self.name}: is flying')


# bird_one = Bird("Kesha", 3)
# bird_one.walk()
# bird_one.say()

# animal_one = Animal('Travis', 2)

# bird_one.fly()
# animal_one.fly()

class Penguin(Bird):

    def say(self):
        return f'{self.__class__.__name__} is trying to say something'

    def fly(self):
        raise TypeError
        # raise NotImplementedError # Will be implemented in the future


class KingPenguin(Penguin):
    def say(self):
        print(super(Bird, self).say())
        # return f'{self.__class__.__name__} is trying to say something'
    

# pengiun = KingPenguin('Howard', 4)
# pengiun.fly()
# print(pengiun.say())

# print(dir(pengiun))
# print(pengiun.__class__.__name__)

animal_one = Animal('Travis', 2)
animal_two = Animal("John", 3)
mammal_one = Mammal('Scot', 1)
bird_one = Bird("Kesha", 3)
pengiun = KingPenguin('Howard', 4)

animals = [animal_one, animal_two, mammal_one, bird_one, pengiun]
# for animal in animals:
#     animal.say()
#     animal.walk()

# animals = []
mammals = []
birds = []
penguins = []

# for animal in animals:
#     if type(animal) == Animal:
#         #....

# for animal in animals:
#     match 

# 'Hello', 'world'

# my_str = 'world!'
# match my_str:
#     case 'Hello':
#         print("It is hello!")
#     case 'world':
#         print("It is world!")
#     case _:
#         print('It is something different')

# Mammal()
for animal in animals:
    match animal:
        case Mammal():
            if animal not in mammals:
                mammals.append(animal)
        case Penguin():
            if animal not in mammals:
                penguins.append(animal)
        case Bird():
            if animal not in mammals:
                birds.append(animal)
        

print(birds)

print(isinstance(pengiun, Bird))
print(type(pengiun) == Bird)
