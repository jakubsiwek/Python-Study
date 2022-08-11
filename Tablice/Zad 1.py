# Zad 1
# Wylosuj tablicę liczb całkowitych o elementach z przedziału <10,30> i
# rozmiarze podanym przez użytkownika. Oblicz sumę tych elementów
# tablicy, które przy dzieleniu przez 5 dają resztę będącą liczbą
# parzystą. Wypisz na ekranie tak otrzymaną tablicę.

import random
import re


def roll_number(min_range: int = 10, max_range: int = 30) -> int:
    if min_range > max_range:
        raise ValueError('min > max')
    return random.randint(min_range, max_range)


def get_arr_size(message: str = 'Podaj rozmiar tablicy: ') -> int:
    while not re.match('^\d+$', user_input := input(message)):
        print('Wprowadz LICZBE!')
    return int(user_input)


def check_condition(arr: [int]) -> [int]:
    def condition(number: int) -> int:
        if number % 5 % 2 == 0:
            return True
        return False
    return list(filter(condition, arr))


def count_elements_condition_sum(arr: [int]) -> [int]:
    def condition(number: int) -> int:
        if number % 5 % 2 == 0:
            return True
        return False

    return sum(list(filter(condition, arr)))


def main() -> None:
    arr_size = get_arr_size()
    print(f'Rozmiar tablicy wynosi: {arr_size}')
    a1 = [roll_number() for i in range(arr_size)]
    print(f'Wylosowana tablica to: {a1}')
    print(f'Suma elementow, ktore przy dzieleniu przez 5 daja reszte parzystą wynosi: {count_elements_condition_sum(a1)}')


if __name__ == '__main__':
    main()
