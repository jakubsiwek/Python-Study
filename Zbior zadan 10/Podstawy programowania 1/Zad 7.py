# Napisz program, w którym pobierasz od użytkownika trzy liczby, dopóki
# ilość cyfr parzystych (+2 sztuki dodajmy do parzystych na start) we wszystkich trzech liczbach nie będzie większa od ilości wszystkich cyfr pobieranych liczb.


def get_numbers() -> (int, int, int):
    return int(input('Podaj pierwsza liczbe: ')), int(input('Podaj druga liczbe: ')), int(input('Podaj trzecia liczbe: '))


def count_digits_in_numbers(numbers: tuple) -> int:
    while True:
        s = 0
        for i in numbers:
            while i > 0:
                s += 1
                i //= 10
        print(s)
        return s


def count_even_digits_in_numbers(numbers: tuple) -> int:
    while True:
        s = 2   # dorzucamy dwie sztuki bo inaczej sie nie uda
        for i in numbers:
            while i > 0:
                if i % 2 == 0:
                    s+= 1
                i //= 10
        print(s)
        return s


def compare_conditions() -> None:
    while True:
        numbers = get_numbers()
        if count_digits_in_numbers(numbers) > count_even_digits_in_numbers(numbers):
            continue
        break


if __name__ == '__main__':
    compare_conditions()
