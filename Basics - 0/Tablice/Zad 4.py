# Wylosuj tablicę liczb całkowitych o elementach z przedziału <10, 45>.
# Rozmiar tablicy jest losowany z przedziału <2, 40>. Pobieraj od
# użytkownika dwie liczby a i b – zmienne int, dopóki nie zajdzie relacja
# a < b. Wyznacz średnią arytmetyczną elementów tablicy o wartościach z
# przedziału <a,b>.

import random
import re


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min jest wiekszy od max')
    return random.randint(min_range, max_range)


def get_user_values(arr):
    while True:
        if re.search('^\d+$', a := input('Podaj pierwsza liczbe: ')) and re.search('^\d+$', b := input('Podaj druga liczbe: ')):
            if int(a) < int(b) < len(arr):
                return int(a), int(b)
        print(f'Pierwsza wpisana wartosc musi byc mniejsza niz druga + obie musza byc liczbami calkowitymi, '
              f'i mniejszymi od {len(arr)}')


def main() -> None:
    MIN_1, MAX_1 = 2, 40
    array_size = roll_number(MIN_1, MAX_1)
    MIN_2, MAX_2 = 10, 45
    a1 = [roll_number(MIN_2, MAX_2) for x in range(array_size)]
    print(f'Wylosowana tablica to: {a1}')
    a, b = get_user_values(a1)
    array_range_mean = sum(a1[a:b+1]) / (b - a + 1)
    print(f'Obliczona srednia wynosi: {array_range_mean}')


if __name__ == '__main__':
    main()
