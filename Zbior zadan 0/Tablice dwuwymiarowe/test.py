# Przygotuj dwie tablice kwadratowe dwuwymiarowe o tych samych wymiarach.
# Wykonaj ich dodawanie, odejmowanie, mnożenie tak samo jak robimy to w przypadku
# macierzy. Dodatkowo wykonaj dzielenie tablic, które polega na tym, że wszystkie
# elementy dzielnej dzielone są przez największy element dzielnika.
import random


def roll_number(min_range: int, max_range: int) -> int:
    if min_range > max_range:
        raise ValueError('Min > max')
    return random.randint(min_range, max_range)


def generate_array(size: int, min_value: int, max_value: int) -> [[int]]:
    return [[roll_number(min_value, max_value) for i in range(size)] for j in range(size)]


def add_arrays(arr1: [[int]], arr2: [[int]]) -> [[int]]:
    a3 = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1))] for i in range(len(arr1))]
    return a3


def find_max_element_of_array(arr: [[int]]) -> int:
    return max([max(i) for i in arr])


def divide_array_by_a_factor(arr: [[int]], factor: int) -> [[int]]:
    divided_arr = [[arr[i][j] / factor for j in range(len(arr))] for i in range(len(arr))]
    return divided_arr


def main() -> None:
    SIZE = roll_number(2, 5)
    MIN_ELEMENT_VALUE = 0
    MAX_ELEMENT_VALUE = 9
    a1 = generate_array(SIZE, MIN_ELEMENT_VALUE, MAX_ELEMENT_VALUE)
    a2 = generate_array(SIZE, MIN_ELEMENT_VALUE, MAX_ELEMENT_VALUE)
    arrays_sum = add_arrays(a1, a2)
    print('Pierwsza wylosowana tablica to: ', a1)
    print('Druga wylosowana tablica to: ', a2)
    print(len(a2))
    print(f'Suma wylosowanych tablic to: {arrays_sum}')
    max_element_of_sec_arr = find_max_element_of_array(a2)
    print(f'Max element in second array is: {max_element_of_sec_arr}')
    print(divide_array_by_a_factor(a1, max_element_of_sec_arr))

if __name__ == '__main__':
    main()
