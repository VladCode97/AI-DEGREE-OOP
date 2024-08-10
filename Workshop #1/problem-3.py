#El programa genera un número aleatorio en un rango especifico y el usuario debe adivinarlo.
#Después de cada intento, el programa indica si el número a adivinar es mayor o menor que
#el ingresado por el usuario, hasta que acierte.

import random

def game_guest() -> None:
    guest_number: int = random.randint(0, 100)
    while(True):
        input_game: int = int(input('Ingrese un número para jugar: '))
        if(input_game == guest_number):
            print(f'Adivinaste el número. El número que adivinaste es {guest_number}')
            break
        elif(input_game < guest_number):
            print(f'El número que ingresas es menor al número que hay que adivinar')
        elif(input_game > guest_number):
            print(f'El número que ingresas es mayor al número que hay que adivinar')

game_guest()
