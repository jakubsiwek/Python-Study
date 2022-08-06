# Pobieraj od użytkownika napis, dopóki nie będzie zawierał poprawnie
# zapisanej liczby. Zakładamy, że poprawnie zapisana liczba to taka, do
# której zapisu użyto „zwykłego” zapisu lub notacji naukowej. Przykłady
# poprawnie zapisanych liczb: 2.4, -12.45, 10E12, -5.45E9, 8E-3,
# 23.34e10, 24.3e-5.

import re


def get_number(message: str) -> str:
    while True:
        while re.search(r'^(-?\d+|-?\d+\.+\d+|\d+\.\d+e-?\d+)$', text := input(message)):
            print('Zle wpisana liczba')
        return text

print('d')
def main() -> None:
    MESSAGE = 'Podaj liczbe: '
    get_number(MESSAGE)


if __name__ == '__main__':
    main()
