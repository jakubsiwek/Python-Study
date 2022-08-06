# Pobierz od użytkownika napis. Kod ASCII wszystkich znaków, które
# znajdują się pod indeksem parzystym zwiększ o 10, natomiast kod ASCII
# pozostałych znaków zmniejsz o 5. Po tej zmianie oblicz, ile liter
# znajduje się w zmodyfikowanym napisie.
#

from typing import Final


def get_string_from_user(message: str) -> str:
    while not (txt := input(message)):
        pass
    return txt


def change_ascii_code(txt: str) -> str:
    ascii_codes = [ord(x) for x in txt]
    for i in range(len(ascii_codes)):
        if ascii_codes[i] % 2 == 0:
            ascii_codes[i] += 10
        else:
            ascii_codes[i] += 5
    new_string = [chr(i) for i in ascii_codes]
    return ''.join(new_string)


def count_letters_in_string(txt: str) -> int:
    count = 0
    for c in txt:
        if c.isalpha():
            count += 1
    return count


def main() -> None:
    MESSAGE: Final = 'Wprowadz tekst: '
    user_input = get_string_from_user(MESSAGE)
    changed_user_input = change_ascii_code(user_input)
    print(f'Zmieniony tekst to: {changed_user_input}')
    print(f'Liczba liter w zmienionym tekscie to: {count_letters_in_string(changed_user_input)}')


if __name__ == '__main__':
    main()

