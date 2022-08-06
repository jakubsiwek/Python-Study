# Wylosuj liczbę z przedziału <-50, 50> i zapisz ją w zmiennej typu
# całkowitoliczbowego o nazwie x. Zbadaj, w którym z wymienionych
# przedziałów znajduje się wylosowana liczba: <-∞, -40), <-40, -20),
# <-20, 20>, (20, ∞).

import random
from typing import Final


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min range is > than max range')
    return random.randint(min_range, max_range)


def check_range(rolled_value: int) -> int:
    match rolled_value:
        case rolled_value if rolled_value < -40:
            return 1
        case rolled_value if -40 <= rolled_value < -20:
            return 2
        case rolled_value if -20 <= rolled_value <= 20:
            return 3
        case rolled_value if 20 < rolled_value :
            return 4


def menu(range_value: int) -> None:
    if range_value == 1:
        print('Rolled value is in range (-∞, -40)')
    elif range_value == 2:
        print('Rolled value is in range <-40, -20)')
    elif range_value == 3:
        print('Rolled value is in range <-20, 20>')
    elif range_value == 4:
        print('Rolled value is in range (20, ∞)')
    else:
        raise ValueError('Range value is not correct')


def main():
    MIN_RANGE: Final = -50
    MAX_RANGE: Final = 50
    print(rolled_num := roll_number(MIN_RANGE, MAX_RANGE))
    menu(check_range(rolled_num))


if __name__ == '__main__':
    main()
