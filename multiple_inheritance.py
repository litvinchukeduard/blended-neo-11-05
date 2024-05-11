# Transport, Car, Boat, Amphibian

class Transport:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Car(Transport):
    def drive(self):
        print(f'{self.name} is driving')


class Boat(Transport):
    def sail(self):
        print(f'{self.name} is sailing')


class Amphibian(Car, Boat):
    pass


car = Car('Toyota', 'ab1234')
boat = Boat('Titanic', '1234566')
amphibian = Amphibian('Amphibian', '9876533')

transports = [car, boat, amphibian]

for transport in transports:
    print()
    try:
        transport.drive()
        transport.sail()
        transport.drive()
    except AttributeError:
        print('This transport can not do that!')

