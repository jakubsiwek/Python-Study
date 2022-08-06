# Zad 3
# Pobierz od użytkownika napis i wykonaj zestawienie, w którym wypiszesz, ile w napisie jest małych liter, dużych liter oraz cyfr.

import re

def get_string_from_user() -> str:
    while True:
        user_input = input('Wprowadz tekst: ')
        if user_input:
            return user_input
        print('Musisz cos wpisac')

def count_digits_in_string(user_input: str) -> int:
    return len(re.sub('\D', '', user_input))


def main() -> None:
    user_input = get_string_from_user()
    print(count_digits_in_string(user_input))


if __name__ == '__main__':
    main()