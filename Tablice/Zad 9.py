# Rozmiar tablicy losowany jest z przedziału <9, 33>. Losuj kolejne
# elementy tablicy z przedziału <2, 30> dopóki nie będą liczbą podzielną
# przez 3.

import random
from typing import List


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    return random.randint(min_range, max_range)


def my_generator(arr_size: int, min_range: int, max_range: int) -> List[int]:
    x = 0
    while x < arr_size:
        while not ((i := roll_number(min_range, max_range)) % 3 == 0):
            pass
        x += 1
        yield i


# def test(arr_size: int) -> List[int]:
#     a1 = []
#     x = 0
#     while x < arr_size:
#         while not ((i := roll_number(2, 30)) % 3 == 0):
#             pass
#         a1.append(i)
#         x += 1
#     return a1


def main() -> None:
    ARRAY_SIZE_MIN = 9
    ARRAY_SIZE_MAX = 33
    ARRAY_ELE_MIN = 2
    ARRAY_ELE_MAX = 30
    array_size = roll_number(ARRAY_SIZE_MIN, ARRAY_SIZE_MAX)
    a1 = [i for i in my_generator(array_size, ARRAY_ELE_MIN, ARRAY_ELE_MAX)]
    print(a1)


if __name__ == '__main__':
    main()