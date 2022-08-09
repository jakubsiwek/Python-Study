# Przygotuj dwie tablice kwadratowe dwuwymiarowe o tych samych wymiarach.
# Wykonaj ich dodawanie, odejmowanie, mnożenie tak samo jak robimy to w przypadku
# macierzy. Dodatkowo wykonaj dzielenie tablic, które polega na tym, że wszystkie
# elementy dzielnej dzielone są przez największy element dzielnika.

import random


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    return random.randint(min_range, max_range)


def generate_2d_array(size: int, min_value: int, max_value: int) -> [[int]]:
    return [[roll_number(min_value, max_value) for i in range(size)] for i in range(size)]


def add_two_2d_arrays(a1: [[int]], a2: [[int]]) -> [[int]]:
    return [list(map(lambda x, y: x + y, a1[i], a2[i])) for i in range(len(a1))]


def add_two_2d_arraysV2(a1: [[int]], a2: [[int]]) -> [[int]]:
    return [[a1[j][i] + a2[j][i] for i in range(len(a1))] for j in range(len(a1))]



def main() -> None:
    SIZE = roll_number(2, 3)
    a1 = generate_2d_array(SIZE, 0, 9)
    a2 = generate_2d_array(SIZE, 0, 9)
    print(a1)
    print(a2)
    print(add_two_2d_arrays(a1, a2))
    print(add_two_2d_arraysV2(a1, a2))


if __name__ == '__main__':
    main()
