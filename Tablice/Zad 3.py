# Z elementów tablicy typu double o rozmiarze i wartościach pobranych
# od użytkownika wyznacz średnią arytmetyczną, którą następnie pomnóż
# razy dwa. Tak otrzymany wynik zapisz do zmiennej x. Wszystkie elementy
# tablicy zwiększ o 10% wartości zmiennej x.

import re


def get_array_size(message: str) -> int:
    while not (re.search('^\d+$', user_input := input(message))):
        print('Podaj liczbe calkowita! ')
    return int(user_input)


def get_double_from_user(message: str) -> float:
    while not (re.search('^\d+\.?\d*$', user_input := input(message))):
        print('Podaj liczbe z kropka. ')
    return float(user_input)


def array_mean(arr: []) -> int:
    return round(sum(arr) / len(arr), 2)


def main() -> None:
    MESSAGE_1 = 'Podaj rozmiar tablicy: '
    arr_size = get_array_size(MESSAGE_1)
    MESSAGE_2 = 'Podaj element tablicy: '
    a1 = [get_double_from_user(MESSAGE_2) for x in range(arr_size)]
    print('Wygenerowana tablica to: ', end='')
    print(*a1, sep=', ')
    arr_mean_val = array_mean(a1)
    print(f'Srednia wartosc elementow tablicy wynosi: {arr_mean_val}')
    a1 = list(map(lambda x: round(x + 0.1*x, 1), a1))
    print(a1)


if __name__ == '__main__':
    main()
