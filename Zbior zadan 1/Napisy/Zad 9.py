# Pobierz od użytkownika napis i powiel w nim n razy wszystkie
# wystąpienia znaku podanego przez użytkownika, gdzie n to liczba pobrana
# przez użytkownika. Przykład:
# Wyraz: abecadlo, n = 3, znak od użytkownika = a wynik: aaabecaaadlo

import re

def get_user_string(message: str) -> str:
    while not (user_input := input(message)):
        print('Wpisz cos')
    return user_input


def get_char_to_multi(message: str) -> str:
    while not re.match('^[A-Za-z]{1}$', user_input := input(message)):
        print('Wprowadz jedna literke!')
    return user_input


def multiply_given_char_in_text(char_to_multiply: str, text: str, n: int) -> str:
    return ''.join([letter * n if letter == char_to_multiply else letter for letter in text])


def main() -> None:
    char_to_multiply = get_char_to_multi('Wprowadz literke: ')
    user_string = get_user_string(f'Wprowadz tekst, w ktorym zostanie powielona literka {char_to_multiply}: ')
    modified_string = multiply_given_char_in_text(char_to_multiply, user_string, 3)
    print(modified_string)

if __name__ == '__main__':
    main()