class Car:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok 

    def wyświetl_informacje(self):
        print(f"Samochód: {self.marka} {self.model}, rok: {self.rok}")