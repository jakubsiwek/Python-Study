# Pobieraj od użytkownika dwa napisy, dopóki pierwszy napis nie będzie zawierał tyle
# spółgłosek co drugi napis samogłosek. Następnie z drugiego napisu usuń wszystkie
# samogłoski, a w miejsce każdej usuwanej samogłoski wstawiaj kolejną spółgłoskę z
# pierwszego napisu.


def get_string_from_user(message: str) -> str:
    while True:
        user_input = input(message)
        if user_input:
            return user_input
        print('Wpisz cos.')


def input_vowels_and_consonants_comparator(text1: str, text2: str) -> bool:
    vowels_count = 0
    consonants_count = 0
    for c in text1:
        if c in 'aeiuoy':
            vowels_count += 1
    for c in text2:
        if c not in 'aeiuoy' and not c.isdigit():
            consonants_count += 1
    return consonants_count == vowels_count


# Następnie z drugiego napisu usuń wszystkie
# # samogłoski, a w miejsce każdej usuwanej samogłoski wstawiaj kolejną spółgłoskę z
# # pierwszego napisu.


def change_string(txt1: str, txt2: str) -> str:
    lst = []
    tmp = 0
    for c in txt2:
        if c not in 'aeiou':
            lst.append(c)
            continue
        for i in range(tmp, len(txt1)):
            if txt1[i] not in 'aeiou':
                lst.append(txt1[i])
                if tmp == 0:
                    tmp += 1
                    break
                tmp = i
    print(lst)

change_string('msadme', 'ereiupz')

