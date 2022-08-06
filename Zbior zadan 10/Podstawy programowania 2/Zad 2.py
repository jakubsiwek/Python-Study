#  Napisz program, który losuje dwie liczby całkowite z przedziału
# <10, 35>, dopóki suma cyfry jedności pierwszej wylosowanej liczby oraz
# cyfry dziesiątek drugiej wylosowanej liczby nie będzie liczbą pierwszą
# większą od 5.

import random
import math


def roll_two_random_numbers() -> (int, int):
    number_1 = random.randint(10, 35)
    number_2 = random.randint(10, 35)
    return number_1, number_2


def is_prime_number(num: int) -> bool:
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    return False


def check_conditions() -> None:
    while True:
        number_1, number_2 = roll_two_random_numbers()
        digits_number_1 = number_1 % 10
        tens_number_2 = (number_2 // 10) % 10
        s = digits_number_1 + tens_number_2
        if is_prime_number(s) and s > 5:
            print(number_1, number_2)
            break


if __name__ == '__main__':
    check_conditions()
