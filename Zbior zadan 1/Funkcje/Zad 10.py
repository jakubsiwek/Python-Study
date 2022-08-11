# Funkcja przyjmuje jako argument dwie tablice elementów typu int o
# dowolnych rozmiarach i zwraca największy element tablicy, której
# średnia arytmetyczna jest większa.


def count_arr_mean_value(arr: list[int]) -> float:
    return round(sum(arr) / len(arr), 2)


def find_max_ele(arr1: list[int], arr2: list[int]) -> int:
    return max(arr1) if count_arr_mean_value(arr1) > count_arr_mean_value(arr2) else max(arr2)


arr1 = [1, 2, 3, 4, 5]
arr2 = [31, 31, 32, 99, 923]

print(find_max_ele(arr1, arr2))
