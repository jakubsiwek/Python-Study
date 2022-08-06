# Wylosuj trzy liczby z przedziału odpowiednio <0, 10>, <-13, 23>,
# <34, 87>. Oblicz średnią arytmetyczną wyznaczonych liczb i wypisz tą
# liczbę spośród losowanych wcześniej, która ma wartość najbliżej
# obliczonej średniej.

import random


def find_closest_number_to_mean() -> int:

    def roll_three_numbers() -> (int, int, int):
        return random.randint(0, 10), random.randint(-13, 23), random.randint(34, 87)

    list1 = list(roll_three_numbers())
    mean = sum(list1) / len(list1)
    lst = [abs(list1[0] - mean), abs(list1[1] - mean), abs(list1[2] - mean)]
    return list1[lst.index(min(lst))]


if __name__ == '__main__':
    print(find_closest_number_to_mean())
    