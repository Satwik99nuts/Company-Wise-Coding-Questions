class Animal:
    def make_sound(self):
        print("The animal makes a sound")
class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

my_animal = Animal()
my_dog = Dog()

my_animal.make_sound()
my_dog.make_sound()