# Zad 7
# Pobieraj od użytkownika liczby, dopóki nie poda on liczby większej od
# 100. Wyznacz spośród podanych liczb liczbę o największej sumie cyfr.

from typing import Final


def get_number(message: str) -> int:
    return int(input(message))


def digits_sum(number: int) -> int:
    number_abs = abs(number)
    s = 0
    while number_abs > 0:
        s += number_abs % 10
        number_abs //= 10
    return s


def get_numbers_until_condition(limit: int) -> int:
    max_digits_sum = 0
    new_digits_sum = 0
    max_number = 0
    while True:
        num = get_number('Enter number: ')
        if num > limit:
            return max_number
        new_digits_sum = digits_sum(num)
        if new_digits_sum > max_digits_sum:
            max_digits_sum = new_digits_sum
            max_number = num


def main() -> None:
    LIMIT: Final = 100
    n = get_numbers_until_condition(LIMIT)
    print(f'{n = }')


if __name__ == '__main__':
    main()