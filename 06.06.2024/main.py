from car import Car
import json

with open("06.06.2024/car.json", "r") as file:
    data = json.load(file)

samochody = [] 

for car_id, car_info in data.items():
    samochody.append(Car(car_info["marka"],car_info["model"],car_info["rok"]))

for Car in samochody:
    Car.wyświetl_informacje()