# Zad 4
# Pobieraj od użytkownika napis, dopóki jego długość nie będzie liczbą
# parzystą. Następnie zamień miejscami kolejne pary znaków, tak jak
# pokazano to w przykładzie: przed -> ABCDEF, po -> BADCFE. Wypisz
# zmodyfikowany napis.

import re


def get_user_string(message: str) -> str:
    while not (re.search('^[A-Za-z]+$', user_input := input(message)) and len(user_input) % 2 == 0):
        pass
    return user_input


def swap_letters(user_input: str) -> str:
    tmp = []
    for i in range(1, len(user_input), 2):
        tmp.extend([user_input[i], user_input[i - 1]])
    return ''.join(tmp)


def main() -> None:
    MESSAGE = 'Wprowadz tekst skladajacy sie z literek o parzystej dlugosci: '
    user_input = get_user_string(MESSAGE)
    print(swap_letters(user_input))


if __name__ == '__main__':
    main()
    print(chr(57344))