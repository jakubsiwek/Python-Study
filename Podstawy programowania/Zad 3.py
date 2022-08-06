# Pobierz od użytkownika trzy liczby i zapisz je do zmiennych typu double
# o nazwach liczba1, liczba2, liczba3. Wyznacz średnią arytmetyczną
# największej i najmniejszej z pobranych liczb. Sprawdź, czy obliczona
# średnia jest większa od liczby środkowej (czyli nie największej i nie
# najmniejszej spośród trzech podanych).


def get_three_nums() -> [float, float, float]:
    num1 = float(input('Podaj pierwsza liczbe: '))
    num2 = float(input('Podaj druga liczbe: '))
    num3 = float(input('Podaj trzecia liczbe: '))
    return [num1, num2, num3]


def mean_max_min(lst: list) -> bool:
    max_val = max(lst)
    min_val = min(lst)
    max_min_mean = (min_val + max_val) / 2
    middle_index = (len(lst) - 1) // 2
    return True if max_min_mean > lst[middle_index] else False


if __name__ == '__main__':
    print('Mean value of min and max numbers is > than middle value' if mean_max_min(get_three_nums()) else
          'Mean value of min and max numbers is < than middle value')



