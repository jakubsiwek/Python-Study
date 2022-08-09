# Przygotuj tablicę dwuwymiarową kwadratową o wymiarze i elementach losowanych z
# przedziału <2.3, 10.11>. Dokonaj przekształcenia tablicy, które polega na podzieleniu
# każdego elementu tablicy przez element na przekątnej znajdujący się w tym samym
# wierszu. Następnie wyznacz kolumnę o największej sumie elementów oraz wiersz o
# najmniejszym iloczynie elementów. Dla tak wyznaczonych kolumny i wiersza oblicz
# odchylenie standardowe ich elementów.

import random


def roll_number(min_range: int, max_range: int) -> float:
    if min_range > max_range:
        raise ValueError('Min > max')
    return random.uniform(min_range, max_range)


def count_column_sum(arr: []) -> []:
    sum_column = 0
    a2 = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            sum_column += arr[j][i]
        a2.append(round(sum_column, 2))
        sum_column = 0
    return a2


def main() -> None:
    MIN_RANGE = 2
    MAX_RANGE = 10
    array_size = 3
    a1 = [[roll_number(MIN_RANGE, MAX_RANGE) for j in range(array_size)] for i in range(array_size)]
    print(f'Wylosowana tablica to: ', a1)
    a1 = [[round(a1[i][j]/a1[i][i], 2) for j in range(array_size)] for i in range(array_size)]
    print(f'Tablica po podzieleniu: ', a1)
    a2 = count_column_sum(a1)  # sumy kolumn
    print('Sumy poszczegolnych kolumn tablicy po podzieleniu wynosza:', a2)
    print(f'Kolumna o najwiekszej sumie elementow ma numer: {a2.index(max(a2))}')
    print(f'Wiersz o najmniejszym iloczynie elementow ma numer: {a1.index(min(i for i in a1))}')


if __name__ == '__main__':
    main()