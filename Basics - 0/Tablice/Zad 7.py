# Rozmiar oraz elementy tablicy są losowane z przedziału <10,30>. Wypisz
# te elementy tablicy, które przy dzieleniu przez 5 dają resztę, która
# jest mniejsza od ostatniej cyfry dzielonego elementu tablicy.

import random


def roll_number(min_range, max_range) -> int:
    if min_range > max_range:
        raise ValueError('Min jest wiekszy od max')
    return random.randint(min_range, max_range)


def validate(arr: []) -> []:
    array = [i for i in arr if i % 5 < i % 10]
    return array


def main() -> None:
    MIN_RANGE = 10
    MAX_RANGE = 30
    array_size = roll_number(MIN_RANGE, MAX_RANGE)
    a1 = [roll_number(MIN_RANGE, MAX_RANGE) for i in range(array_size)]
    print(a1)
    a2 = validate(a1)
    print(a2)


if __name__ == '__main__':
    main()