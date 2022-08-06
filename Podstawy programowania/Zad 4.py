# Pobierz od użytkownika dwie zmienne typu double o nazwach bok1 oraz
# bok2. Będą one reprezentowały boki trójkątów równobocznych.
# Zaimplementuj instrukcję, która wyświetli na ekranie informację, jakim
# procentem pola trójkąta równobocznego o boku bok1 jest pole trójkąta
# równobocznego o boku bok2.


def get_triangle_sides() -> (float, float):
    side1 = float(input('Podaj pierwszy bok trojkata rownobocznego: '))
    side2 = float(input('Podaj pierwszy bok trojkata rownobocznego: '))

    def count_ratio() -> int:
        ratio = (side1 / side2) ** 2
        return int(ratio * 100)

    return count_ratio()


if __name__ == '__main__':
    print(f'Stosunek pola pierwszego do drugiego wynosi: {get_triangle_sides()}%')
