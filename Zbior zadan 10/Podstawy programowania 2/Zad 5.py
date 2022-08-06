# Napisz program, który losuje liczbę z przedziału <30, 200>. Następnie pobieraj
# od użytkownika kolejne liczby całkowite tak długo, aż średnia wszystkich
# podanych liczb razem z liczbą wylosowaną nie dadzą średniej, która jest
# co najmniej o 20 mniejsza od liczby wylosowanej na początku.


import random


def get_number_from_user(message: str) -> int:
    try:
        return int(input(message))
    except ValueError:
        print('Nie podales numeru  ')


def roll_number() -> int:
    return random.randint(30, 200)


