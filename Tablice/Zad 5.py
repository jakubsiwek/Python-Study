# Pobierz od użytkownika rozmiar oraz elementy tablicy typu int. Oblicz,
# ile w tablicy jest elementów, które są dzielnikami liczby, którą
# wcześniej wylosujesz z przedziału <5, 100>.

import random
import re

def roll_number(min: int, max: int) -> int:
    return random.randint(min, max)


def get_array_size(message: str) -> int:
    while not re.search('^\d+$', user_input := input(message)):
        print('Podaj liczbe calkowita! :) ')
    return int(user_input)


def get_array_element(message: str) -> int:
    while not re.search('^\d+$', user_input := input(message)):
        print('Podaj liczbe calkowita! :) ')
    return int(user_input)


def count_divisors(arr: []) -> int:
    print(x := roll_number(5, 100))
    a2 = [i for i in arr if x % i == 0]
    return len(a2)


def main() -> None:
    MESSAGE_1 = 'Podaj rozmiar tablicy: '
    arr_size = get_array_size(MESSAGE_1)
    MESSAGE_2 = 'Podaj element tablicy: '
    a1 = [get_array_size(MESSAGE_2) for x in range(arr_size)]
    print(a1)
    print(count := count_divisors(a1))

if __name__ == '__main__':
    main()