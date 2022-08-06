# Pobierz od użytkownika rozmiar tablicy i utwórz tablicę elementów typu
# int. Elementy tablicy losujesz z przedziału <-10, 20>, jeżeli element
# tablicy znajduje się pod indeksem parzystym lub z przedziału <30,50>,
# jeżeli element tablicy znajduje się pod indeksem nieparzystym. Oblicz
# sumę elementów tablicy, które dzielą się przez indeks, pod którym się
# znajdują.

import random
import re


def get_arr_size(message: str) -> int:
    while not re.search('^\d+$', arr_size := input(message)):
        print('Podaj liczbe')
    return int(arr_size)


def get_arr_element(min_range: int, max_range: int) -> int:
    return random.randint(min_range, max_range)


def count_sum_elements_divided_by_index(arr: []) -> int:
    s = 0
    for i, y in enumerate(arr):
        if y % (i+1) == 0:  # zaczynamy od 1
            s += y
    return s


def main() -> None:
    MESSAGE_1 = 'Podaj rozmiar tablicy: '
    array_size = get_arr_size(MESSAGE_1)
    a1 = [get_arr_element(-10, 20) if i % 2 == 0 else get_arr_element(30, 50) for i in range(array_size)]
    print('Wylosowana tablica to: ', a1)
    el_sum_div_5 = count_sum_elements_divided_by_index(a1)
    print(f'Suma elementow podzielnych przez indexy na ktorych stoja to: {el_sum_div_5}')


if __name__ == '__main__':
    main()