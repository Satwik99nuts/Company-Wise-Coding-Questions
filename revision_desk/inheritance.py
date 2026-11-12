class Animal:
    def make_sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def bark(self):
        print("dog barks")

dog = Dog()
dog.make_sound()
dog.bark()


