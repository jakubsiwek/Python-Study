# Pobieraj od użytkownika trzy napisy dopóki nie będą posiadały tej samej długości.
# Pierwszy napis musi składać się z samych małych liter, drugi wyraz musi składać się z
# samych dużych liter, a trzeci napis musi mieć parzystą długość i tyle samo samogłosek
# co spółgłosek. Następnie na koniec napisu pierwszego dołącz wszystkie samogłoski z
# napisu trzeciego, a na początek napisu drugiego dołącz wszystkie spółgłoski z napisu
# trzeciego. Wypisz na ekranie trzy napisy, którymi posługiwałeś się w tym programie i
# wyznacz ten, który ma najwięcej samogłosek i ten który ma najwięcej spółgłosek.

from typing import Final


def get_string_from_user(message: str) -> str:
    while True:
        user_input = input(message)
        if user_input:
            return user_input
        print('Wpisz cos.')


def check_third_string(txt: str) -> bool:
    vowels_count = 0
    consonants_count = 0
    for c in txt:
        if c in 'aeiouy':
            vowels_count += 1
        else:
            consonants_count += 1
    if len(txt) % 2 == 0 and vowels_count == consonants_count:
        return True
    return False


def get_three_strings(message1: str, message2: str, message3: str) -> (str, str, str):
    while True:
        input_1 = get_string_from_user(message1)
        input_2 = get_string_from_user(message2)
        input_3 = get_string_from_user(message3)
        if len(input_1) == len(input_2) == len(input_3):
            if input_1.isupper() and input_2.islower() and check_third_string(input_3):
                return input_1, input_2, input_3


def change_first_and_second_string(input_1: str, input_2: str, input_3: str) -> (str, str):
    tmp_1 = list(input_1)
    tmp_2 = list(input_2)
    for c in input_3:
        if c in 'aeiuoy':
            tmp_1.append(c)
            continue
        tmp_2.append(c)
    return ''.join(tmp_1), ''.join(tmp_2)


def check_which_txt_has_most_vowels(inputs: list) -> str:
    max_counter = 0
    vowels_count = 0
    texts_with_most_vowels = list()
    for txt in inputs:
        for c in txt:
            if c in 'aeiuoy':
                vowels_count += 1
        if vowels_count >= max_counter:
            texts_with_most_vowels.append(txt)
            max_counter = vowels_count
        vowels_count = 0

    return ', '.join(texts_with_most_vowels)


def main() -> None:
    MESSAGE_1: Final = 'Podaj pierwszy napis, ktory musi miec same duze litery: '
    MESSAGE_2: Final = 'Podaj drugi napis, ktory musi miec same same litery: '
    MESSAGE_3: Final = 'Podaj trzeci napis, ktory musi miec parzysta dlugosc oraz tyle samo samoglosek co spolglosek: '
    user_input_1, user_input_2, user_input_3 = get_three_strings(MESSAGE_1, MESSAGE_2, MESSAGE_3)
    print('Poprawnie wpisane napisy to: {}, {}, {}'.format(user_input_1, user_input_2, user_input_3))
    change_user_input_1, changed_user_input_2 = change_first_and_second_string(user_input_1, user_input_2, user_input_3)
    print(f'Zmieniony pierwszy i drugi napis to: {change_user_input_1}, {changed_user_input_2}')
    user_inputs = [user_input_1.lower(), user_input_2.lower(), user_input_3.lower()]
    print(f'Napisy ktore maja najwiecej samoglosek to: {check_which_txt_has_most_vowels(user_inputs)}')


if __name__ == '__main__':
    main()
