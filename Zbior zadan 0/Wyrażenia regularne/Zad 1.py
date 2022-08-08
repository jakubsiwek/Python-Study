# Pobieraj od użytkownika numer PESEL, dopóki nie będzie on poprawny. Oprócz
# wyrażeń regularnych zastosuj również własną walidację sprawdzającą poprawność
# numeru PESEL.

import re

def get_user_pesel(message: str) -> []:
    while not re.search('\d{11}', user_input := input(message)):
        'Wprowadz pesel skladajacy sie z samych cyfr (11)'
    print(user_input)
    return list(user_input)


def check_if_pesel_is_valid(user_pesel: []) -> bool:
    tmp = user_pesel[:len(user_pesel) - 1]
    tmp = [int(i) for i in tmp]
    factors = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    valid_sum = sum(list(map(lambda x, y : x * y, tmp, factors)))
    last_digit = user_pesel[len(user_pesel) - 1]
    print(f'Ostatnia cyfra peselu: {last_digit}')
    print(10 - valid_sum % 10)
    if int(last_digit) == 10 - valid_sum % 10:
        return True
    raise ValueError('Podales bledny pesel :) ')


def main() -> None:
    user_pesel =  get_user_pesel('Podaj pesel: ')
    print(user_pesel)
    if check_if_pesel_is_valid(user_pesel):
        print('Pesel jest ok')


if __name__ == '__main__':
    main()

