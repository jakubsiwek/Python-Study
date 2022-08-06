# Pobierz od użytkownika dwa napisy i wygeneruj trzeci napis. Trzeci
# napis zawiera na początku same samogłoski z napisu pierwszego, a następnie same spółgłoski z napisu drugiego.
# Przykład: napis pierwszy
# -> abcdef, napis drugi -> ghijkl, wynik -> aeghjkl.

def get_all_consonants_from_string(txt: str) -> str:
    return ''.join([x for x in txt if x not in 'aeiuo'])


def get_two_inputs() -> (str, str):
    while True:
        input_1 = input('Podaj pierwszy napis: ')
        input_2 = input('Podaj drugi napis: ')
        if input_1 and input_2:
            return input_1, input_2


if __name__ == '__main__':
    txt_1, txt_2 = get_two_inputs()
    print(get_all_consonants_from_string(txt_1))
    print(get_all_consonants_from_string(txt_2))