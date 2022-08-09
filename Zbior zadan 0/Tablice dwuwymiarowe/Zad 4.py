# Przygotuj dwie tablice dwuwymiarowe o takich samych wymiarach pobranych od
# użytkownika oraz o elementach losowanych z przedziału <-12, 34>. Elementy w
# każdym wierszu losujesz dotąd dopóki w wierszach o numerach nieparzystych
# znajdować się będą elementy tylko ujemne, a w wierszach o numerach parzystych
# elementy tylko dodatnie. Następnie utwórz trzecią tablicę, której kolejne wiersze będą
# wierszami albo z tablicy pierwszej, albo z tablicy drugiej w zależności od tego który
# wiersz będzie miał większą sumę elementów.

import random
import re


def roll_positive_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    while True:
        x = random.randint(min_range, max_range)
        if x >= 0:
            return x


def roll_negative_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    while True:
        x = random.randint(min_range, max_range)
        if x < 0:
            return x


def get_user_number() -> int:
    while not re.search('^[2-4]$', user_input := input('Wprowadz rozmiar tablicy dwuwymiarowej: : ')):
        print('Wprowadz liczbe calkowita, ktora jest z przedzialu 2-4!')
    return int(user_input)


def third_array(arr1: [], arr2: []) -> []:
    tmp = [arr1[i] if sum(arr1[i]) > sum(arr2[i]) else arr2[i] for i in range(len(arr1))]
    return tmp


def main() -> None:
    MIN_ROLL_RANGE = -12
    MAX_ROLL_RANGE = 34
    array_size = get_user_number()
    a1 = [[roll_positive_number(MIN_ROLL_RANGE, MAX_ROLL_RANGE) for i in range(array_size)] if j % 2 == 0
          else [roll_negative_number(MIN_ROLL_RANGE, MAX_ROLL_RANGE) for i in range(array_size)]
          for j in range(array_size)]
    print(f'Pierwsza wylosowana tablica to: {a1}')
    a2 = [[roll_positive_number(MIN_ROLL_RANGE, MAX_ROLL_RANGE) for i in range(array_size)] if j % 2 == 0
          else [roll_negative_number(MIN_ROLL_RANGE, MAX_ROLL_RANGE) for i in range(array_size)]
          for j in range(array_size)]
    print(f'Druga wylosowana tablica to: {a2}')
    a3 = third_array(a1, a2)
    print(f'Trzecia utworzona tablica to: {a3}')


if __name__ == '__main__':
    main()
