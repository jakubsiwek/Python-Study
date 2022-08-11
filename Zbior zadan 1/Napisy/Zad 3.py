# Zad 3
# Pobierz od użytkownika napis i wykonaj zestawienie, w którym wypiszesz,
# ile w napisie jest małych liter, dużych liter oraz cyfr.

import re


def get_user_string(message: str) -> str:
    while True:
        user_input = input(message)
        if user_input:
            return user_input
        print('Wpisz cos')


def count_numbers_in_string(user_input: str) -> int:
    numbers = len(re.sub('\D+', '', user_input))
    return numbers


def count_small_letters_in_string(user_input: str) -> int:
    small_letters = len(re.sub('[^a-z]+', '', user_input))
    return small_letters


def count_big_letters_in_string(user_input: str) -> int:
    big_letters = len(re.sub('[^A-Z]+', '', user_input))
    return big_letters  # return len(re.sub())


def main() -> None:
    MESSAGE = 'Wpisz tekst do analizy: '
    user_input = get_user_string(MESSAGE)
    print(f'Liczba cyfr w napisie wynosi: count_numbers_in_string(user_input)')
    print(f'Liczba malych liter w napisie wynosi: count_small_letters_in_string(user_input)')
    


if __name__ == '__main__':
    main()