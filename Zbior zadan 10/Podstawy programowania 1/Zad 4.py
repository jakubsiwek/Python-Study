# Napisz program, w którym użytkownik podaje dwie liczby całkowite,
# dopóki ich suma nie będzie większa od szescianu sumy cyfr większej z podanych
# liczb.


def count_cube_sum(input_value: int) -> int:
    x1 = len(str(input_value))
    temp = 0
    for i in range(0, x1, 1):
        temp += (input_value // 10**i) % 10
    return temp ** 3


def choose_higher(choose_1: int, choose_2: int) -> int:
    if choose_1 >= choose_2:
        return choose_1
    return choose_2


def check_condition() -> (int, int, int):
    while ((x1 := int(input('Podaj pierwsza liczbe: '))) + (x2 := int(input('Podaj druga liczbe: ')))) < count_cube_sum(choose_higher(x1, x2)):
        pass
    return x1, x2, count_cube_sum(choose_higher(x1, x2))


if __name__ == '__main__':
    input_1, input_2, cubed_sum = check_condition()
    print('Udalo sie. Suma wspianych liczb jest wieksza od szescianu sumy cyfr wiekszej z wpisanych liczb!')
    x = input()
    print(type(x))