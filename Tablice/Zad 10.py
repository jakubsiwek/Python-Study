# Rozmiar tablicy pobierany jest od użytkownika. Elementy tablicy są
# losowane z przedziału <a,b>. Liczby a i b to wartości typu int
# pobierane od użytkownika, dopóki nie będzie spełniony warunek a < b.
# Wypisz z tablicy wszystkie te elementy, które posiadają parzysty indeks
# i są podzielne przez wartość wyrażenia b – a

import re
import random


def get_array_size_from_user(message: str) -> int:

    while not re.search('^\d+$', user_input := input(message)):
        print('Podaj liczbe calkowita!')
    return int(user_input)


def roll_array_element(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    return random.randint(min_range, max_range)


def get_range_from_user() -> (int, int):
    while True:
        while not re.search('^\d+$', a := input('Podaj poczatek przedzialu (a): ')):
            print('Wprowadz liczbe calkowita!')
        while not re.search('^\d+$', b := input('Podaj poczatek przedzialu (b): ')):
            print('Wprowadz liczbe calkowita!')
        if a < b:
            return int(a), int(b)
        print('a ma byc mniejsze od b!')




def main() -> None:
    MESSAGE_1 = 'Podaj rozmiar tablicy: '
    arr_size = get_array_size_from_user(MESSAGE_1)
    a, b = get_range_from_user()
    a1 = [roll_array_element(a, b) for x in range(arr_size)]
    print('Wylosowana tablica to:', a1)

if __name__ == '__main__':
    main()