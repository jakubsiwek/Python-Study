# Wylosuj tablicę liczb całkowitych o elementach z przedziału <10,30> i
# rozmiarze podanym przez użytkownika. Oblicz sumę tych elementów
# tablicy, które przy dzieleniu przez 5 dają resztę będącą liczbą
# parzystą. Wypisz na ekranie tak otrzymaną tablicę.

import random
import re


def roll_number(min: int, max: int) -> int:
    if min > max:
        raise ValueError('Wartosc poczatkowa jest wieksza od maksymalnej')
    return random.randint(min, max)


def get_user_number(message: str) -> int:
    while not re.search(r'^\d+$', user_input := input(message)):
        print('Podaj liczbe bez przecinków, kropek czy liter!')
    return int(user_input)


def main() -> None:
    MIN = 10
    MAX = 30
    MESSAGE = 'Podaj rozmiar tablicy: '
    array_size = get_user_number(MESSAGE)
    print(f'Wpisany rozmiar tablicy: {array_size}')
    a1 = [roll_number(MIN, MAX) for x in range(0, array_size)]
    print('Elementy tablicy: ', *a1, sep=', ')
    sum_of_elements = sum(x for x in a1 if x % 5 % 2 == 0)
    print(f'Suma elementow, ktore przy dzieleniu przez dwa daja wynik parzysty to: {sum_of_elements}')


if __name__ == '__main__':
    main()

