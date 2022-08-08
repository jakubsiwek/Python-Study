# Pobieraj od użytkownika napis dopóki suma cyfr, które się w nim znajdują nie będzie
# większa od 20. Następnie wyznacz wartość największej cyfry i sprawdź czy dzieli się
# ona przez najmniejszą cyfrę w napisie.

import re


def get_user_num(message: str, value: int) -> str:
    while True:
        sum = 0
        while not re.match(r'^\d+$', user_input := input(f'{message}{value}: ')):
            print('Nie wpisales liczby')
        for c in user_input:
            sum += int(c)
        if sum > value:
            return user_input


def find_lowest_and_highest_digit(number: str) -> (int, int):
    digits = re.findall(r'\d', number)
    return int(max(digits)), int(min(digits))


def main() -> None:
    MESSAGE = 'Podaj liczbe, ktorej suma cyfr jest mniejsza od '
    user_num = get_user_num(MESSAGE, 20)
    max_digit, min_digit = find_lowest_and_highest_digit(user_num)
    print(max_digit, min_digit)


if __name__ == '__main__':
    main()
