# Elementy tablicy realizują pewną funkcję określoną wzorem f(x) = ax^2 + bx + c.
# Współczynniki a, b, c funkcji są ustalane losowo jako liczby z przedziału <0.3, 2.13>.
# Każdemu kolejnemu elementowi tablicy o indeksie i odpowiada wartość f(i), czyli
# wartość funkcji f(x) dla argumentu i. Przygotuj taką tablicę dla rozmiaru ustalonego
# wcześniej przez użytkownika i znajdź indeks największego elementu tablicy


import random
import re


def roll_number(min_value: float, max_value: float) -> float:
    return random.uniform(min_value, max_value)


def get_arr_size(message: str) -> int:
    while not (re.match('\d+', user_input := input(message))):
        print('Wpisz liczbe calkowita!')
    return int(user_input)


def generate_arr(a: float, b: float, c: float, size: int) -> list[float]:
    def count_value(a: float, b: float, c:float, x: int) -> float:
        return round(a * x ** 2 + b * x + c, 2)
    return [count_value(a,b,c,i) for i in range(size)]


def main() -> None:
    MIN_VALUE = 0.3
    MAX_VALUE = 2.13
    ARR_SIZE = get_arr_size('Wprowadz rozmiar tablicy, ktora bedzie przechowywac wartosci funkcji: ')
    A = roll_number(MIN_VALUE, MAX_VALUE)
    B = roll_number(MIN_VALUE, MAX_VALUE)
    C = roll_number(MIN_VALUE, MAX_VALUE)
    arr = generate_arr(A, B, C, ARR_SIZE)
    print('Generated arr:', arr)
    print(f'Index of max value => {arr.index(max(arr))}')

if __name__ == '__main__':
    main()
