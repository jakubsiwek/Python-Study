# Pobierz od użytkownika napis i powiel w nim n razy wszystkie
# wystąpienia znaku podanego przez użytkownika, gdzie n to liczba pobrana
# przez użytkownika. Przykład:
# Wyraz: abecadlo, n = 3, znak od użytkownika = a wynik: aaabecaaadlo

from typing import Final


def get_user_string(message: str) -> str:
    while True:
        user_string = input(message)
        if user_string:
            return user_string
        print('Musisz wpisac zdanie ')


def get_user_char(message: str) -> str:
    while True:
        user_char = input(message)
        if user_char and len(user_char) == 1:
            return user_char
        print('Musisz podac jeden znak z klawiatury')


def get_user_num(message: str) -> int:
    while True:
        try:
            user_num = int(input(message))
            if user_num:
                return user_num
        except ValueError:
            print('Podaj liczbe! ')


def change_text(char: str, text: str, mul: int) -> str:
    return ''.join([x if x != char else x*mul for x in text])


def main() -> None:
    MESSAGE1: Final = 'Wpisz tekst: '
    MESSAGE2: Final = 'Wpisz cyfre: '
    MESSAGE3: Final = 'Wpisz literke, ktora ma zostac skopiowana: '
    text = get_user_string(MESSAGE1)
    number = get_user_num(MESSAGE2)
    char = get_user_char(MESSAGE3)
    print(change_text(char, text, number))


if __name__ == '__main__':
    main()
