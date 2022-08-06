# Pobierz od użytkownika napis i sprawdź, ile występuje w nim wyrazów.
# Zbadaj, ile wyrazów zaczyna się z dużej litery oraz ile wyrazów zaczyna
# się z małej litery. Wypisz na ekranie otrzymane wyniki.

def get_string_from_user(message: str) -> str:
    while not (user_input := input(message)):
        print('Wpisz cos!')
    return user_input


def count_words_in_string(txt: str) -> int:
    count = len(txt.split(sep=' '))
    return count


def count_words_starting_with_capital_small(txt: str) -> (int, int):
    count_capital = 0
    count_small = 0
    for word in txt.split(sep=' '):
        if word[0].isupper():
            count_capital += 1
        else:
            count_small += 1
    return count_small, count_capital


if __name__ == '__main__':
    user_string = get_string_from_user('Wprowadz zdanie: ')
    print(f'Liczba wyrazow we wprowadzonym zdaniu: {count_words_in_string(user_string)}')
    num_small, num_capital = count_words_starting_with_capital_small(user_string)
    print(f'Liczba wyrazow zaczynajacych sie z malej litery: {num_small}, z duzej: {num_capital}')
