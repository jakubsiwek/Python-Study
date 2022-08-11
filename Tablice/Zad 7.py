# Zad 7
# Rozmiar oraz elementy tablicy są losowane z przedziału <10,30>. Wypisz
# te elementy tablicy, które przy dzieleniu przez 5 dają resztę, która
# jest mniejsza od ostatniej cyfry dzielonego elementu tablicy.
import random


def roll_number(min_range: int, max_range: int) -> int:
    return random.randint(min_range, max_range)


def find_elements(arr: list[int]) -> list[int]:
    return [i for i in arr if (i % 5 < i % 10)]


def main() -> None:
    arr_size = roll_number(10, 30)
    arr = [roll_number(10, 30) for i in range(arr_size)]
    print('Generated array:', arr)
    found_elements = find_elements(arr)
    print('Found elements:', found_elements)


if __name__ == '__main__':
    main()