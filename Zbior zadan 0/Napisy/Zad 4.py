# Pobieraj od użytkownika napis dopóki suma cyfr, które się w nim znajdują nie będzie
# większa od 20. Następnie wyznacz wartość największej cyfry i sprawdź czy dzieli się
# ona przez najmniejszą cyfrę w napisie.

from typing import Final


def get_user_digits_string(message: str) -> str:
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return user_input
        print('Napis nie sklada sie z samych cyfr!')


def check_digits_sum_in_string_and_division(txt: str) -> sum:
    s = 0
    txt_list = list(txt)
    min_number = int(min(txt_list))
    for i in txt:
        s += int(i)
    print(f'Najmniejsza cyfra we wpisanej liczbie to {min_number}')
    print('Suma cyfr we wpisanej liczbie dzieli sie przez najmniejsza cyfre liczby') if s % min_number == 0 else \
        print('Suma cyfr we wpisanej liczbie nie dzieli sie przez najmniejsza cyfre liczby')
    return s


def main() -> None:
    MESSAGE: Final = 'Podaj napis skladajacy sie z cyfr bez spacji: '
    while True:
        user_num = get_user_digits_string(MESSAGE)
        if check_digits_sum_in_string_and_division(user_num) > 20:
            print('Wpisana liczba ma sume cyfr > 20, OK')
            break
        else:
            print('Suma cyfr wpisanej liczby jest mniejsza niz 20')


if __name__ == '__main__':
    main()
