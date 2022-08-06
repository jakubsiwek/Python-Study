# Przygotuj tablicę jednowymiarową liczb całkowitych. Wymiar tablicy
# jest losowany z przedziału <10, 100>. Każdy element tablicy ma wartość,
# którą losujemy z przedziału <100, 200> dopóki suma cyfr nie będzie
# liczbą posiadającą dokładnie dwa dzielniki, nie licząc 1 oraz tej
# liczby. Wyznacz sumę czterech największych elementów tablicy. Uwaga,
# kiedy w tablicy mamy przykładowo elementy: 1 1 1 2 2 2 3 3 4 4 5 5
# to cztery największe elementy przyjmujemy jako 5, 4, 3 oraz 2.


import math
import random


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    return random.randint(min_range, max_range)


def count_digits_sum(number: int) -> int:
    abs_number = abs(number)
    s = 0
    while abs_number > 0:
        s += abs_number % 10
        abs_number //= 10
    return s


def count_divisors(number: int) -> int:
    s = 0
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            if i ** 2 == number:
                s += 1
            else:
                s += 2
    return s


# def sortuj_przez_wybor(nums_set: {}) -> None:  # Sety nie mają indeksowania :/
#     for i in range(len(nums_set)):
#         min_index = i
#         for j in range(i+1, len(nums_set)):
#             if nums_set[j] < nums_set[min_index]:
#                 min_index = j
#         nums_set[i], nums_set[min_index] = nums_set[min_index], nums_set[i]


def find_4_biggest_elements(arr: [int]) -> [int, int, int, int]:
    nums_set = set(arr)
    sorted_set = sorted(nums_set)
    sorted_set_list = list(sorted_set)
    for i in range(4):
        match i:
            case 0:
                print(f'Najwiekszy element to: {sorted_set_list[len(sorted_set_list) - 1 - i]}')
            case 1:
                print(f'Drugi najwiekszy element to: {sorted_set_list[len(sorted_set_list) - 1 - i]}')
            case 2:
                print(f'Trzeci najwiekszy element to: {sorted_set_list[len(sorted_set_list) - 1 - i]}')
            case 3:
                print(f'Czwarty najwiekszy element to: {sorted_set_list[len(sorted_set_list) - 1 - i]}')


def roll_arr_element(min_range: int, max_range: int) -> int:
    while True:
        rolled_value = roll_number(min_range, max_range)
        if count_divisors(count_digits_sum(rolled_value)) == 2:
            return rolled_value


def main() -> None:
    MIN_ARRAY_SIZE = 10
    MAX_ARRAY_SIZE = 100
    MIN_VALUE = 100
    MAX_VALUE = 200
    arr_size = roll_number(MIN_ARRAY_SIZE, MAX_ARRAY_SIZE)
    a1 = [roll_arr_element(MIN_VALUE, MAX_VALUE) for i in range(arr_size)]
    print(a1)
    find_4_biggest_elements(a1)


if __name__ == '__main__':
    main()
