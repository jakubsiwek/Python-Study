# Utwórz tablicę jednowymiarową o rozmiarze pobranym od użytkownika. Tablicę
# wypełniamy w następujący sposób: jeżeli indeks elementu jest podzielny przez 3
# wartość elementu pod tym indeksem losujemy z przedziału <101,203>, jeżeli indeks
# elementu przy dzieleniu przez 3 daje resztę 1 wartość elementu pod tym indeksem
# wyznaczamy jako dwukrotną wartość elementu na poprzedniej pozycji. Pozostałe
# elementy mają wartość zero. Dla tak wypełnionej tablicy wyznacz średnią
# arytmetyczną tych elementów, których cyfra jedności jest większa od cyfry setek.

import re
import random


def check_if_ones_bigger_than_tens(number: int) -> bool:
    ones = number % 10
    tens = (number // 10) % 10
    return True if ones > tens else False


def count_mean_value(arr: [int]) -> int:
    return sum([i for i in arr if check_if_ones_bigger_than_tens(i)]) / len(arr)


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('min > max')
    return random.randint(min_range, max_range)


def get_arr_size(message: str) -> int:
    while not re.match('\d+', user_input := input(message)):
        print('Musisz wprowadzic numer!')
    return int(user_input)


def generate_array(arr_size: int, min_value: int = 101, max_value: int = 203) -> [int]:
    tmp = [roll_number(min_value, max_value) if i % 3 == 0 else 0 for i in range(arr_size)]
    print(tmp)
    return [tmp[i - 1] * 2 if i % 3 == 1 else tmp[i] for i in range(len(tmp))]


def main() -> None:
    arr_size = get_arr_size('Wprowadz rozmiar tablicy:')
    a1 = generate_array(arr_size)
    print(a1)
    print(count_mean_value(a1))



if __name__ == '__main__':
    main()