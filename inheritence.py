class Mammel:
    def walk(self):
        print('walk')


class Dog(Mammel):
    def balk(self):
        print('balk')
    pass

class Cat(Mammel):
    def be_annoying(self):
        print('be_annoying')
    pass
    pass


dog = Dog()
dog.walk()
dog.balk()


cat = Cat()
cat.walk()
#cat.balk() # this wont work since this is part of Dog