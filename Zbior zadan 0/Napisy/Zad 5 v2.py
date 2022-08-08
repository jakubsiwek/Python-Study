# Pobieraj od użytkownika napis dopóki suma cyfr, które się w nim znajdują nie będzie
# większa od 20. Następnie wyznacz wartość największej cyfry i sprawdź czy dzieli się
# ona przez najmniejszą cyfrę w napisie.

import re


def get_user_input(message: str) -> str:
    while True:
        user_input = input(message)
        if user_input:
            return user_input
        print('Wpisz cos')


def get_digits_from_string(user_input: str) -> str:
    digits_in_string = re.sub('\D+', '', user_input)
    return digits_in_string


def count_sum_of_string_digits(user_input_digits: str) -> int:
    digits_sum = 0
    for i in user_input_digits:
        digits_sum += int(i)
    return digits_sum


def main() -> None:
    user_input = get_user_input('Wpisz tekst: ')
    digits = get_digits_from_string(user_input)
    digits_sum = count_sum_of_string_digits(digits)
    print(f'Suma cyfr we wpisanym napisie: {user_input} wynosi: {digits_sum}')


if __name__ == '__main__':
    main()