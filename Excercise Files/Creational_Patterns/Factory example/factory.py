""""It is a simplification of the Abstract Factory,
in which the abstract class has concrete methods that use
 some of the abstract ones; as we use one or another daughter of this abstract class.
  Programmer: Jesús Eduardo Rico Sandoval"""


class Dog:
    """"A single dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    """"A single dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """"The factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
