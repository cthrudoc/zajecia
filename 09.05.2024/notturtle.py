from turtle import Turtle, Screen # importujemy potrzebne biblioteki
import random

t = Turtle() # tworzymy obiekt turtle
t.speed(1) # funkcja speed ustala szybkość żółwia
screen = Screen() # nie wiem xd

for _ in range(4): # nakazuje powtórzyć 4 razy poniższe komendy aby narysować kwadrat
    t.forward(100) # nakazuje narysować linię na 100 pixeli
    t.right(90) # nakazuje odwrócić się o 90 stopni

screen.exitonclick() # zamykanie programu na kliknięcie