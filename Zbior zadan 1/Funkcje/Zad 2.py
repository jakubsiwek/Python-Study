# Napisz funkcję, która przyjmuje jako argument napis i zamienia w nim
# wszystkie duże litery na małe, a małe litery na duże. Funkcja zwraca
# tak zmodyfikowany napis.

def my_swap_case(text: str) -> str:
    return ''.join([letter.lower() if letter.isupper() else letter.upper() for letter in text])

text = 'AlA ma KotA'
print(my_swap_case(text))