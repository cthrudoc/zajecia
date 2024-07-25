class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Some generic sound")
    def info(self):
        print(f"I am a {self.name} and my species is {self.species}.")