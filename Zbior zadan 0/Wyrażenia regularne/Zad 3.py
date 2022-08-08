# Pobieraj od użytkownika informacje o samochodzie, dopóki nie będzie miała ona
# postaci:
# MARKA_POJEMNOSC_PRZEBIEG_CENA, przykładowo AUDI_1.5_150000_120000.
# Zakładamy, że marka musi być napisana z dużych liter, pojemność ma zawsze jedno
# miejsce po przecinku i separator w postaci kropki, przebieg ma wartość od 0 do 500000
# oraz cena jest zawsze powyżej 50000. Informacje są oddzielone od siebie za pomocą
# znaku ‘_’ Oprócz wyrażeń regularnych zastosuj dodatkowe instrukcje realizujące
# walidację.

import re

def get_user_string() -> str:
    # while not re.search('[A-Z]+_[0-9]{1}\.[0-9]{1}_[0-9]{0, 6}_[0-9]{5, }', user_input := input('Podaj info')):
    while not re.search('[A-Z]+_[0-9]{1}\.[0-9]{1}_(500000|[1-4]\d{5}|[1-9]\d{0,4}|0)_([5-9]\d{4}$|[1-9]\d{5,})', user_input := input('Podaj info o aucie: ')):
        print('Cos zle wpisales. Ma byc np. \'BMW_1.3_150000_120000\' gdzie Ostatnia liczba ma byc > 50000'
              'a przed ostatnia ma byc mniejsza od 500000')
    return user_input


print(get_user_string())