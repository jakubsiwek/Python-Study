# Pobieraj od użytkownika napis dopóki nie będzie palindromem o parzystej sumie
# kodów ASCII. Następnie wszystkie samogłoski w tym napisie zastąp najbliżej znajdującą
# się spółgłoską o większym kodzie ASCII. Wypisz tak zmodyfikowany napis.


def is_palindrome(txt: str) -> bool:
    return txt == txt[::-1]


def get_string_from_user(message: str) -> str:
    while True:
        user_input = input(message)
        if is_palindrome(user_input) and len(user_input) > 2:
            return user_input
        print('Wprowadzony tekst nie jest palindromem')


def check_if_ascii_sum_is_even(txt: str) -> bool:
    ascii_sum = sum(ord(x) for x in txt)
    return True if ascii_sum % 2 == 0 else False


def is_vowel(c: str) -> bool:
    if c.isalpha():
        return c.lower() in 'aeyiuo'
    return False


def change_vowels(txt: str) -> str:
    new = [ord(c)+1 if is_vowel(c) else ord(c) for c in txt]
    new_letters = [chr(c) for c in new]
    return ''.join(new_letters)


def main() -> None:
    while True:
        input_text = get_string_from_user('Wpisz cos: ')
        if check_if_ascii_sum_is_even(input_text):
            print(change_vowels(input_text))
            break
        print('Wpisany tekst nie mial sumy ascii parzystej!')


if __name__ == '__main__':
    main()





