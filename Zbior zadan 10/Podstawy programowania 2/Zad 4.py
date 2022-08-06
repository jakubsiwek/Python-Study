# Napisz program, który symuluje prostą grę dwuosobową. Aplikacja prosi
# pierwszego użytkownika o podanie dowolnej liczby z przedziału
# <100, 999>. Następnie drugi użytkownik podaje liczby, dopóki nie uda
# mu się podać takiej, która ma identyczną sumę cyfr, jak liczba podana
# przez przeciwnika. Należy zliczyć ilość prób, które potrzebował gracz,
# żeby podać prawidłową liczbę. Następnie drugi gracz podaje liczbę
# i gracz pierwszy musi na tych samych zasadach podać liczbę. Gra kończy
# się, kiedy jeden z graczy będzie potrzebował więcej niż 5 prób
# na podanie prawidłowej liczby. Nie zapomnij na koniec wyświetlić
# informacji o zwycięzcy.


def get_number(message: str) -> int:
    while True:
        try:
            input_number = int(input(message))
            if 1000 > input_number > 99:
                return input_number
        except ValueError:
            print('Podaj liczbe! ')


def count_numbers_digits_sum(number: int) -> int:
    numbers_abs = abs(number)
    s = 0
    while numbers_abs > 0:
        s += numbers_abs % 10
        numbers_abs //= 10
    return s


def player_2_turn(player_2_trials: int) -> int:
    player_1_number = get_number('Graczu pierwszy podaj liczbe, ktorej sume ma zgadnac gracz drugi: ')
    while player_2_trials < 6:
        player_1_number_sum = count_numbers_digits_sum(player_1_number)
        player_2_input = get_number('Graczu numer 2, sprobuj odgadnac sume cyfr liczby podanej przez gracza pierwszego: ')
        if player_2_input != player_1_number_sum:
            player_2_trials += 1
        if player_2_input == player_1_number_sum:
            player_2_trials += 1
            return player_2_trials
    return player_2_trials


def player_1_turn(player_1_trials: int) -> int:
    player_2_number = get_number('Graczu drugi podaj liczbe, ktorej sume ma zgadnac gracz pierwszy: ')
    while player_1_trials < 6:
        player_2_number_sum = count_numbers_digits_sum(player_2_number)
        player_1_input = get_number('Graczu numer 1, sprobuj odgadnac sume cyfr liczby podanej przez drugiego: ')
        if player_1_input != player_2_number_sum:
            player_1_trials += 1
        if player_1_input == player_2_number_sum:
            player_1_trials += 1
            return player_1_trials
    return player_1_trials


def game() -> None:
    player_1_score = 0
    player_2_score = 0
    while player_1_score < 6 and player_2_score < 6:
        player_1_score = player_1_turn(player_1_score)
        player_2_score = player_2_turn(player_2_score)
    print(f'Liczba prob gracza pierwszego to: {player_1_score} a drugiego gracza to: {player_2_score}')

game()