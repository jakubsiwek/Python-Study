# Napisz program, w którym użytkownik podaje liczbę całkowitą. Sprawdź,
# czy suma cyfr tej liczby jest liczbą pierwszą.


def check_sum(user_input: int) -> bool:
    x = len(str(user_input))
    digits_sum = 0
    if user_input > 1:
        for i in range(0, x, 1):
            digits_sum += (user_input // 10 ** i) % 10
        for j in range(2, digits_sum, 1):
            if digits_sum % j == 0:
                return False
        return True
    return False


def check_sum_2(user_input: int) -> bool:

    def digits_sum(number: int) -> int:
        s = 0
        num_abs = abs(number)
        while num_abs > 0:
            s += num_abs % 10
            num_abs //= 10
        return s

    dig_sum = digits_sum(user_input)
    print(dig_sum)
    for j in range(2, dig_sum//2, 1):
        if dig_sum % j == 0:
            return False
    return True


if __name__ == '__main__':
    if check_sum(value := int(input('Give number to verify: '))):
        print('Sum of digits is prime number ')
    else:
        print('Sum of digits isn\'t prime number')

    if check_sum_2(value := int(input('Give number to verify: '))):
        print('Sum of digits is prime number ')
    else:
        print('Sum of digits isn\'t prime number')

