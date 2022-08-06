# Napisz program, który losuje trzy liczby całkowite z przedziału
# <30, 100>, dopóki suma cyfr najmniejszej liczby nie będzie taka sama
# jak suma cyfr liczby największej.

import random


def roll_three_numbers() -> (int, int, int):
    return random.randint(30, 100), random.randint(30, 100), random.randint(30, 100)


def count_digits_sum(num: int) -> int:
    s = 0
    digit = 0
    abs_num = abs(num)
    while abs_num > 0:
        digit = abs_num % 10
        s += digit
        abs_num //= 10
    return s


def check_condition() -> None:
    while True:
        numbers = roll_three_numbers()
        if count_digits_sum(max(numbers)) == count_digits_sum(min(numbers)):
            print(numbers)
            break


if __name__ == '__main__':
    check_condition()



