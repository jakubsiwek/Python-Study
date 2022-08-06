# Napisz program, w którym wygenerujesz tablicę jednowymiarową liczb
# całkowitych. Rozmiar tablicy losowany jest z przedziału <10, 40>.
# Elementy tablicy losowane są z przedziału < 30, 50>. Wyznacz indeksy
# tych dwóch elementów tablicy, pomiędzy którymi występuje najmniejsza
# różnica. Wygeneruj nową tablicę, w której ‘przesuniesz’ dwa wyznaczone
# elementy na koniec tablicy.

import random
import re


def generate_array(min_range_arr: int, max_range_arr: int, min_value: int, max_value: int) -> []:

    def generate_number(min_range_arr: int, max_range_arr: int) -> int:
        return random.randint(min_range_arr, max_range_arr)

    return [generate_number(min_value, max_value) for i in range(generate_number(min_range_arr, max_range_arr))]


def find_two_elements(array: []) -> []:
    tmp2 = ['', 100]
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if abs(array[i] - array[j]) < tmp2[1]:
                tmp2[1] = abs(array[i] - array[j])
                tmp2[0] = f'{i}, {j}'  # indeksy tych dwoch elementow, ktorych roznica jest najmniejsza
    # print(tmp2)
    print(f'Indeksy o najmniejszej różnicy to: ' + tmp2[0] + ' a ich roznica wynosi: ' + str(tmp2[1]))
    tmp = re.findall('\d', tmp2[0])  # biore indeksy z tmp2[0]
    tmp[0], tmp[1] = array[int(tmp[0])], array[int(tmp[1])]  # zapisuje elementy tablicy do przesuniecia na poczatek
    array.remove(tmp[0]), array.remove(tmp[1])
    array.append(tmp[0]), array.append(tmp[1])


def main() -> None:
    a1 = generate_array(5, 7, 30, 50)
    print(a1)
    find_two_elements(a1)
    print(a1)


if __name__ == '__main__':
    main()