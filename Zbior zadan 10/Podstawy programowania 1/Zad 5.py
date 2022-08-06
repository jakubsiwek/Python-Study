# Napisz program, w którym użytkownik podaje liczbę całkowitą i wyznacza,
# ile jest w niej cyfr parzystych, znajdujących się na pozycji parzystej.
# Zakładamy, że cyfra jedności ma pozycję parzystą, cyfra dziesiątek
# ma pozycję nieparzystą, cyfra setek ma pozycję parzystą itd.


def count_even_digits(input_1: int) -> int:
    x1 = len(str(input_1))
    temp = 0
    for i in range(0, x1, 1):
        if i % 2 == 0:
            val = (input_1 // 10 ** i) % 10
            if val % 2 == 0:
                temp += 1
    return temp


if __name__ == '__main__':
    number = abs(int(input('Give number to count even digits at even places inside it: ')))
    print(f'Number of even digits at even places is equal: {count_even_digits(number)}')


