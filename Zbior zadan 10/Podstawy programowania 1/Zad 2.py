# Napisz program, w którym losowane są trzy liczby całkowite z przedziału
# <100, 999>. Z tak otrzymanych liczb utwórz liczbę trzycyfrową, której
# cyfry setek, dziesiątek i jedności to największe spośród odpowiednio
# cyfr setek, cyfr dziesiątek oraz cyfr jedności trzech wylosowanych
# liczb. Kiedy przykładowo wylosujesz liczby 123, 438, 918 wynikiem
# będzie liczba 938, ponieważ 9 to największa z cyfr setek, 3 to
# największa z cyfr dziesiątek oraz 8 to największa z cyfr jedności.


import random
from typing import Final


def roll_three_numbers(min_range: int, max_range:int) -> (int, int, int):
    if min_range > max_range:
        raise ValueError('Min range is > than max range')
    return random.randint(min_range, max_range), random.randint(min_range, max_range), random.randint(min_range, max_range)


def find_max_ones(roll_1: int, roll_2: int, roll_3: int) -> int:
    ones_1, ones_2, ones_3 = roll_1 % 10, roll_2 % 10, roll_3 % 10
    return max(ones_1, ones_2, ones_3)


def find_max_tens(roll_1: int, roll_2: int, roll_3: int) -> int:
    tens_1, tens_2, tens_3 = (roll_1 // 10) % 10, (roll_2 // 10) % 10, (roll_3 // 10) % 10
    return max(tens_1, tens_2, tens_3)


def find_max_hundreds(roll_1: int, roll_2: int, roll_3: int) -> int:
    hundreds_1, hundreds_2, hundreds_3 = (roll_1 // 100) % 10, (roll_2 // 100) % 10, (roll_3 // 100) % 10
    return max(hundreds_1, hundreds_2, hundreds_3)


def creat_numer(hundreds: int, tens: int, ones: int) -> int:
    return hundreds * 100 + tens * 10 + ones


def main() -> None:
    MIN_RANGE: Final = 100
    MAX_RANGE: Final = 999
    roll_1, roll_2, roll_3 = roll_three_numbers(MIN_RANGE, MAX_RANGE)
    print(f'Rolled values are: {roll_1, roll_2, roll_3}')
    max_ones = find_max_ones(roll_1, roll_2, roll_3)
    max_tens = find_max_tens(roll_1, roll_2, roll_3)
    max_hundreds = find_max_hundreds(roll_1, roll_2, roll_3)
    print(f'Num created of max ones, tens, hundreds is {creat_numer(max_hundreds, max_tens, max_ones)}')


if __name__ == '__main__':
    main()
