# Pobierz od użytkownika rozmiar oraz wygeneruj elementy tablicy typu int z przedzialu 1-100
# . Oblicz,
# ile w tablicy jest elementów, które są dzielnikami liczby, którą
# wcześniej wylosujesz z przedziału <5, 1000>.
import random
import re


def get_arr_size(message: str) -> int:
    while not re.match('\d+', user_size := input(message)):
        print('Wpisz liczbe calkowita!')
    return int(user_size)


def roll_number(min_range: int, max_range: int) -> int:
    return random.randint(min_range, max_range)


def gen_arr(size: int, min_value: int, max_value: int) -> list[int]:
    return [roll_number(min_value, max_value) for i in range(size)]


def count_divisible_numbers(arr: list[int], rolled_number: int) -> int:
    counter = 0
    for number in arr:
        if rolled_number % number == 0:
            counter += 1
    return counter


def main() -> None:
    dividend = roll_number(5, 1000)
    arr_size = get_arr_size('Wprowadz rozmiar tablicy losowanych liczb: ')
    min_arr_value = 1
    max_arr_value = 100
    arr = gen_arr(arr_size, min_arr_value, max_arr_value)
    print(count_divisible_numbers(arr, dividend))


if __name__ == '__main__':
    main()