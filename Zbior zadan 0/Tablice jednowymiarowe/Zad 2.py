# Utwórz tablicę jednowymiarową o rozmiarze losowanym z przedziału <20, 40>.
# Elementy tablicy to kolejne elementy ciągu opisanego wzorem xn = x0 + 2∙r∙i. Wartości
# x0 oraz r są losowane z przedziału <1,5>, parametr i oznacza kolejny wyraz ciągu,
# zaczynamy od i = 1 i to będzie pierwszy element tablicy. Oblicz sumę elementów
# tablicy, które są podzielne przez 4.


import random
from functools import reduce


def roll_number(min_value: int, max_value: int) -> int:
    if min_value > max_value:
        raise ValueError('Min > max')
    return random.randint(min_value, max_value)


def generate_arr(size: int, r: int, x0: int) -> list[int]:
    def count_value(x: int) -> int:
        return x0 + 2 * r * x
    return [count_value(i) for i in range(1, size)]


def count_sum_of_elements_div_by_4(arr: list[int]) -> int:
    return sum([i for i in arr if i % 4 == 0])


def main() -> None:
    MIN_VALUE = 1
    MAX_VALUE = 6
    ARR_SIZE = roll_number(MIN_VALUE, MAX_VALUE)
    R, X0 = roll_number(1, 5), roll_number(1, 5)
    arr1 = generate_arr(ARR_SIZE, R, X0)
    print(arr1)
    print(count_sum_of_elements_div_by_4(arr1))


if __name__ == '__main__':
    main()
