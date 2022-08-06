# 3. Napisz program, który losuje 10 liczb całkowitych.
# Liczby muszą być z przedziału <10, 99>. Każda kolejna pobierana liczba
# musi mieć cyfrę dziesiątek taką samą jak cyfra jedności poprzednio
# pobranej liczby. Kiedy cyfra jedności poprzednio pobranej liczby była
# równa zero, wtedy pobierana liczba może posiadać dowolną cyfrę
# dziesiątek. Pierwsza pobierana liczba jest dowolną liczbą dwucyfrową.
# Oblicz spośród pobranych liczb sumę tych, których cyfra jedności wynosi
# zero. Nie stosujemy tablic.

from typing import Final
import random

def draw_int_number(min_range: int, max_range: int) -> int:
    return random.randint(min_range, max_range)


def draw_numbers(min_range: int, max_range: int, n: int) -> int:

    def digit_at_position(n: int, pos: int) -> int:
        if pos < 0:
            raise ValueError('Position is out of range')
        n_abs = abs(n)
        return (n_abs // 10 ** pos) % 10

    def check_numbers(n1: int, n2: int) -> bool:
        u = digit_at_position(n1, 0)
        return u == 0 or u == digit_at_position(n2, 1)

    if min_range >= max_range:
        raise ValueError('Range is not correct')

    if n <= 0:
        raise ValueError('Number of items must be positive')

    prev_number = draw_int_number(min_range, max_range)
    print(f'Number = {prev_number}')
    s = 0

    if digit_at_position(prev_number, 0) == 0:
        s += prev_number

    for _ in range(1, n):
        while not check_numbers(prev_number, n := draw_int_number(min_range, max_range)):
            pass

        if digit_at_position(n, 0) == 0:
            s += n

        prev_number = n
        print(f'Number = {prev_number}')

    return s


def main() -> None:
    MIN_RANGE: Final = 10
    MAX_RANGE: Final = 99
    N: Final = 10

    s = draw_numbers(MIN_RANGE, MAX_RANGE, N)
    print(f'SUMA = {s}')

main()