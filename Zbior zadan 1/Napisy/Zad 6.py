# Zad 6
# Pobierz od użytkownika napis. Kod ASCII wszystkich znaków, które
# znajdują się pod indeksem parzystym zwiększ o 10, natomiast kod ASCII
# pozostałych znaków zmniejsz o 5. Po tej zmianie oblicz, ile liter
# znajduje się w zmodyfikowanym napisie.
import math
import re


def get_user_string(message: str) -> str:
    while True:
        while not (user_input := input(message)):
            print('Musisz wpisac chociaz jeden znak! ')
        return user_input


def change_ascii_codes(user_string: str) -> str:
    tmp2 = ''.join([chr(i) for i in [(ord(user_string[i]) + 10) if i % 2 == 0 else (ord(user_string[i]) + 5) for i in
                                     range(len(user_string))]])
    return tmp2


def count_letters_in_string(changed_user_string: str) -> int:
    return len(re.findall('[A-Za-z]', changed_user_string))


def main() -> None:
    MESSAGE = 'Podaj napis: '
    tmp = change_ascii_codes(get_user_string(MESSAGE))
    print(f'Zmieniony tekst to: {str(tmp)}')
    words_counter = count_letters_in_string(tmp)
    print(f'Liczba liter wynosi: {words_counter}')


if __name__ == '__main__':
    main()
    a1 = [1, 2, 3]
    print(*a1)
