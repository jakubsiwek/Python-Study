# Pobieraj od użytkownika trzy liczby typu int do zmiennych a, b, c
# dopóki ich iloczyn nie będzie liczbą większą od 10 oraz nie będzie
# zachodził warunek a < b < c. Następnie oblicz sumę liczb z przedziałów
# <a,b> oraz <b,c> i wypisz na ekranie większa z otrzymanych sum.


def get_three_numbers() -> (int, int, int):
    while True:
        num1 = int(input('Podaj pierwsza liczbe: '))
        num2 = int(input('Podaj druga liczbe: '))
        num3 = int(input('Podaj trzecia liczbe: '))
        if num1 < num2 < num3 and num1 * num2 * num3 > 10:
            return num1, num2, num3


def count_ranges(value1: int, value2: int, value3: int) -> int:
    first_range_sum = 0
    second_range_sum = 0
    for i in range(value1, value2 + 1, 1):
        first_range_sum += i
    for j in range(value2, value3 + 1, 1):
        second_range_sum += j
    return first_range_sum if first_range_sum > second_range_sum else second_range_sum


if __name__ == '__main__':
    number1, number2, number3 = get_three_numbers()
    print(count_ranges(number1, number2, number3))

