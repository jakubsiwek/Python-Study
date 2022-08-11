# Wylosuj tablicę liczb całkowitych o elementach z przedziału <-30, 45>.
# Rozmiar tablicy jest losowany z przedziału <9, 20>. Każdy element,
# który jest liczbą ujemną zastąp wartością przeciwną do wartości tego
# elementu. Pozostałe elementy zastąp wartością odwrotną do wartości
# tych elementów. Wypisz na ekranie tak otrzymaną tablicę.

import random


def generate_array() -> list[int]:

    def roll_number(min_value: int, max_value: int) -> int:
        return random.randint(min_value, max_value)

    size = roll_number(9, 20)
    min_value = -30
    max_value = 45
    return [roll_number(min_value, max_value) for i in range(size)]


def edit_array(arr: list[int]) -> None:
    print([abs(element) if element < 0 else round(1 / element, 2) for element in arr])


def main() -> None:
    arr1 = generate_array()
    print(arr1)
    edit_array(arr1)


if __name__ == '__main__':
    main()