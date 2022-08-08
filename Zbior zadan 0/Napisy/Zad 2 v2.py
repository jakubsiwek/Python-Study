# Pobieraj od użytkownika dwa napisy, dopóki pierwszy napis nie będzie zawierał tyle
# spółgłosek co drugi napis samogłosek. Następnie z drugiego napisu usuń wszystkie
# samogłoski, a w miejsce każdej usuwanej samogłoski wstawiaj kolejną spółgłoskę z
# pierwszego napisu.

import re


def get_user_strings() -> []:
    while True:
        user_text_1 = input('Wpisz pierwszy napis: ')
        user_text_2 = input('Wpisz drugi napis: ')
        vowels_1 = re.sub('[^aeiouy]', '', user_text_1)
        consonants_2 = re.sub('[aeiouy]', '', user_text_2)
        if len(consonants_2) == len(vowels_1):
            return [user_text_1, user_text_2]


def edit_second_string(strings: []) -> []:
    edited_string = strings[1]
    consonants = [i for i in strings[0] if i not in 'aeiou']  # spolgloski z pierwszego napisu
    tmp = []  # tmp, ktore bedzie przechowywac kolejne spolgloski z drugiego napisu lub spolgloski z pierwszego przy wymianie
    i = 0  # licznik zeby wstawiac kolejne spolgloski z pierwszego napisu
    for c in edited_string:
        if c not in 'aeiuo':
            tmp.append(c)
            continue
        tmp.append(consonants[i])
        i += 1
    strings[1] = ''.join(tmp)
    print('Drugi napis po zmianie to: ' + ''.join(tmp))


def main() -> None:
    user_inputs = get_user_strings()
    edit_second_string(user_inputs)


if __name__ == '__main__':
    main()
