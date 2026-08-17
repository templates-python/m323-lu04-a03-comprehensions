"""Quadrate aller geraden Zahlen.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu04/aufgaben/comprehensions1
"""

def squares_of_even_numbers():
    # TODO: Erstelle eine Liste der Quadrate aller geraden Zahlen von 1 bis 100
    return [i**2 for i in range(2, 102, 2)]


if __name__ == '__main__':
    result = squares_of_even_numbers()
    print(result)
