# Pobieraj od użytkownika napis, dopóki jego długość nie będzie liczbą
# parzystą. Następnie zamień miejscami kolejne pary znaków, tak jak
# pokazano to w przykładzie: przed -> ABCDEF, po -> BADCFE. Wypisz
# zmodyfikowany napis.

def get_user_string(message: str) -> str:
    while len(txt := input(message)) % 2 != 0 or len(txt) == 0:
        pass
    return txt


def swap(txt: str) -> str:
    tmp = list(txt)
    print(tmp)
    for i in range(0, len(txt) - 1, 2):
        tmp[i], tmp[i + 1] = txt[i + 1], txt[i]
    return ''.join(tmp)


if __name__ == '__main__':
    print(get_user_string('Podaj tekst: '))
    print(swap('programminge'))

# def swap_elements_in_string(txt: str) -> str:
#     tmp = []
#     new_string = ''
#     if len(txt) % 2 != 0:
#         for i in range(0, len(txt) - 2, 2):
#                 i += 1
#                 tmp.append(txt[i])
#                 i -= 1
#                 tmp.append(txt[i])
#         tmp.append(txt[len(txt)-1])
#         new_string = ''.join(tmp)
#         return new_string
#     for i in range(0, len(txt), 2):
#         i += 1
#         tmp.append(txt[i])
#         i -= 1
#         tmp.append(txt[i])
#     new_string = ''.join(tmp)
#     return new_string

