# Pobierz od użytkownika dwa napisy. Wszystkie spółgłoski z pierwszego
# napisu zastąp samogłoską, która jako pierwsza, począwszy od indeksu o
# numerze 0, pojawiła się w napisie drugim. Jeżeli w drugim napisie nie
# wystąpiła samogłoska wyświetl komunikat NIEPRAWIDŁOWE DANE WEJŚCIOWE.

from typing import Final


def is_vowel(c: str) -> bool:
    return c.lower() in 'aeyuioąęó'


def is_consonant(c: str) -> bool:
    return c.isalpha() and c.lower() not in 'aeyuioąęó'


def find_first_vowel(text: str) -> str:
    for t in text:
        if is_vowel(t):
            return t
    raise ValueError('Cannot find vowel in text')


def replace_consonants(text: str, replacer: str) -> str:
    modified_text = []
    for t in text:
        modified_text.append(replacer if is_consonant(t) else t)
    return ''.join(modified_text)


def get_user_strings(message_1: str, message_2: str) -> (str, str):
    while True:
        text_1 = input(message_1)
        text_2 = input(message_2)
        for c in text_2:
            if is_vowel(c):
                return text_1, text_2
        print('NIEPRAWIDLOWE DANE WEJSCIOWE')


def swap_consonants(txt: str, txt2: str) -> str:

    def get_first_vowel() -> str:
        for v in txt2:
            if is_vowel(v) and v.isalpha():
                return v

    swap_char = get_first_vowel()
    chars = []
    for c in txt:
        chars.append(swap_char if not is_vowel(c) else c)
    return ''.join(chars)


def main() -> None:
    MESSAGE1: Final = 'Podaj pierwszy napis: '
    MESSAGE2: Final = 'Podaj drugi napis: '
    user_string_1, user_string_2 = get_user_strings(MESSAGE1, MESSAGE2)
    print(f'Drugi napis po zmianach to: {swap_consonants(user_string_1, user_string_2)}')



if __name__ == '__main__':
    main()
