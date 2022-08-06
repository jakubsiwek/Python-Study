# Pobierz od użytkownika liczbę typu int. Następnie wypisz na ekranie
# wszystkie potęgi liczby 2, które będą mniejsze od podanej liczby co
# najmniej o 5 .


def get_num() -> int:
    return int(input('Give number: '))


def print_out(input_value: int) -> None:
    i = 0
    print('Powers of two which are lower than input value by 5 are: ')
    while abs(input_value) - (2 << i) > 5:
        print(2 << i, end=' ')
        i += 1


if __name__ == '__main__':
    print_out(get_num())
