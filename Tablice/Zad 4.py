# Wylosuj tablicę liczb całkowitych o elementach z przedziału <10, 45>.
# Rozmiar tablicy jest losowany z przedziału <2, 40>. Pobieraj od
# użytkownika dwie liczby a i b – zmienne int, dopóki nie zajdzie relacja
# a < b. Wyznacz średnią arytmetyczną elementów tablicy o wartościach z
# przedziału <a,b>. Zwracamy ostatnia dobrze wpisana kombinacje
import random
import re


def get_numbers_until_condition() -> tuple[int, int]:
    prev_entered_range = (0, 1) # Dafault values
    while True:
        x = input('Podaj poczatek przedzialu:')
        y = input('Podaj koniec przedzialu:')
        if re.match('^\d+$', x) and re.match('^\d+$', y):
            if int(x) > int(y):
                return prev_entered_range
            prev_entered_range = int(x), int(y)
            continue
        print('Nie wpisales liczy!')


def generate_arr(min_arr_value: int, max_arr_value: int, min_size: int, max_size: int) -> list[int]:
    def roll_number(min_range: int, max_range: int) -> list[int]:
        return random.randint(min_range, max_range)
    arr_size = roll_number(min_size, max_size)
    arr = [roll_number(min_arr_value, max_arr_value) for i in range(arr_size)]
    print('Generated array:', arr)
    return arr


def count_mean_value_of_given_range(min_range: int, max_range: int, arr: list[int]) -> float:

    return sum([arr[i] for i in range(min_range, max_range)]) / (max_range - min_range)

def main() -> None:
    x, y = get_numbers_until_condition()
    min_arr_value = 10
    max_arr_value = 45
    min_size = 2
    max_size = 40
    arr = generate_arr(min_arr_value, max_arr_value, min_size, max_size)
    mean_value_of_range = count_mean_value_of_given_range(x, y, arr)
    print(f'Mean value from range <{x}, {y}> is equal: {mean_value_of_range}')


if __name__ == '__main__':
    main()