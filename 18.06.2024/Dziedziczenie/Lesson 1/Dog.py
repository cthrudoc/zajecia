from Animal import Animal

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    def make_sound(self):
        print("Hau Hau")
    def info(self):
        super().info()
        print(f"I am a {self.name}")


my_dog = Dog("Bob" , "Yamnik")
my_dog.info()
my_dog.make_sound()