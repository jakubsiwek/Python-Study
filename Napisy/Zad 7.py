# Pobieraj od użytkownika dwa napisy, dopóki nie będą posiadały tej
# samej długości. Następnie wygeneruj trzeci napis, który będzie
# zawierał w sobie na przemian znaki z pierwszego i drugiego napisu.
# Przykładowo wyraz pierwszy ABCD oraz wyraz drugi EFGH dają wynik
# AEBFCGDH.


def get_two_strings() -> (str, str):
    while True:
        input_1 = input('Podaj pierwszy napis: ')
        input_2 = input('Podaj drugi napis: ')
        if input_1 and input_2:
            return input_1, input_2


def new_string(txt1: str, txt2: str) -> str:
    tmp = []
    if len(txt1) >= len(txt2):
        for i in range(0, len(txt2)):
            tmp.append(txt1[i])
            tmp.append(txt2[i])
        for i in range(len(txt2), len(txt1)):
            tmp.append(txt1[i])

    else:
        for i in range(0, len(txt1)):
            tmp.append(txt1[i])
            tmp.append(txt2[i])
        for i in range(len(txt1), len(txt2)):
            tmp.append(txt2[i])

    return ''.join(tmp)


if __name__ == '__main__':
    user_input_1, user_input_2 = get_two_strings()
    print(new_string(user_input_1, user_input_2))
