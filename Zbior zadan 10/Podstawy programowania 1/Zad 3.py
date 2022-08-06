# Napisz program, w którym losowane są trzy liczby całkowite z przedziału
# <10, 100>, dopóki ich suma nie będzie większa od trzykrotności liczby
# środkowej (czyli drugiej co do wielkości spośród trzech podanych).


import random
from typing import Final


def roll_number(min_range: int, max_range: int) -> int:
    if max_range < min_range:
        raise ValueError('Min range is > than max range value')
    return random.randint(min_range, max_range)


def mid_value(roll_1: int, roll_2: int, roll_3: int) -> int:
    if roll_1 <= roll_2 <= roll_3 or roll_3 <= roll_2 <= roll_1:
        return roll_2
    elif roll_2 <= roll_1 <= roll_3 or roll_3 <= roll_1 <= roll_2:
        return roll_1
    return roll_3


def check_sum(range_min: int, range_max: int) -> (int, int, int):
    while ((roll_1 := roll_number(range_min, range_max)) + (roll_2 := roll_number(range_min, range_max)) + (roll_3 := roll_number(range_min, range_max))) < (3 * mid_value(roll_1, roll_2, roll_3)):
        pass
    print(f'Mid value times 3 is equal: {mid_value(roll_1, roll_2, roll_3) * 3}')
    return roll_1, roll_2, roll_3


def main() -> None:
    MIN_RANGE: Final = 10
    MAX_RANGE: Final = 100
    print(f'Rolled numbers which sum is higher than mid value times 3 is: {check_sum(MIN_RANGE, MAX_RANGE)}')


if __name__ == '__main__':
    main()

