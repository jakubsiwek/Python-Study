# Pobieraj od użytkownika napis, dopóki nie będzie składał się z samych
# dużych liter. Przeprowadź analizę pobranego napisu:
# a) Zlicz, ile w napisie znajduje się znaków, których kod ASCII
# posiada nieparzystą cyfrę jedności

from typing import Final


def get_user_string(message: str) -> str:
    while True:
        text = input(message)
        if text.isupper():
            return text


def check_ascii_ones(text: str) -> int:
    n = 0
    for c in text:
        if (ord(c) % 10) % 2 == 1:
            n += 1
    return n

# b) Oblicz sumę kodów ASCII znaków znajdujących się na parzystych
# indeksach w napisie. Następnie znajdź pierwszą liczbę z
# przedziału <65, 90>, która jest dzielnikiem wyznaczonej wcześniej
# sumy. Będzie to kod ASCII jednej z dużych liter alfabetu. Zlicz,
# ile w napisie występuje liter większych od wyznaczonej litery.


def find_bigger_letter_from_given_condition(text: str, min_val: int, max_val: int) -> int:

    def count_sum_ascii() -> int:
        s = 0
        for i, c in enumerate(text):
            if i % 2 == 0:
                s += ord(c)
        return s

    ascii_sum = count_sum_ascii()

    def find_first_value_from_range_which_is_divisor(min_value: int, max_value: int) -> int:
        for i in range(min_value, max_value):
            if ascii_sum % i == 0:
                return i
        raise ValueError('Podany napis nie ma dzielnika z danego przedzialu')

    return find_first_value_from_range_which_is_divisor(min_val, max_val)


def count_bigger_chars_than_given(ascii_char: int, txt: str) -> int:
    s = 0
    for c in txt:
        if ord(c) > ascii_char:
            s += 1
    return s


def main() -> None:
    MESSAGE: Final = 'Podaj napis skladajacy sie tylko z duzych liter! '
    MIN_RANGE: Final = 65
    MAX_RANGE: Final = 90
    user_input = get_user_string(MESSAGE)
    found_ascii = find_bigger_letter_from_given_condition(user_input, MIN_RANGE, MAX_RANGE)
    chars_num = count_bigger_chars_than_given(found_ascii, user_input)
    print(f'W napisie wystepuje wiecej o {chars_num} wiekszych liter wiecej od {chr(found_ascii)}')


if __name__ == '__main__':
    main()




