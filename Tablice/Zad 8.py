# Rozmiar tablicy losowany jest z przedziału <4, 10>. Pobieraj od
# użytkownika elementy tablicy dotąd, dopóki każdy kolejny element
# tablicy, począwszy od drugiego, nie będzie większy od elementu
# poprzedniego. Wypisz elementy otrzymanej tablicy.


import random
import re
from typing import List


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    return random.randint(min_range, max_range)


def get_user_number(number: int) -> int:
    while not re.search('^\d+$', user_input := input(f'Podaj {number} element tablicy: ')):
        print('Wpisz liczbe calkowita! ')
    return int(user_input)


def fill_array(arr: List[int], size: int) -> List[int]:
    prev_input = 0
    for i in range(size):
        if i == 0 or i == 1:
            x = get_user_number(i)
            arr.append(x)
            prev_input = x
        if i > 1:
            while not (x := get_user_number(i)) > prev_input:
                print(f'Podaj wieksza liczbe niz: {prev_input}')
            arr.append(x)
            prev_input = x


def main() -> None:
    MIN_RANGE = 4
    MAX_RANGE = 10
    arr_size = roll_number(MIN_RANGE, MAX_RANGE)
    a1 = []
    print(f'Wylosowany rozmiar tablicy to: {arr_size}')
    fill_array(a1, arr_size)
    print(a1)

if __name__ == '__main__':
    main()