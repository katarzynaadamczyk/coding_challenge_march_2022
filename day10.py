''' Solution to task from https://www.instagram.com/p/Ca6kMWOgS0I/ '''


import pandas as pd
from random import randint
import string


def names_generator(nameslst, surnameslst) -> string:
    return nameslst[randint(0, len(nameslst) - 1)] + ' ' + surnameslst[randint(0, len(surnameslst) - 1)]


def main():
    namelst = list(pd.read_csv('day10datanames.csv', sep=',')['IMIE'])
    surnamelst = list(pd.read_csv('day10datasurnames.csv', sep=',')['Nazwisko'])
    for i in range(10):
        print(names_generator(namelst, surnamelst))


if __name__ == '__main__':
    main()
    