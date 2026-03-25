class Mammel:
    def walk(self):
        print('walk')


class Dog(Mammel):
    pass

class Cat(Mammel):
    pass


dog = Dog()
dog.walk()