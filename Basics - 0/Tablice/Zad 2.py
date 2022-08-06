# Wylosuj tablicę liczb całkowitych o elementach z przedziału <-30, 45>.
# Rozmiar tablicy jest losowany z przedziału <9, 20>. Każdy element,
# który jest liczbą ujemną zastąp wartością przeciwną do wartości tego
# elementu. Pozostałe elementy zastąp wartością odwrotną do wartości
# tych elementów. Wypisz na ekranie tak otrzymaną tablicę.

import random


def roll_number(min, max) -> int:
    if min > max:
        raise ValueError('Podana wartosc min jest wieksza od max')
    return random.randint(min, max)

print('Version 2')

print('Forgot')
def function_to_check_array(n) -> int:
    if n < 0:
        return abs(n)
    if n == 0:
        return n
    return 1/n


def main () -> None:
    MIN_1 = -30
    MAX_1 = 45
    MIN_2 = 9
    MAX_2 = 20
    array_size = roll_number(MIN_2, MAX_2)
    a1 = [roll_number(MIN_1, MAX_1) for x in range(array_size)]
    a2 = map(function_to_check_array, a1)
    result = list(a2)
    a3 = [round(float(x), 2) for x in result]  # Da sie w jakis lepszy sposob zaokraglic elementy?
    print('Wylosowane elementy to: ', end='')
    print(*a3, sep=', ')


if __name__ == '__main__':
    main()
