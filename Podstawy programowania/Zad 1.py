# Pobierz od użytkownika wartość – liczbę rzeczywistą, którą przechowasz
# w zmiennej typu double o nazwie x. Dla pobranej wartości wyznacz
# wartość wielomianu W(x) = 2x^12 + 3x^5-4x^2

def user_input() -> float:
    while not (input_num := input('Please input float number: ').isdigit()):
        print(f'Given input: {input_num} is not a number.')
    return input_num


def polynomial_value() -> float:
    x = user_input()
    pol_value = 2 * x**12 + 3 * x**5 - 4 * x**2
    return pol_value


if __name__ == '__main__':
    print(poly_value := polynomial_value())

