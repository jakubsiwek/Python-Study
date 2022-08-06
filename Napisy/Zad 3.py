# Pobierz od użytkownika napis i wykonaj zestawienie, w którym wypiszesz,
# ile w napisie jest małych liter, dużych liter oraz cyfr.


def get_text_input(message: str) -> str:
    while not (input_text := input(message)):
        pass
    return input_text


def count_digits_and_letters(text: str) -> (int, int, int):
    digits_ = sum(c.isdigit() for c in text)
    small_letters_ = sum(c.islower() for c in text)
    big_letters_ = sum(c.isupper() for c in text)
    return digits_, small_letters_, big_letters_


def main() -> None:
    txt = get_text_input('Wprowadz tekst: ')
    digits, small, big = count_digits_and_letters(txt)
    print('Ilosc cyfr: {}, ilosc malych liter: {}, ilosc duzych liter: {}'.format(digits, small, big))


if __name__ == '__main__':
    main()

