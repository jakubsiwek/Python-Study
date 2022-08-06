# Pobieraj od użytkownika liczby typu int do zmiennych a i b dopóki a
# nie będzie mniejsze od b. Następnie wyznacz iloczyn tych liczb z
# przedziału <a,b>, których cyfra jedności jest liczbą pierwszą.


def get_numbers() -> (int, int):
    while (num1 := int(input('Podaj pierwsza liczbe: '))) > (num2 := int(input('Podaj druga liczbe: '))):
        pass
    return num1, num2


def check_if_ones_is_prime(num: int) -> int:
    num_ones = num % 10
    if num_ones > 1:  # Czy nie wpisano 1
        for i in range(2, num, 1):
            if num_ones % i == 0:
                return False
        return True
    return False


def range_product(range_min: int, range_max: int) -> int:
    p = 1
    for i in range(range_min, range_max + 1, 1):
        if check_if_ones_is_prime(i):
            p *= i
    return p


if __name__ == '__main__':
    a, b = get_numbers()
    print(range_product(a, b))

