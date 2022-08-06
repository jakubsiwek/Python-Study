# Napisz program, w którym losujesz dwie liczby całkowite z przedziału
# <30, 100>. Wyznacz liczbę o większej ilości nieparzystych dzielników
# (nie traktuj jako dzielniki liczby 1 oraz liczby badanej).

import math
import random


def roll_two_numbers() -> (int, int):
    return random.randint(30, 100), random.randint(30, 100)


def odd_divisors_counter(number: int) -> int:
    ev_count = 0
    od_count = 0
    for i in range(1, int(pow(number, 1 / 2)) + 1):
        if number % i == 0:
            if i == number / i:
                if i % 2 == 0:
                    ev_count += 1
                else:
                    od_count += 1

            else:
                if i % 2 == 0:
                    ev_count += 1
                else:
                    od_count += 1
                if (number / i) % 2 == 0:
                    ev_count += 1
                else:

                    od_count += 1

    return od_count


def check_odd_divisors(roll_1: int, roll_2: int) -> int:
    return roll_1 if odd_divisors_counter(roll_1) > odd_divisors_counter(roll_2) else roll_2

def main() -> None:
    rolled_number_1, rolled_number_2 = roll_two_numbers()
    print(f'Rolled values are: {rolled_number_1} and {rolled_number_2}')
    print(f'Number with more odd divisors is {check_odd_divisors(rolled_number_1, rolled_number_2)}')


if __name__ == '__main__':
    main()