# Przygotuj dwie tablice kwadratowe dwuwymiarowe o tych samych wymiarach.
# Wykonaj ich dodawanie, odejmowanie, mnożenie tak samo jak robimy to w przypadku
# macierzy. Dodatkowo wykonaj dzielenie tablic, które polega na tym, że wszystkie
# elementy dzielnej dzielone są przez największy element dzielnika.


import random


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    return random.randint(min_range, max_range)


def divide_array(divisor: int, arr: []) -> []:
    tmp = [[round(arr[i][j] / divisor, 2) for j in range(len(arr))] for i in range(len(arr))]
    return tmp


def main() -> None:
    array_size = roll_number(2, 6)
    a1 = [[roll_number(1, 10) for i in range(array_size)] for i in range(array_size)]  # to bedzie dzielna
    a2 = [[roll_number(1, 10) for i in range(array_size)] for i in range(array_size)]  # a to dzielnik
    a3 = [[a1[i][j] + a2[i][j] for j in range(array_size)] for i in range(array_size)]  # Suma dwoch tablic
    a4 = [[a1[i][j] - a2[i][j] for j in range(array_size)] for i in range(array_size)]  # Roznica dwoch tablic
    print(list(max(i) for i in a1))
    print(f'Wylosowana tablica nr.1:',  a1)
    print(f'Wylosowana tablica nr.2:',  a2)
    print(f'Suma elementow tablic:',  a3)
    print(f'Roznica elementow tablic:',  a4)
    # a5 = [a1[i] + a2[i] for i in range(array_size)]  # Suma wierszow dwoch tablic
    # print(a5)


# Dodatkowo wykonaj dzielenie tablic, które polega na tym, że wszystkie
# elementy dzielnej dzielone są przez największy element dzielnika.

    max_value_from_array = max(max(i) for i in a2)

    a1 = divide_array(max_value_from_array, a1)
    print(f'Tablica nr.1 podzielona przez max element ({max_value_from_array}) z tablicy nr.2 to: {a1}')


if __name__ == '__main__':
    main()
    test = [[3213, 23312], [3, 32]]

