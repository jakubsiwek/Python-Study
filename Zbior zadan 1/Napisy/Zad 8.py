# Zad 8
# Pobierz od użytkownika napis i sprawdź, ile występuje w nim wyrazów.
# Zbadaj, ile wyrazów zaczyna się z dużej litery oraz ile wyrazów zaczyna
# się z małej litery. Wypisz na ekranie otrzymane wyniki.


import re


def count_words(message: str) -> {}:
    words = {
        'lower_letter_at_start': 0,
        'upper_letter_at_start': 0
    }

    def get_user_string(message: str) -> str:
        while not re.match('\w+', user_string := input(message)):
            print('Wpisz napis!')
        return user_string

    user_string = get_user_string(message)

    def count_words_upper_letter(user_string: str) -> None:
        counter = re.findall('[A-Z][a-zA-Z]+', user_string)
        words['upper_letter_at_start'] += len(counter)

    def count_words_lower_letter(user_string: str) -> None:
        counter = re.findall('(\s+[a-z][a-z]+)', user_string)
        counter2 = re.findall('^[a-z]\w+', user_string)
        words['lower_letter_at_start'] += len(counter)
        words['lower_letter_at_start'] += len(counter2)

    count_words_lower_letter(user_string)
    count_words_upper_letter(user_string)

    [print(f'Liczba slow {k} wynosi {v}') for k, v in words.items()]


def main() -> None:
    count_words('Wprowadz tekst: ')


if __name__ == '__main__':
    main()
    # print(re.findall('[A-Z][a-zA-Z]+', 'Marek ma Dwa Koty i Trojke dzieci'))
    # words = {
    #     'lower_letter_at_start': 0,
    #     'upper_letter_at_start': 0
    # }
    # words['lower_letter_at_start'] += 3
    # print(words)


# --------------------------------------- 2 sposób -----------------------------------------------
#
# def get_words(text: str) -> list[str]:
#     return re.split(r'\s+', text)
#
# def count_words(text: str) -> int:
#     return len(get_words(text))
#
# def count_lowercase_uppercase_words(text: str) -> dict[str, int]:
#     words = get_words(text)
#
#     counted_words = {'lower': 0, 'upper': 0}
#     for word in words:
#         if re.match(f'^[a-z].*', word):
#             counted_words['lower'] += 1
#         elif re.match(f'^[A-Z].*', word):
#             counted_words['upper'] += 1
#
#     return counted_words
#
# def main() -> None:
#     text = 'Dzisiaj jest wtorej a JUtro JEst Sroda'
#     print(count_words(text))
#     print(count_lowercase_uppercase_words(text))
#
# if __name__ == '__main__':
#     main()