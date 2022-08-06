# Wylosuj do zmiennej a liczbę z przedziału <1,20>. Pobieraj od
# użytkownika dwie liczby, dopóki ich średnia arytmetyczna nie będzie
# różniła się od wartości zmiennej a o mniej niż 2.

import random


def get_number_until_condition() -> (int, int):
    a = random.randint(1, 20)
    print(f'Rolled number is {a = }')
    while True:
        num1, num2 = int(input('Podaj pierwsza liczbe: ')), int(input('Podaj druga liczbe: '))
        m = (num1 + num2) / 2
        if abs(m - a) < 2:
            return num1, num2


if __name__ == '__main__':
    print(get_number_until_condition())
