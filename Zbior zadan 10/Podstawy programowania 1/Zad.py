


def outer_function(number: int):
    x = 10
    y = 5

    def inner_function(number2: int):
        number = 7
        nonlocal x
        x+= 1
        print(x)
        print(number)
        return number2 + number
    print(number)
    return inner_function

z = outer_function(3)

o = z(5)
print(o)

#
#
# b = 1.25
# from fractions import Fraction
# n = Fraction(b)
# print(n)
# z = Fraction(2, 3)
# print(z)
#
# tekst = 'Kot'
# tekst2 = 'tok'
# print(tekst[::-1] == tekst2)
#
# text_moj = 'Marcinek Jest swirem '
# count_small = sum(c.islower() for c in text_moj)
# print(count_small)
#
#
# lista = [1, 2, 3, 4, 5, 6, 7]
# tmp = list(lista)
# for i in range(0, len(lista) -1, 2):
#     tmp [i], tmp[i + 1] = lista[i + 1], lista [i]
#
# print(tmp)
# print(lista)
#
# nop = 'ala ma koota'
# print(nop.split(sep=' '))